# Dimension-changing maps for universal contiguous-OR words

This note isolates what can and cannot be inherited when the dimension is
changed.  Throughout, `nu(k)` is the minimum length for the nonzero problem,
and a word is a sequence of nonempty subsets whose consecutive unions contain
every nonempty subset of the ground set.

## 1. Quotients preserve coverage, but almost never shorten the word

**Join-quotient lemma.**  Let

```
phi : 2^X -> 2^Y
```

be a surjective map satisfying `phi(U union V)=phi(U) union phi(V)` and
`phi(empty)=empty`.  If `A` is universal on `X`, then the word obtained from
`phi(A)` by deleting zero terms is universal on `Y`.  Consecutive equal terms
may also be run-compressed.

The proof is immediate: apply `phi` to a witnessing interval.  Its nonzero
terms remain consecutive after all zero terms are removed, and have the same
union.  Run-compression is safe because replacing a nonempty constant run by
one copy does not change any interval union.

There is a sharp reason this does not halve a word when one coordinate is
removed.  A join map is determined by the images of the atoms.  If
`|X|=|Y|+1` and `phi` is onto, then for every `y in Y` some atom of `X` must
map to the singleton `{y}`.  These atoms are distinct.  Hence at most one
source atom can lie in the kernel.  A nonempty mask maps to zero only when it
is the singleton consisting of that one kernel atom.  Consequently an
entrywise quotient from `k` to `k-1` can automatically delete only occurrences
of one singleton.  Coordinate identification has empty kernel and deletes no
term at all.

Thus projection is a coverage theorem, not a length-halving theorem.

## 2. Restriction is stronger than projection

For `Y subseteq X`, let `A|Y` be the subsequence consisting of those entries
of `A` which are entirely contained in `Y`.

**Restriction lemma.**  `A|Y` is universal on `Y`.

Indeed, a witness for `S subseteq Y` cannot contain an entry using a coordinate
outside `Y`.  The whole witness therefore survives in `A|Y`, and its terms are
still consecutive there.

This gives useful exact counting inequalities.  If `a_s` is the number of
entries of cardinality `s` in a universal `k`-word of length `n`, then for
every `ell <= k`, double counting pairs `(entry,Y)` gives

```
sum_s a_s binom(k-s,ell-s) >= binom(k,ell) nu(ell).       (R)
```

Here a binomial coefficient is zero when its lower argument is invalid.
Likewise, projecting every entry to `Y`, rather than filtering it, gives

```
sum_s a_s binom(k-s,ell)
    <= binom(k,ell) (n-nu(ell)).                          (Q)
```

For `ell=k-1`, (R) becomes

```
sum_i |A_i| <= k (n-nu(k-1)).                            (1)
```

More individually, if `f_b` is the number of entries containing coordinate
`b`, then

```
f_b <= n-nu(k-1)                                        (2)
```

because deleting all entries containing `b` leaves a universal `(k-1)`-word.
Since every coordinate occurs, this also proves the weak but unconditional
strict monotonicity

```
nu(k) >= nu(k-1)+1.
```

The inequalities (R) and (Q), for all `ell`, are a potentially useful new
linear-programming relaxation on the rank distribution of an optimal word.

## 3. Exact normal form for adding one coordinate

Let `z` be a new coordinate.  Write an arbitrary word on `X union {z}` uniquely
as

```
Q_i = C_i union (epsilon_i ? {z} : empty),
```

where `C_i subseteq X` and `epsilon_i` is zero or one.

**Two-colour extension lemma.**  `Q` is universal on `X union {z}` if and only
if both conditions below hold.

1. For every nonempty `S subseteq X`, some interval has `C`-union `S` and all
   its epsilon labels are zero.
2. For every `S subseteq X`, including `S=empty`, some interval has `C`-union
   `S` and contains at least one epsilon-one position.

The two conditions are exactly the witnesses for `S` and `{z} union S`.
In particular, the zero-labelled subsequence is itself universal on `X`, and
some epsilon-one term has old part empty (the literal singleton `{z}`).

This is an exact formulation of dimension lifting.  It shows what an optimal
lift must do: the clean and marked witnesses must be heavily interleaved and
must reuse endpoint chains.  Merely making a second transformed copy is only
one very special solution of this two-colour problem.

### A sharp obstruction to one-interface lifts

