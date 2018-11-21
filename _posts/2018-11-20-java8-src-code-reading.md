---
layout: post
categories: Programming
tags: Programming
title: "Java 8 source code reading"
description: Collection
---

### java 8 source code

## ref to [java8 src code reading](https://www.cnblogs.com/joemsu/p/7667509.html)

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






