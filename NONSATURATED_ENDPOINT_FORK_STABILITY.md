# Nonsaturated endpoint-fork stability at rank-count equality

## 1. Scope and status

This note gives necessary structure for a word attaining the rank-count
length.  It does not assume a derivative row, a Johnson path, a prescribed
band schedule, or positive literal boundary mass.  Its main application is
the nonsaturated branch left open by boundary--core rigidity.

Everything labelled **Theorem**, **Lemma**, or **Corollary** below is proved
in the note.  Statements in the final section labelled **OPEN** are not
proved and are not used in any conclusion.

Throughout, one witness interval is selected for each target under
discussion.  Different targets of one fixed rank receive different selected
intervals.  Array positions are indexed by `1,...,n`.

## 2. The two-middle-layer endpoint fork

Let

```text
k=2m+1,
M=C(k,m)=C(k,m+1),
n=M+d.
```

Assume a zero-free word `A_1,...,A_n` covers every rank-`m` and every
rank-`(m+1)` mask.  Select one witness for every mask in each of these two
layers.

For the selected rank-`m` witnesses, let `L_m,R_m` be their sets of left and
right endpoints.  Define `L_(m+1),R_(m+1)` analogously and put

```text
L=L_m intersection L_(m+1),
R=R_m intersection R_(m+1),
C=L intersection R.
```

### Lemma 2.1 (shared endpoint count)

```text
|L|>=M-d,
|R|>=M-d,
|C|>=M-3d.                                      (2.1)
```

Negative right sides are interpreted as vacuous.

### Proof

Selected witnesses for distinct equal-rank masks form an interval
antichain.  In particular, their left endpoints are distinct and their right
endpoints are distinct.  Each of the four endpoint sets above consequently
has size `M` inside an `n=M+d` element universe.  Hence

```text
|L|>=2M-n=M-d,
|R|>=2M-n=M-d.
```

A second inclusion--exclusion in the physical position universe gives

```text
|C|>=|L|+|R|-n>=2(M-d)-(M+d)=M-3d.
```

QED.

Fix `p in C`.  There are four selected witnesses incident with `p`:

```text
I_p^+ : rank m,   left endpoint p,
J_p^+ : rank m+1, left endpoint p,
I_p^- : rank m,   right endpoint p,
J_p^- : rank m+1, right endpoint p.
```

### Lemma 2.2 (nesting and the mixed-case exclusion)

One has

```text
I_p^+ proper-subset J_p^+,
I_p^- proper-subset J_p^-                         (2.2)
```

as physical intervals.  Moreover, exactly one of the following holds.

1. `I_p^-=I_p^+=[p,p]`.  Its label is the rank-`m` entry `A_p`.
2. Both `I_p^-` and `I_p^+` are nonsingletons.  They are different selected
   witnesses for different rank-`m` masks, meet physically only at `p`, and

   ```text
   A_p subseteq U(I_p^-) intersection U(I_p^+),
   |A_p|<=m-1.                                   (2.3)
   ```

It is impossible for exactly one of `I_p^-`,`I_p^+` to be a singleton.

### Proof

At a common left endpoint the two intervals are nested.  If the
rank-`(m+1)` interval were contained in the rank-`m` interval, its OR label
would be a rank-`(m+1)` subset of a rank-`m` set, impossible.  Thus the
rank-`m` interval is a proper prefix of the rank-`(m+1)` interval.  The same
argument at a common right endpoint gives the proper-suffix statement.

Suppose, for example, `I_p^-=[p,p]` while `I_p^+` is not a singleton.  Then

```text
U(I_p^-)=A_p subseteq U(I_p^+).
```

Both sets have rank `m`, so they are equal.  This would put two different
physical intervals with the same label into a family in which exactly one
witness was selected for each rank-`m` mask.  That is impossible.  The
opposite mixed case is symmetric.

If both are nonsingletons, one extends strictly left from `p` and the other
strictly right, so their physical intersection is `{p}`.  They cannot have
the same label for the same one-witness-per-mask reason.  Distinct `m`-sets
have intersection rank at most `m-1`, and `A_p` is contained in both ORs.
This proves (2.3).  QED.