Suppose all zero-labelled entries precede all one-labelled entries, or vice
versa.  The clean block has length at least `nu(k)`.  For the `W(k)` middle
sets `S`, witnesses of `{z} union S` need distinct endpoints in the marked
block: interval unions with one fixed endpoint form a chain and hence contain
at most one member of that antichain.  Therefore every one-interface lift has

```
length >= nu(k)+W(k).                                   (3)
```

Numerically this gives

```
k=10 -> 11:  at least 254+252 = 506, not the target 465;
k=11 -> 12:  at least 465+462 = 927, not the target 926;
k=12 -> 13:  at least 926+924 = 1850, not the target 1719.
```

Thus a recursion compatible with `B(k)` must be genuinely multi-interface.
This is not a matter of optimizing the standard doubled word.

The usual trimmed lift is the special construction

```
A || {z} || ({z} union A_1),...,({z} union A_(n-1)),
```

and proves `nu(k+1)<=2nu(k)`.  More generally, if `rho_R(A)` is the least `m`
such that the interval unions of `A_1,...,A_m`, together with all suffix unions
of `A`, cover the old cube, then

```
nu(k+1) <= |A|+1+rho_R(A).
```

The middle-antichain argument gives `rho_R(A)>=W(k)-1`, another proof that
this entire single-boundary template cannot attain the conjectured odd cases.

## 4. Forced endpoint pairing in a near-width extension

Let `X` have size `2m`, and consider in dimension `2m+1` the two families

```
L={S subseteq X: |S|=m},
U={{z} union S: S in L}.
```

Choose one witness for every member of both families in a word of length `n`.
Within either family the right endpoints are distinct.  Hence the sets of
right endpoints used by `L` and `U` intersect in at least `2W(2m)-n` places.
At a common endpoint the two interval unions lie on one chain; comparability
forces the pair to be exactly `S` and `{z} union S` for the same `S`.  The same
statement holds for left endpoints.

Since

```
W(2m+1)=2W(2m)-Cat_m,
Cat_m=W(2m)/(m+1),
```

any conjecturally optimal length `W(2m+1)+d` word has at least

```
Cat_m-d                                                   (4)
```

same-mask endpoint pairings on each side.  The Catalan correction in the
odd-dimensional width is therefore exactly an endpoint-reuse requirement,
not an accidental binomial identity.

There is a little more rigidity.  At a shared right endpoint the witness for
`{z} union S` strictly contains the witness for `S` by extending it to the
left.  At a shared left endpoint it strictly contains it by extending to the
right.  The same pair `S,{z} union S` cannot share both endpoints, since then
the two witnessing intervals would be identical but have different unions.
Consequently the right-paired and left-paired masks are disjoint.  At least

```
2(Cat_m-d)
```

different middle masks therefore carry one of these two directed nesting
hooks in every length `W(2m+1)+d` extension.

This suggests searching/proving a global noncrossing or forest structure on
these forced Catalan-many paired witnesses.

## 5. Why the exact `k=12` word does not reduce to `k=11`

There are three different operations, and none gives the desired length.

1. **Entrywise coordinate erasure.**  By the join-quotient lemma it preserves
   coverage, but it deletes only literal copies of the erased singleton.
   Greedy pruning of all twelve quotients of the known 926-word reaches only
   627 at best.
2. **Literal restriction.**  Keeping entries which avoid one coordinate is
   always valid.  For the exact 926-word the twelve raw lengths are
   `671,668,675,670,673,674,672,666,661,669,664,641`; deletion pruning reaches
   583.  The exact factor has total entry weight 3108 (average 3.356), and its
   coordinate frequencies are only
   `255,258,251,256,253,252,254,260,265,257,262,285`.  No coordinate is used
   in the 461 entries that would be needed to filter directly to length 465.
3. **Restricting the central rank-six row.**  The no-coordinate section has
   the correct 462 vertices, but its induced ordering has 24 non-Johnson
   jumps, 104 forbidden coordinate runs of total delay-three deficit 163, and
   misses `3,21,34` lower shadows in ranks `3,4,5`.  Its upper shadows happen
   to be complete.

The third operation leaves 25 Johnson path components.  It can be repaired
only by reconnecting those components, restoring every internal run to length
at least four, completing the missing lower shadows, and solving the exact
delay-three pinning problem.  That is a valuable upper-complete seed, but it is
essentially the hard part of the `k=11` problem again.

The one-sided completeness is a theorem, not an experimental accident.  For
any set sequence `T` and coordinate `z`:

