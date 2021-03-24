print("-----------Set----------")
s1={1,2,3,4,5,6}
s2={1,2,3}
 
print("Original set", s1)
s1.add(8)
print("Add 8 in set", s1)
s1.remove(8)
print("Remove 8 in set", s1)
s1.pop()
print("Pop element default 1st element in set", s1)
print("Length set", len(s1))
 
s1.update([8,9])
print("updated 8,9 in set",s1)
 
s1.discard(3)
print("discard 3",s1)
s1={1,2,3,4,5,6}
s2={1,2,3,9}
print("Reinitialize s1 ::",s1)
print("initialize s2 ::",s2)
print("s2 subset of s1 ::",s2.issubset(s1))
print("s2 superset of s1 ::",s2.issuperset(s1))
print("s1 Union s2 ::",s1.union(s2))
print("s1 Intersection s2 ::",s1.intersection(s2))
print("s1 diffrence s2 ::",s1-s2)
print("s1 Symmetric diffrence s2 ::",s1^s2)
 
s3=s2.copy()
print("Copy s3 as s2",s3)
print("Length of s3::",len(s3))
print("Min of s3::",min(s3))
print("Max of s3::",max(s3))
print("Sum of s3::",sum(s3))
print("Sorted of s3::",sorted(s3))