Call a position in case 2 a **double-fork centre**.  Write `F` for the set of
double-fork centres.

### Theorem 2.3 (double-fork stability)

Let `z_m` be the number of physical entries of rank exactly `m`.  Then

```text
|F|>=M-3d-z_m.                                    (2.4)
```

Now additionally suppose every entry has rank at most `m+1`.  Put

```text
p=number of entries of rank at most m-1,
h=number of entries of rank m+1.
```

Then

```text
|F|>=p+h-4d,                                      (2.5)
p-|F|<=4d-h.                                      (2.6)
```

Thus all but at most `4d-h` of the entire rank-at-most-`m-1` position set
are double-fork centres.

### Proof

By Lemma 2.2, every point of `C` which is not a double-fork centre is a
position carrying a rank-`m` entry.  There are at most `z_m` such positions.
Combine this with (2.1) to obtain (2.4).

Under the rank cap,

```text
n=p+z_m+h,
M=n-d.
```

Substitution into (2.4) gives

```text
|F|>=n-d-3d-z_m=p+h-4d.
```

Since every double-fork centre has entry rank at most `m-1`, `F` is a subset
of the `p` low positions, and rearrangement gives (2.6).  QED.

### Theorem 2.4 (the fork path forest)

Make one vertex for each selected rank-`m` witness.  For every `p in F`, add
a directed edge

```text
I_p^-  -->  I_p^+.
```

This is a directed linear forest on the `M` selected rank-`m` masks.  It has
`|F|` edges and exactly `M-|F|` path components after isolated vertices are
included.  The physical entry at an edge junction is contained in the
intersection of its two distinct endpoint masks.

### Proof

A selected interval can be `I_p^+` only at its unique left endpoint and can
be `I_q^-` only at its unique right endpoint.  Hence indegree and outdegree
are at most one.  Along a directed edge the junction is the right endpoint
of the first nonsingleton interval and the left endpoint of the second.  On
following another edge, the physical junction strictly moves to the right.
Directed cycles are therefore impossible.  Lemma 2.2 supplies the label and
intersection statement.  QED.

## 3. Rank and coordinate incidence inherited by the fork fabric

Suppose now that the word is universal, has exact length `B(k)=M+d`, and the
upper middle rank `m+1` attains this bound.  Exact rank truncation gives the
rank cap required in Theorem 2.3.

For integers `s<=ell`, put

```text
beta_s(ell)=max_(1<=t<=s) [C(ell,t)+tau(ell,t)].
```

For an `ell`-set `Y subseteq [k]`, define

```text
P_s(Y)={i: A_i subseteq Y and |A_i|<=s},
F_s(Y)=F intersection P_s(Y).
```

### Lemma 3.1 (pointwise coordinate restriction)

For every `s<=ell`,

```text
|P_s(Y)|>=beta_s(ell).                              (3.1)
```

### Proof

Delete every entry not belonging to `P_s(Y)`.  If a target `T subseteq Y`
has rank at most `s`, every entry of any original witness for `T` is a
nonempty subset of `T`; hence no position of that witness is deleted.  The
retained word still covers the complete punctured ideal through rank `s` on
the coordinate set `Y`.  Applying the rank-count bound separately at every
rank at most `s` proves (3.1).  QED.

### Theorem 3.2 (fork-filtration incidence)

For every `1<=s<=min(m-1,ell)`,

```text
|F_s(Y)|>=beta_s(ell)-(4d-h).                       (3.2)
```

In particular, with `Y=[k]`,

```text
#{i in F: |A_i|<=s}>=beta_s(k)-4d+h.               (3.3)
```

Summing (3.2) over all `ell`-sets gives the rank-resolved incidence family

```text
sum_(i in F, |A_i|<=s)
    C(k-|A_i|,ell-|A_i|)
 >= C(k,ell) [beta_s(ell)-4d+h]_+.                 (3.4)
```

### Proof

The exceptional set of low positions `(rank<=m-1) minus F` has size at most
`4d-h` by (2.6).  Since `P_s(Y)` is a subset of the low positions, at most
that many of its members can fail to be forks.  Combine with (3.1).  Equation
(3.4) is the double count of pairs `(i,Y)` with `A_i subseteq Y`.  QED.

