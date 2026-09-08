# Reverse pin load in the `k=11` Type-II two-component branch

## 1. Result

Assume a hypothetical zero-free universal word of length `465` is in the
Type-II branch with two rank-at-most-four components.  Orient them as in the
audited component theorem:

```text
C1 = the slack-one component,
C2 = the slack-two component.
```

Let `n2=|C2|`, let `z` be the number of distinct literal rank-five entries,
and let `y2` be the number of selected rank-five witnesses of physical
length three.  In this branch every such length-three witness lies in `C2`.

For a coordinate `b`, put

```text
o2(b) = #{i in C2 : b in A[i]}.
```

If `b` is absent from the slack-one component, then

```text
3 o2(b) >= 176,                                      (1.1)
n2 + o2(b) >= 177,                                   (1.2)
3 o2(b) + z + y2 >= 386,                             (1.3)
n2 + o2(b) + z + y2 >= 387.                          (1.4)
```

In particular, the small pointwise consequence is

```text
boxed: b notin OR(C1)  =>  o2(b) >= 59.               (1.5)
```

The genuinely joint strengthening is

```text
boxed: b notin OR(C1)
       => o2(b) >= max(59,ceil((386-z-y2)/3)).         (1.6)
```

Unlike the existing `D2` localization, this applies when the slack-two
component is coordinate-complete and the slack-one component is the one
with a coordinate deficit.  Thus it controls precisely the orientation left
open by `K11_TWO_COMPONENT_PIN_LOCALIZATION.md`.

The row is coordinate-sensitive: it counts occurrences of the *same named
coordinate* in the *named slack-two component*.  It is not implied by the
component lengths, support sizes, entry-rank totals, or selected-width
profiles.

## 2. Exact setup

The Type-II two-component theorem supplies the following globally WLOG
canonical witness choice.

* Every entry has rank at most five.
* The `z` literal rank-five entries are distinct and are selected as
  singleton rank-five witnesses.
* Deleting them leaves `C1,C2` with slacks one and two.
* Every internal adjacent pair of `C1` is a different selected rank-five
  witness.
* Every selected nonliteral rank-five witness in `C2` has physical length at
  most three.
* At least one of `OR(C1),OR(C2)` is `[11]`.

Write

```text
D1=[11]\OR(C1).
```

If `b in D1`, the coordinate-complete component is necessarily `C2`.

There are exactly

```text
sum_(s=1)^4 C(10,s-1) = 1+10+45+120 = 176           (2.1)
```

nonempty masks of ranks at most four containing `b`, and exactly

```text
C(10,4)=210                                          (2.2)
```

rank-five masks containing `b`.

## 3. Touched-cell theorem

For a path of length `n` with `o` marked positions, let `G2(n,o)` be the
largest possible number of singleton and adjacent-pair cells which meet a
marked position.  Then

```text
G2(n,o)=o+min(n-1,2o)=min(3o,n+o-1).                 (3.1)
```

Indeed there are `o` marked singleton cells.  Each marked position is
incident with at most two path edges, so at most `2o` adjacent pairs are
touched, and there are only `n-1` adjacent pairs in total.  Both upper bounds
are simultaneously attainable by spacing the marked positions when
`2o<=n-1` and taking a vertex cover of the path otherwise.

### Theorem 3.1

For every `b in D1`,

```text
G2(n2,o2(b)) >= 176 + max(0,210-z_b-y2),             (3.2)
```

where

```text
z_b=#{literal rank-five entries containing b}.        (3.3)
```

Consequently

```text
G2(n2,o2(b)) >= max(176,386-z-y2).                    (3.4)
```

#### Proof

Every rank-at-most-four target containing `b` has a witness wholly in a low
component.  It cannot have a witness in `C1`, because no entry of `C1`
contains `b`.  It therefore has a witness in `C2`.  The slack-two named-cell
theorem makes this witness a singleton or adjacent pair.  The 176 different
target values require 176 different physical cells, all touched by an
occurrence of `b`.

Of the 210 rank-five targets containing `b`, exactly `z_b` are among the
selected literal singleton witnesses.  Every other such target is
nonliteral and cannot have a witness in `C1`, so its selected witness lies in
`C2`.  At most `y2` of them can use length-three witnesses, because `y2` is
the total number of selected rank-five triples.  Hence at least

```text
max(0,210-z_b-y2)
```

of these rank-five targets use adjacent-pair witnesses in `C2`.

Those pair cells are distinct from one another and from the 176 lower-target
cells: one physical interval has one OR value, and the two target families
have different ranks.  They are also touched by `b`.  This proves (3.2).

Finally `z_b<=z`, so the right side of (3.2) is at least the right side of
(3.4).  QED.

Substituting (3.1) into (3.4) gives exactly the four linear inequalities
(1.1)--(1.4).  Thus the displayed quartet is not four unrelated estimates;
it is one named-coordinate touched-cell inequality.

## 4. The raw `n2+o2` row is not the main new cut