* the subsequence of terms avoiding `z` preserves every consecutive-union
  witness whose target avoids `z`;
* the subsequence of terms containing `z`, after erasing `z`, preserves every
  consecutive-intersection witness whose target contains `z`.

Every term of such a witness necessarily lies in the indicated section, so
this is just the restriction proof on the join and meet sides.  A two-sided
central row in dimension `k` therefore yields two complementary one-sided
seeds in dimension `k-1`: the avoiding section is upper-union complete, while
the containing section is lower-intersection complete.  For `12 -> 11`, a
plausible global repair should couple the upper-complete rank-six section to
the lower-complete rank-five section rather than repairing only one
projection.  Johnson connectivity, long runs, and the opposite shadows are
the pieces not inherited.

There is an exact way to retain both sections at once.  Let `Q_i,Q_(i+1)` be
an edge of the rank-`r` Johnson path in `X union {z}`.  Replace it after
erasing `z` as follows:

* two no-`z` rank-`r` vertices `P,P'` become
  `P, P intersection P', P'`;
* two with-`z` residual rank-`(r-1)` vertices `R,R'` become
  `R, R union R', R'`;
* a mixed edge is already an inclusion edge `R subset P`.

The result is an alternating walk in the middle-level incidence graph of
`X`, and it visits every rank-`r` and rank-`(r-1)` vertex at least once.  The
original vertices visit each exactly once; only the inserted edge colours may
repeat.  Conversely, the upper vertices of an alternating Hamilton path give
a rank-`r` Johnson path with distinct adjacent intersections.

Thus reverse dimension reduction can be stated as a clean repeat-elimination
problem: simplify this canonical spanning alternating walk to a Hamilton path
while retaining the one-sided shadows and run constraints.  This uses both
sections of the solved `k=12` object and is more faithful than discarding half
of it.

There is also an exact structural reason reverse lifting is exceptional.  If a
rank-six path in twelve dimensions is the standard odd-to-even braid in a
coordinate `z`, then the `z`-incidence word has one zero block and one one
block, each of length 462, and the projected one-block is the adjacent-
intersection row of the zero-block plus its omitted colour.  Only under those
two conditions can the odd source path be recovered.  An arbitrary optimal
even-dimensional path is not forced to have any such section-convex
coordinate; the known `k=12` path does not.

## 6. The correct parity-changing central recursions

Put `M=binom(2m,m)` and `Cat_m=M/(m+1)`.  The middle-layer sizes obey

```
W(2m+1)=M+(M-Cat_m)=2M-Cat_m,
W(2m+2)=2W(2m+1).                                      (5)
```

This identifies the correct central-row geometry.

* Even to odd cannot be a doubled middle row.  It must join all `M` sets in
  rank `m` (with the new coordinate) to all `M-Cat_m` old sets in rank `m+1`.
  The exact saving from doubling is one Catalan number.
* Odd to even really does consist of two equal sections.  This is why an
  intersection braid can double the central row without wasting a vertex.

For a Johnson path `P`, define its lower and upper edge rows

```
(nabla P)_i = P_i intersection P_(i+1),
(Delta P)_i = P_i union P_(i+1).
```

They satisfy the exact one-sided identities

```
intersection of consecutive nabla-P terms
    = intersection of the corresponding one-longer P window;
union of consecutive Delta-P terms
    = union of the corresponding one-longer P window.              (6)
```

On incidence words, `nabla` erodes every internal one-run by one, whereas
`Delta` dilates it by one (and may merge nearby runs).  Thus odd-to-even
intersection braids naturally lower the required factor delay by one, while
even-to-odd union braids naturally raise it by one.  This is the parity
mechanism that a `B(k)`-compatible recursion should exploit.

### Proved odd-to-even braid

Let `X` have size `2r-1`.  Let `P_0,...,P_(M-1)` enumerate all rank-`r` sets,
let `C_i=P_i intersection P_(i+1)` be distinct, and let `C*` be the omitted
rank-`(r-1)` set.  If `C* subseteq P_0 intersection P_(M-1)`, then

```
P_0,...,P_(M-1),
{z} union C*, {z} union C_0,...,{z} union C_(M-2)         (7)
```