This is coordinate-sensitive stability, not merely a rank histogram: every
coordinate restriction contains almost its full rank-count quota inside the
same touching-interval path forest.

### Theorem 3.3 (upper incidence from forest acyclicity)

For every `1<=q<=m-1`, the same fork centres satisfy

```text
sum_(i in F) C(|A_i|,q)
 <= C(k,q) [C(k-q,m-q)-1].                         (3.5)
```

More pointwise, for each fixed `q`-set `Q`,

```text
#{i in F: Q subseteq A_i}
 <= C(k-q,m-q)-1.                                  (3.6)
```

### Proof

If `Q subseteq A_i` at a fork edge, then `Q` is contained in both endpoint
rank-`m` masks by (2.3).  In the fork path forest, restrict to the
`C(k-q,m-q)` vertices whose masks contain `Q`.  The counted fork edges form a
subgraph of this induced forest, so there are at most one fewer edges than
vertices.  This proves (3.6).  Summing over all `Q` counts each centre
`C(|A_i|,q)` times and gives (3.5).  QED.

## 4. The special width-three overlap law

Assume `d=3`.  At a double-fork centre the two selected rank-`m` witnesses
have physical lengths in `{2,3}`: they are nonsingletons, and each is a
proper same-endpoint subinterval of a rank-`(m+1)` witness of length at most
four.  Write their lengths as

```text
lambda_p^- , lambda_p^+ in {2,3}.
```

### Theorem 4.1 (forbidden mixed overlap)

If `p<q` are double-fork centres and `q-p` is one or two, then

```text
lambda_p^+ = lambda_q^-.                           (4.1)
```

### Proof

For `q=p+1`, the facing intervals are

```text
[p,p+lambda_p^+-1],
[q-lambda_q^-+1,q].
```

If their lengths are `(2,3)` or `(3,2)`, the shorter interval is properly
contained in the longer.  This is impossible for two selected witnesses of
distinct equal-rank masks.  Equal length two makes them the same physical
interval; equal length three makes them overlap without containment.

For `q=p+2`, the same inspection shows that mixed lengths again give proper
containment.  Equal length three gives the same physical interval, while
equal length two gives two noncontaining intervals meeting in one position.
Thus only equal facing lengths are possible in both cases.  QED.

### Corollary 4.2 (three consecutive forks are homogeneous in the middle)

If `p,p+1,p+2` are all double-fork centres, then

```text
lambda_p^+
 =lambda_(p+1)^-
 =lambda_(p+1)^+
 =lambda_(p+2)^-.                                  (4.2)
```

In particular the middle centre has type `(2,2)` or `(3,3)`.

### Proof

Apply Theorem 4.1 to the three pairs at distances one, one, and two.  QED.

Let

```text
sigma=3M+6-sum_(j=1)^m C(2m+1,j)
     =3M+7-2^(2m).                                  (4.3)
```

This is the short-band residual at active rank `m+1`.

### Theorem 4.3 (short-fork defect charge)

The number of type-`(2,2)` double-fork centres is at most `sigma`.
Consequently at least

```text
[|F|-sigma]_+                                      (4.4)
```

fork centres have a length-three rank-`m` witness on at least one side.

If `T_3(F)` denotes the number of three-consecutive-position windows all of
whose positions belong to `F`, then

```text
T_3(F)>= [3|F|-2n-2]_+,                            (4.5)
```

and at least

```text
[3|F|-2n-2-sigma]_+                                (4.6)
```

centres are interiors of three-fork runs and have type `(3,3)`.

### Proof

At a type-`(2,2)` centre `p`, the two selected rank-`m` pair witnesses are
`[p-1,p]` and `[p,p+1]`.  Their labels are distinct `m`-sets, so the OR of
the centered triple `[p-1,p+1]` has rank at least `m+1`.  Distinct centres
give distinct physical triple cells.