Equation (1.2) is correct, but it becomes redundant after two already valid
rank-five component facts are included.  If `b notin OR(C1)`, then all `q1`
selected rank-five values in `C1` avoid `b`, so

```text
q1<=C(10,5)=252,
n2=q2+2>=212-z.                                     (4.1)
```

The existing named-cell capacity gives

```text
q2>=95+z,
n2>=97+z.                                           (4.2)
```

Therefore

```text
n2>=max(212-z,97+z)>=155.                           (4.3)
```

Together with `o2(b)>=59`, this gives `n2+o2(b)>=214`, much stronger than
(1.2).  The useful new information is therefore the occurrence lower bound
(1.5), and especially its coupling to the already materialized `z,y2` in
(1.6), not the standalone size row proposed by the first relaxation.

## 5. Strictness against the current scalar/profile ledger

The following abstract two-component profile satisfies all current
component-size, support, named-cell, and central-width marginals:

```text
z=1,
(q1,q2)=(252,209),
(n1,n2)=(253,211),
(|OR(C1)|,|OR(C2)|)=(10,11),
y=(y0,y1,y2)=(1,364,97),
x=(x0,x1,x2,x3)=(0,4,364,94),
w7=(w0,w1,w2,w3,...)=(0,3,4,323,0,...,0),
entry ranks (a1,...,a5)=(11,45,110,298,1).            (5.1)
```

The checks are

```text
q1+q2=461=462-z,
n1+n2=464=465-z,
q1=C(10,5),
q2>=95+z,
min(n1,L4(10))+min(2n2-1,L4(11))=253+421>=561,
y2>=95+z,
y1+2y2=558>=549,
x0+x1<=y0+3,
x0+x1+x2<=y0+y1+3,
y2<=x3+3.
```

The rank-seven profile obeys all three cumulative endpoint rows and has
four-truncated moment

```text
3+2*4+3*323=980>=930.                                (5.1a)
```

The entry ranks meet every cumulative filtration row.  Their six-subcube
support moment is `20,866`; it can be distributed as 76 abstract support
counts equal to 46 and 386 equal to 45.  Thus every current six-subcube
run-credit charge is zero.  As elsewhere, this is a separation from the
current scalar ledger, not a proposed realization of all array bits.

Take the missing coordinate of `C1` to be `b`.  The current summaries permit
only 59 positions of `C2` to contain `b`: they remember that `C2` is
coordinate-complete but do not count its pin load.  This passes the raw
lower-family row (1.1) at equality, but

```text
3*59+z+y2=275<386,                                  (5.2)
```

so it violates the new joint row (1.3).  The profile is only a strictness
certificate for the relaxation, not a claimed OR word.  The complete base
CNF of course implies Theorem 3.1 semantically.

The same profile with 58 occurrences violates even (1.5), showing that the
pointwise coordinate count is itself absent from the current marginals.

## 6. Compact SAT projection

The current Type-II plan already contains exact membership flags for `C1`
and `C2`, the global literal-five count `z`, and the selected rank-five
width count `y2`.  A compact optional module needs only:

1. the eleven final coordinate-OR bits of `C1`;
2. for each `b`, exact flags
   `occ2[b,i] <-> (i in C2 and b in A[i])`;
3. eleven exact counters `o2(b)=sum_i occ2[b,i]`;
4. conditional comparisons (1.1) and (1.3) whenever the final `C1` OR omits
   `b`.

Rows (1.2) and (1.4) are mathematically exact but are not recommended for a
first implementation: (1.2) is redundant by Section 4, while in the
relevant low-`z` profiles the `3o2+z+y2` row is normally the stronger branch
of the exact minimum.

The module is globally WLOG because it uses the same canonical rank-five
witness choice already certified by the Type-II component encoding.  It
does not fix a coordinate, a component cut, or a central path.

## 7. Scope

This theorem applies only in the two-component Type-II subcase.  It does not
change the rigorous bracket for `nu(11)`, and it does not assert that the
profile (5.1) extends to an OR array.  Its purpose is to expose a distributed
coordinate consequence to the solver with eleven counters rather than a
bank of 176 target selectors per coordinate.

The companion checker is

```text
python3 scratch/check_k11_type2_reverse_pin_load.py
```

and verifies the touched-cell envelope, every constant, the redundancy
calculation, and the strictness profile.

## 8. Companion projection on the already localized side

The existing `D2` theorem is set-valued, although its production projection
currently retains only four rank totals.  If `b notin OR(C2)`, all 176 lower
targets containing `b` occur literally in `C1`.  Therefore the immediate
coordinate projection is

```text
b notin OR(C2) => #{i in C1:b in A[i]} >=176.          (8.1)
```

This is stronger than the currently encoded rank-only rows for that named
coordinate, but it is not a new theorem beyond the literal-localization law.
The genuinely new orientation is Sections 1--6: when `C2` is complete and
`C1` misses `b`, the target family is no longer literal and must instead be
paid for by the touched singleton/pair cells of `C2`.