is a Hamilton path through the complete rank-`r` layer in dimension `2r`.
The first lower edge colours are complete.  Its old-coordinate upper colours
are complete exactly when the adjacent unions of `P` cover rank `r+1`; its
new-coordinate upper colours are all `{z} union P_i`.  Lower shadows in the
second block are shifted intersection shadows of `P` by (6).

If all coordinate one-runs of `P`, including boundary runs, have length at
least `d+1`, then (7) satisfies the internal run condition for delay `d-1`.
Weaker endpoint hypotheses suffice, but this symmetric condition is a clean
rigorous one.

This central lift is exactly width-preserving.  It explains the successful
`11 -> 12` and `13 -> 14` strategy when the delay drops from three to two.

### Promising even-to-odd inverse object

For a rank-`m` path `P` in dimension `2m`, its upper-colour word `Delta P` is
a walk through rank `m+1`.  It has `M-1` terms but only `M-Cat_m` possible
colours.  If one can choose `P` so that every upper colour occurs in one
contiguous run, compressing equal runs gives a Hamilton path `R` of exact
length `M-Cat_m`.  Then, after choosing the orientation so that the seam is a
containment edge,

```
reverse(R) || ({z} union P)                              (8)
```

enumerates the complete middle layer in dimension `2m+1` with exactly
`W(2m+1)` vertices.  Identity (6) preserves the upper derivative structure.

The missing theorem is to obtain this **Catalan-compressed upper-colour path**
simultaneously with long runs, lower-shadow pinnability, and the seam
conditions.  This is much more precise than asking for an arbitrary optimal
array and directly reflects the exact Catalan saving forced by (5).

## 7. Complement duality

Coordinatewise complementation is an anti-automorphism, not a join
homomorphism:

```
complement(union interval) = intersection(complemented entries).
```

Thus complementing an OR-universal word does not generally produce another
OR-universal word.  It produces an intersection-universal word (all masks in
the full version, all proper masks in the nonzero version).  On the middle
layer in even dimension, however, complementation is a Johnson-graph
automorphism and exchanges lower intersection shadows with upper union
shadows.  Antipodal symmetry is therefore a legitimate reduction for central
path design, but not a dimension-reduction operation on completed OR words.

## 8. Product maps and their limitation

Iterating the trimmed lift gives `nu(k+ell)<=2^ell nu(k)`.  Symmetric-chain
products do better asymptotically: the Cartesian chain construction gives

```
nu(a+b) <= W(b)(2^a-1)+W(a)(2^b-1),
```

and the complement-bridge Euler product gives
`(sqrt(2)+o(1))W(a+b)` for a balanced split.  These are genuine product
constructions, but they pay for two independent endpoint-chain tasks.  The
known fixed-bipartition/one-interface lower bound shows that the leading
`sqrt(2)` is intrinsic to that paradigm.

To reach constant one, a product must follow the rank convolution

```
binom(a+b,r)=sum_j binom(a,j)binom(b,r-j)
```

and braid adjacent rank rectangles so that the same endpoints serve both
factors.  The two-bit square lifts and the Catalan-compressed parity braids are
the first finite-dimensional instances of this more global product idea.

## 9. Concrete mathematical targets

The most useful next lemmas are now sharply stated.

1. **Catalan-compressed union-row theorem.**  Construct, for every `m`, a
   rank-`m` Hamilton path `P` in `J(2m,m)` whose adjacent-union colours each
   occupy one interval and whose compressed union row has the required run
   and shadow properties.  This would give the correct even-to-odd central
   width rather than a doubled upper bound.
2. **Endpoint-safe intersection-braid theorem.**  Strengthen (7) so that exact
   lower pin-labelability and all upper shadows are inherited, not merely the
   central Hamilton row and one side of the derivative triangle.
3. **Section-forest absorption theorem.**  Given the path forest obtained by
   restricting a factorable even path to one coordinate section, reconnect
   `c` components using `O(c)` local absorbers while repairing all run and
   depth-`d` shadow defects.  Applied to the exact `k=12` row, `c=25`.
4. **Rank-distribution LP.**  Combine (R), (Q), and the short-interval pool
   inequalities.  Any improvement over the rank-slack lower bound obtainable
   from dimension restriction would appear first in this finite linear
   system.

The main conclusion is negative but productive: exact solutions in adjacent
dimensions are not ordinary homomorphic images of one another.  The natural
recursion lives at the level of paired central rows, edge-colour braids, and
endpoint reuse.  That is also where the binomial/Catalan arithmetic of the
conjectured value `B(k)` lives.