Every mask below rank `m+1` has a witness of length at most three.  The band
of all cells of lengths one, two, and three has `3M+6` cells, while the
number of nonempty masks below rank `m+1` is `2^(2m)-1`.  After one cell is
selected for each such lower mask, exactly `sigma` cells remain.  Every
rank-at-least-`m+1` triple is among those remaining cells.  Hence there are
at most `sigma` type-`(2,2)` centres, proving (4.4).

If `F` has `g` runs in the physical path, then

```text
T_3(F)=sum_runs [length-2]_+ >= |F|-2g.
```

There are at most `n-|F|+1` nonempty runs, so

```text
T_3(F)>=|F|-2(n-|F|+1)=3|F|-2n-2,
```

with the positive part added when the right side is negative.  Corollary
4.2 makes the middle of every such triple type `(2,2)` or `(3,3)`.  Different
three-position windows have different middle positions, and at most `sigma`
of those positions can be type `(2,2)`.  This proves (4.6).  QED.

### Theorem 4.4 (forced graded Johnson segments)

Let `a,a+1,...,a+t-1` be a run of consecutive double-fork centres, with
`t>=3`.  There is one value

```text
epsilon in {2,3}
```

such that

```text
lambda_i^+=epsilon       (a<=i<=a+t-2),
lambda_i^-=epsilon       (a+1<=i<=a+t-1).           (4.7)
```

If `epsilon=3`, put

```text
T_i=U([i,i+2])           (a<=i<=a+t-2),
Q_i=U([i,i+3])           (a<=i<=a+t-3).
```

Then the `T_i` are distinct selected rank-`m` masks, the `Q_i` are distinct
selected rank-`(m+1)` masks, and

```text
Q_i=T_i union T_(i+1),
|T_i intersection T_(i+1)|=m-1.                   (4.8)
```

Thus the run contains a genuine Johnson path segment through rank `m`, with
rainbow rank-`(m+1)` union colours.  Summed over all fork runs, the number of
forced Johnson edges of this form is at least the quantity in (4.6).

### Proof

For consecutive centres, Theorem 4.1 gives

```text
lambda_i^+=lambda_(i+1)^-.
```

For centres two apart it gives

```text
lambda_i^+=lambda_(i+2)^-.
```

Combining these equalities down the run proves (4.7); only the unused
outermost values `lambda_a^-` and `lambda_(a+t-1)^+` can differ.

Suppose the common value is three.  The outgoing lower witness at `i` is
then exactly `[i,i+2]`.  Its same-left-endpoint upper witness is a proper
superinterval and has length at most four, so it is exactly `[i,i+3]`.
This proves that the displayed `T_i,Q_i` are selected witnesses in the stated
ranks.  Selected witnesses within one rank have distinct labels.

The interval `[i,i+3]` is the union of the overlapping intervals
`[i,i+2]` and `[i+1,i+3]`, whence `Q_i=T_i union T_(i+1)`.  Two distinct
rank-`m` subsets of the rank-`(m+1)` set `Q_i` are different facets, so their
intersection has rank `m-1`.  A run of length `t` contributes exactly `t-2`
such edges.  The proof of (4.6) says that, after at most `sigma` type-`(2,2)`
run interiors are discarded, at least its displayed number of run interiors
have common value three.  QED.

## 5. Exact odd-dimensional consequences below twenty

For `k=11,13,15,17,19`, the conjectural equality length is `n=M+3` and
boundary--core rigidity gives `h<=1`.  The nonsaturated branch has `h=0`.
Theorem 2.3 says that at most `12-h` positions of rank at most `m-1` fail to
be double-fork centres.

Using only the rank-count records at rank `m-1`, every equality candidate has
at least the following number of double-fork centres:

| `k` | `m` | `beta_(m-1)(k)` | forced double forks |
|---:|---:|---:|---:|
| 11 | 5 | 331 | at least `319+h` |
| 13 | 6 | 1288 | at least `1276+h` |
| 15 | 7 | 5006 | at least `4994+h` |
| 17 | 8 | 19450 | at least `19438+h` |
| 19 | 9 | 75584 | at least `75572+h` |

For `k=11`, (3.3) additionally forces, in the nonsaturated branch, at least

