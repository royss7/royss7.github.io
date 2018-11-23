---
layout: post
categories: Programming
tags: Programming
title: "Java 8 source code reading"
description: Collection
---

*ref to [java8 src code reading](https://www.cnblogs.com/joemsu/p/7667509.html)*

- collection
  1. top interface `java.lang.Iterable` has 3 methods 
  ```  java
  iterator();
  forEach(); // since 1.8;
  spliterator(); // since 1.8, use for stream()
  ```

  2. interface `java.util.Collection extends java.lang.Iterable` methods
  ``` java
  size();
  isEmpty();
  contains();
  @Override iterator();
  toArray();
  toArray(T[] a); // if length of a is <= size(), will copy data to a, then return a; else will new a array and copy data to it then return it.
  add();
  remove();
  // bulk operations
  containsAll();
  addAll();
  removeAll();
  removeIf(); // since 1.8. lambda support, remove all element which meet the condition
  retainAll();
  clear();

  // compare and hash
  equals();
  hashCode();
  @Override spliterator();
  stream(); // since 1.8
  parallelStream(); // since 1.8
  ```

  3. interface `java.util.List extends java.util.Collection`, List is ordered, can be access by integer index, elements can be duplicated, *as consider, will only rare man need unique list(which elements should be unique just as set)*. methods

  ``` java
  replaceAll(); // since 1.8, lambda support, replace all value by apply function on original value
  sort(); // since 1.8, lambda support, it will convert to array by toArray(), then sort the Object Array, at last replace elements will the sorted object
  get(int index);
  set(i, e);
  add(i, e); // support in list but not collection, collection only has add(e)
  remove(i); // list only
  indexOf(e);
  lastIndexOf(e);
  listIterator();
  listIterator(i);
  subList(fromIndex, toIndex);
  @Override spliterator();

  ```

  4. abstract class `java.util.AbstractCollection implements Collection` implements some methods such as `isEmpty() = size() == 0`.

  5. abstract class `java.util.AbstractList extends java.util.AbstractCollection implements java.util.List`. which implement immutable list interface(e.g get(i), but set(i, e) is not), so To implement an unmodifiable list, the programmer needs only to extend this class and provide implementations for the {@link #get(int)} and {@link List#size() size()} methods [[java.util.AbstractList]]. iterator's design, almost all loop operation depends on iterator.

  6. final class ArrayList
  ```
  public class ArrayList<E> extends AbstractList<E>
        implements List<E>, RandomAccess, Cloneable, java.io.Serializable 
  ``` 
  AbstractList has already implements List, why ArrayList implements again? ref [here](https://stackoverflow.com/questions/3854748/why-do-many-collection-classes-in-java-extend-the-abstract-class-and-implement-t)

  7. `java.util.Spliterator` is parallel iterator since java 8. [ref](https://blog.csdn.net/lh513828570/article/details/56673804)

  8. top interface Map `java.util.Map`, methods
  ``` java
  size();
  isEmpty();
  containsKey();
  containsValue();
  get();
  put();
  remove();
  // bulk operation
  putAll();
  clear();
  keySet();
  values(); // why keySet not named as keys?, because keySet return a Set(keys are unique) and values return a collection(values can be duplicate)
  entrySet(); // entry are unique and return a set
  equals();
  hashCode();
  getOrDefault(); // since java 8
  forEach(); // since java 8
  replaceAll(); // since java 8
  putIfAbsent(); // since java 8
  remove(); // since java 8
  replace(); // since java 8
  computeIfAbsent(); // since java 8
  computeIfPresent(); // since java 8
  compute(); // since java 8, same as map?
  merge(); // since java 8
  ```
  internal interface `Entry`, methods
  ``` java
  getKey();
  getValue();
  setValue();
  equals();
  hashCode();
  comparingByKey(); // since java 8
  comparingByValue(); // since java 8
  ```
  10. abstract class `java.util.AbstractMap extends java.util.Map`
  11. final class `java.util.HashMap extends java.util.Abstract implements java.util.Map`, bins will convert between list and tree as the bin counts change. methods:
  ``` java
  Node implements Map.Entry;
  hash(); // hash an object
  tableSizeFor();
  ```
  查找bin的是hash & (n-1), 其中n一定是2的幂，这样可以防止越界，同时比hash % n高效，其中hash是key的hash值。
  resize需求： n * loadFactor >= value count时
  12. final class `java.util.LinkedHashMap extends java.util.HashMap extends java.util.Map`, 因为Hashmap有些bin可能转化为tree了，因此用LinkedHashMap不是很适合，但是已经无法修改了（官方解释）。
  13. interface `java.util.SortedMap extends java.util.Map`, methods
  ``` java
  comparator();
  subMap();
  headMap();
  tailMap();
  firstKey();
  lastKey();
  keySet();
  values();
  entrySet();
  ```

  14. interface `java.util.NavigableMap extends java.util.SortedMap`, methods
  ``` java
  lowerEntry();
  lowerKey();
  lowerValue();
  floorEntry();
  floorKey();
  ceilingEntry();
  ceilingKey();
  higherEntry();
  higherKey();
  firstEntry();
  lastEntry();
  pollFirstEntry();
  pollLastEntry();
  descendingMap();
  navigableKeySet();
  descendingKeySet();
  subMap();
  headMap();
  tailMap();
  ```
  
  15. final class `java.util.TreeMap extends java.util.AbstractMap implements java.util.NavigableMap, Cloneable, Serializable`, it's Sorted map. implements by Red-black tree. 红黑树的实现和算法导论描述的一模一样，卧槽，以前写的什么狗屁代码。
  16. interface `java.util.Set extends java.util.Collection`
  17. interface `java.util.SortedSet extends java.util.Set`
  18. interface `java.util.NavigableSet extends java.util.SortedMap`
  19. abstract class `java.util.AbstractSet extends java.util.AbstractCollection`
  20. final class `java.util.TreeSet extends java.util.AbstractSet implements java.util.NavigableSet, Cloneable, Serializable`, TreeSet和TreeMap对比：TreeSet集成自AbstractSet,AbstractSet又继承自Collection,所以TreeSet是一个Collection,而TreeMap->NavigableMap->AbstractMap->Map，所以TreeMap是一个Map而不是Collection；TreeSet内部数据结构为NavigableMap，而不是implements Map 接口，对TreeSet的操作都是调用内部数据NavigableMap的调用，而TreeMap内部是一颗红黑树。
  21. final class `java.util.Vector extends java.util.AbstractList implements java.util.List, RandomAccess, Cloneable, Serializable`, vector和ArrayList区别：1.Vector是线程安全的，但是线程同步代价大，ArrayList不是线程安全的，一般情况下用ArrayList，2.Vector在空间不足是扩容策略：有一个capacityIncrement参数控制，ArrayList每次扩容为当前大小的1.5倍。
  22. interface `java.util.Queue extends java.util.Collection`, FIFO, methods:
  ``` java
  add();
  offer(); // same as add, but not throw exception when capacity is not enough
  remove();
  poll(); // get and remove first element
  element(); // get but not remove first element
  peek(); // get but not remove first element, return null instead of throw NoSuchElementException(element)
  ```
  23. interface `java.util.Deque extends java.util.Queue`, methods:
  ``` java
  addFirst();
  addLast();
  offerFirst();
  offerLast();
  removeFirst();
  removeLast();
  pollFirst();
  pollLast();
  getFirst();
  getLast();
  peekFirst();
  peekLast();
  removeFirstOccurrence();
  removeLastOccurrence();
  push(); // Stack methods? why deque has Stack methods?
  pop();
  remove(); // collection methods
  contains();
  size();
  iterator();
  descendingIterator();
  ```

  24. abstract class `java.util.AbstractSequentialList extends java.util.AbstractList`, can not random access but sequential access, like LinkedList.
  25. final class `java.util.LinkedList extends java.util.AbstractSequentialList implements List, Deque, Cloneable, Serializable`.
  26. final class `java.util.PriorityQueue extends java.util.AbstractQueue implements Serializable`, it's a heap.
  27. final class `java.util.HashSet extends java.util.AbstractSet implements Set, Cloneable, Serializable`
  28. final class `java.util.LinkedHashSet extends HashSet, implements Set, Cloneable, Serializable`











