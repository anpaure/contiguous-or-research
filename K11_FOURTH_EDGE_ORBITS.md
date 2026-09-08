# Exact fourth-edge orbit split for the factorable `k=11` search

## 1. Prefix notation

Retain the canonical masks

```text
C=31, E=63, F=119,
```

one of the four second-edge representatives `G`, and one of the fifteen
third-edge representatives `H` certified in
`K11_THIRD_EDGE_ORBITS.md`.  We classify the next central vertex `I` under
the stabilizer of the complete fixed prefix `C,E,F,G,H`.

The result is 60 exhaustive fourth-edge branches:

| second `q` | third `t` | `H` | fourth-orbit representatives `I` |
|---:|---:|---:|---|
|0|0|125|`221, 95, 237, 111`|
|0|1|252|`476, 221, 222, 492, 237, 238`|
|0|2|95|`207, 111`|
|0|3|222|`462, 238, 207`|
|1|0|245|`469, 221, 215, 485, 237, 231`|
|1|1|252|`476, 221, 222, 492, 237, 238`|
|1|2|500|`980, 476, 469, 470, 996, 492, 485, 486`|
|1|3|215|`455, 231, 207`|
|1|4|222|`462, 238, 207`|
|1|5|470|`966, 486, 462, 455`|
|2|0|126|`238, 111`|
|2|1|222|`462, 238, 207`|
|3|0|222|`462, 238, 207`|
|3|1|246|`486, 238, 231`|
|3|2|470|`966, 486, 462, 455`|

## 2. Why exactly fifteen labelled transitions survive per prefix

Write the first three Johnson transitions as

```text
E -> F : remove x1, add y1=6,
F -> G : remove x2, add y2,
G -> H : remove x3, add y3.
```

The already certified prefix guarantees that `y1,y2,y3` are distinct and
all belong to `H`.

Consider `H -> I = H-{x4}+{y4}`.  The removal `x4` cannot be:

* `y1`: its coordinate word would contain `0,1,1,1,0`, an internal
  one-run of length three;
* `y2`: it was absent at `F`, so its completed run through `G,H` would have
  length two; or
* `y3`: its completed run would have length one.  Equivalently, this last
  choice repeats the lower colour of `G -> H`.

All three violate delay-three factorability.  There are six coordinates in
`H`, so three removal coordinates remain.  For each, there are five possible
addition coordinates outside `H`, giving exactly fifteen labelled candidates.

Direct checking shows that none of these candidates repeats `E,F,G,H` or an
earlier lower colour.  This last finite statement is also independently
enumerated rather than assumed in the audit checker.

## 3. Orbit completeness

For a coordinate `b`, define its prefix membership signature

\[
 \sigma(b)=(1_{b\in C},1_{b\in E},1_{b\in F},
             1_{b\in G},1_{b\in H}).
\]

The stabilizer of `C,E,F,G,H` is exactly the direct product of symmetric
groups on equal-signature coordinate classes.  A fourth transition is
therefore classified by the ordered pair

```text
(signature(x4), signature(y4)).
```

It is transitive on all transitions with one such pair, because the removed
and added coordinates lie in disjoint inside/outside classes.  Different
signature pairs cannot be related.  Enumerating the fifteen legal labelled
transitions for each certified `(q,t)` prefix and retaining one representative
of every signature pair yields exactly the displayed table.  The row counts
sum to

```text
15 + 30 + 5 + 10 = 60.
```

Thus the table is complete and irredundant modulo the residual stabilizer.

## 4. SAT interface

The source accepts the nested settings

```text
RECOMBINE_SECOND_ORBIT=q
RECOMBINE_THIRD_ORBIT=t
RECOMBINE_FOURTH_ORBIT=u
```

and fixes the directed arc `H -> I` to the corresponding table entry.  The
fourth option is rejected unless all preceding orbit settings exist and the
search uses the complete ordered `J(11,6)` graph with delay three and WLOG
canonicalization active, and actually enforces factorability either up front
or through the exact lazy run loop.  Pure shadow/base relaxations are rejected
because the cooldown exclusions would not be valid for their larger feasible
sets.

Running all 60 triples `(q,t,u)` is exhaustive only for the factorable fixed
central-row ansatz.  It does not restrict or decide the unrestricted
monotone-band problem.