```text
44  double-fork centres whose entry has rank at most 2,
154 double-fork centres whose entry has rank at most 3,
319 double-fork centres whose entry has rank at most 4.
```

The corresponding numbers improve by one in the `h=1` branch.  They use the
rank-count records `beta_2(11)=56`, `beta_3(11)=166`, and
`beta_4(11)=331`; no certificate or search evidence enters them.

The pointwise version (3.2) is stronger than these global counts.  Still at
`k=11`, every ten-coordinate set `Y` contains at least `199+h` fork centres
whose entries are rank-at-most-four subsets of `Y`; every nine-, eight-, and
seven-coordinate set contains respectively at least

```text
116+h, 60+h, 25+h
```

such centres.  Here the inputs are

```text
beta_4(10)=211,
beta_4(9)=128,
beta_4(8)=72,
beta_4(7)=37.
```

Equivalently, the fork-centre entry ranks obey the coordinate-incidence cuts

```text
sum_(i in F) (11-|A_i|)             >= 2189+11h,
sum_(i in F) C(11-|A_i|,2)          >= 6380+55h,
sum_(i in F) C(11-|A_i|,3)          >= 9900+165h,
sum_(i in F) C(11-|A_i|,4)          >= 8250+330h.   (5.1)
```

The first says, in particular, that at least `199+h` fork centres omit each
prescribed coordinate.  These are direct theorem consequences, not a claim
that the resulting integer system is infeasible.

The width-three residuals from (4.3) are

| `k` | `sigma` | forks forced to have a length-three side |
|---:|---:|---:|
| 11 | 369 | no positive consequence from (4.4) |
| 13 | 1059 | at least `217+h` |
| 15 | 2928 | at least `2066+h` |
| 17 | 7401 | at least `12037+h` |
| 19 | 14997 | at least `60575+h` |

Using (4.6) gives at least `2285+3h` type-`(3,3)` run-interior centres at
`k=17` and at least `26955+3h` at `k=19`; the same scalar consequence is
zero at `k=11,13,15`.

These are necessary stability statements.  They do not prove or disprove
equality.

## 6. Full critical flags and the `k=14` double-diamond theorem

The next lemma works without oddness.  Fix consecutive ranks

```text
a=r-d, a+1,...,r
```

in a word of length

```text
n=C(k,r)+d.
```

Select one witness for every mask in every displayed rank.  Put

```text
M_j=C(k,j),
Lambda=sum_(j=a)^r M_j-d*n.                        (6.1)
```

### Theorem 6.1 (two-sided critical flags)

There are at least `Lambda` common left endpoints and at least `Lambda`
common right endpoints for all `d+1` selected layers.  At every such endpoint
the selected intervals have physical lengths exactly

```text
1,2,...,d+1
```

in increasing rank order.  In particular, the rank-`a` witness is a
singleton.

At least

```text
[2*Lambda-M_a]_+                                   (6.2)
```

positions support both a left-growing and a right-growing full flag.

### Proof

The left endpoint set of rank `j` has size `M_j` in an `n`-position universe.
The complement union bound gives

```text
|intersection_(j=a)^r L_j|
 >= n-sum_(j=a)^r(n-M_j)
  = sum_(j=a)^r M_j-d*n
  = Lambda.
```

The right side is identical.  At a common endpoint the intervals are strictly
nested in increasing rank order.  The largest, rank-`r` interval has length
at most `n-M_r+1=d+1` by the equal-rank interval-slack lemma.  There are
`d+1` distinct positive integer lengths, so they are exactly `1,...,d+1`.

Both the left-flag and right-flag endpoint sets are subsets of the physical
singleton witnesses selected for the `M_a` rank-`a` masks.  Inclusion--
exclusion inside this common set of at most `M_a` singleton witnesses gives
(6.2).  QED.

### Corollary 6.2 (`k=14` exact double diamonds)

If a universal 14-coordinate word has length `B(14)=3434`, choose witnesses
in ranks five, six, and seven.  Then

```text
Lambda=C(14,5)+C(14,6)+C(14,7)-2*3434
      =2002+3003+3432-6868
      =1569.
```

Therefore at least

```text
2*1569-2002=1136                                  (6.3)
```

positions support two-sided exact flags

```text
rank 5 singleton  -> rank 6 pair -> rank 7 triple
```

in both physical directions.

At each such centre `p`, write `S=A_p`.  The selected pair ORs are

```text
U([p-1,p])=S union {x},
U([p,p+1])=S union {y}
```

with `x!=y`.  Consequently the centered triple satisfies

```text
U([p-1,p+1])=S union {x,y},
|U([p-1,p+1])|=7.                                 (6.4)
```

Thus every equality word contains at least 1136 exact local rank-`5/6/7`
double diamonds.  Their rank-five base masks are distinct.

### Proof

Only (6.4) remains.  Each pair contains the selected rank-five singleton and
has rank six, so it adds one coordinate.  The two pair labels are different:
otherwise the fixed selected rank-six family would contain two different
physical witnesses for the same target.  Hence the added coordinates are
different, and the OR of the centered triple has rank seven.  QED.

The bases also obey the following coordinate incidence consequence.  If
`Y subseteq [14]`, then at least

```text
[C(|Y|,5)-866]_+                                   (6.5)
```

of the 1136 double-diamond bases are contained in `Y`.  Indeed, at most
`C(14,5)-C(|Y|,5)` of all rank-five masks lie outside that subcube.  Taking
`|Y|=13` shows that at least `421` double diamonds omit each prescribed
coordinate.

If `a,a+1,...,a+t-1` is any consecutive run of these double-diamond
centres, then their distinct rank-five bases `S_i=A_i` satisfy

```text
B_i=S_i union S_(i+1)=U([i,i+1])       (a<=i<a+t-1),
Q_i=B_i union B_(i+1)=U([i,i+2])       (a<=i<a+t-2).
```

The `B_i` are distinct selected rank-six masks, the `Q_i` are distinct
selected rank-seven masks, and consecutive bases are Johnson adjacent.
Thus every such run is a fully graded rank-`5/6/7` path segment.  This is an
exact implication, but the count `1136` alone does not force two centres to
be adjacent in a path of length `3434`.

For the odd `d=3` cases, Theorem 6.1 applied to ranks
`m-2,m-1,m,m+1` also forces two-sided full four-rank flags.  Formula (6.2)
is positive from `k=15` onward and gives respectively

```text
k=15:   125,
k=17:  2634,
k=19: 16778
```

centres with exact ranks `m-2,m-1,m,m+1` at physical lengths
`1,2,3,4` in both directions.

## 7. Audit and exact remaining gap

The proofs use only the following established inputs.

1. Selected intervals for distinct equal-rank masks are noncontaining and
   therefore have distinct left and right endpoints.
2. A rank layer of size `M` selected in length `M+d` has witness length at
   most `d+1`.
3. Exact rank truncation at an attaining rank bounds every entry by that rank.
4. The rank-count theorem applies after coordinate restriction.

No conclusion assumes that adjacent selected masks are Johnson adjacent.
In particular, at a generic double-fork centre the intersection of its two
rank-`m` labels can be larger than the physical entry, and can have any rank
from `|A_p|` through `m-1`.

No conclusion assumes that the fork forest covers lower masks, that its hulls
cover upper masks, or that an abstract fork forest is factorable by one OR
word.  Those converses are unproved.

The following are the exact live next steps.

* **OPEN (dense-fork collision lemma).**  Show that a width-three word in
  which all but twelve low positions are fork junctions must spend more than
  `sigma` short-band defects, or else loses a required lower target.
* **OPEN (fork-factor construction).**  Construct a path forest satisfying
  (3.2)--(4.2), factor it into entries, and prove that its short cells cover
  the lower ideal while its hulls cover all upper ranks.  This would be a
  genuinely nonsaturated route toward `nu(k)=B(k)`.
* **OPEN (`k=14` diamond collision).**  Prove that 1136 exact double diamonds
  force too many repeated rank-seven triple values or incompatible coordinate
  pins.  Corollary 6.2 alone does not provide such a collision bound.

Accordingly this note strengthens the equality normal form but changes no
certified value or lower endpoint by itself.
