# A global move-to-front / symmetric-chain route

This note records a general, non-computational route toward the conjectural
asymptotic value

\[
  \nu(k)=(1+o(1))W(k),\qquad
  W(k)=\binom{k}{\lfloor k/2\rfloor}.
\]

The main point is to cover the whole Boolean lattice by chains first, so that
"upper shadows" and "lower pinning" are no longer separate tasks.  The only
remaining issue is whether those chains can be visited by the exact
last-occurrence dynamics of an OR array.

Everything labeled theorem or lemma below is proved here.  The final
move-to-front tour statement is explicitly a conjectural missing lemma.

## 1. Ordered partitions and move-to-front

An ordered partition of `[k]` is a tuple

\[
  \Pi=(B_1,\ldots,B_s)
\]

of pairwise disjoint nonempty blocks whose union is `[k]`.  Define its nonempty
prefix-union chain by

\[
  \operatorname{Pref}(\Pi)
  =\{B_1,\ B_1\cup B_2,\ldots,
          B_1\cup\cdots\cup B_s\}.
\]

For a nonempty set `X subseteq [k]`, define

\[
  M_X(B_1,\ldots,B_s)
   =(X,B_1\setminus X,\ldots,B_s\setminus X),
\]

after deleting empty blocks.  Notice that all elements of `X` form **one**
new block.  They have equal last-occurrence time; they must not be split into
singletons.

If `Pi` is the last-occurrence ordered partition after reading an array prefix
and the next array entry is `X`, then the next state is exactly `M_X(Pi)`.
The suffix ORs at that endpoint are exactly `Pref(M_X(Pi))`.

## 2. The MTF--SCD tour theorem

Let `D={C_1,...,C_W}` be a symmetric chain decomposition (SCD) of the Boolean
lattice `2^[k]`.  It has

\[
  W=W(k)=\binom{k}{\lfloor k/2\rfloor}
\]

chains.

### Definition (MTF--SCD tour)

An MTF--SCD tour consists of

* an ordering `C_1,...,C_W` of the chains of `D`;
* ordered partitions `Pi_1,...,Pi_W` of `[k]`; and
* nonempty update sets `X_2,...,X_W`;

such that

\[
  C_i\setminus\{\varnothing\}
      \subseteq \operatorname{Pref}(\Pi_i)
\]

and

\[
  \Pi_i=M_{X_i}(\Pi_{i-1})\qquad(2\le i\le W).
\]

The SCD chains need only occur as subchains of the prefix chains; extra prefix
sets are harmless.

### Theorem 1 (tour implies a near-width OR array)

If an MTF--SCD tour exists, then

\[
  \boxed{\nu(k)\le W(k)+k-1.}
\]

#### Proof

Write `Pi_1=(B_1,...,B_s)`.  Start the array with the blocks in reverse order,

\[
  B_s,B_{s-1},\ldots,B_1.
\]

They are disjoint, so at the last of these `s` endpoints their last-occurrence
times are strictly ordered as `B_1,...,B_s`.  The state is exactly `Pi_1`.
Now append

\[
  X_2,X_3,\ldots,X_W.
\]

The state after appending `X_i` is `Pi_i`, by the definition of `M_X`.
Therefore every nonempty member of every SCD chain is a suffix OR at one of
these endpoints.  Since the SCD partitions `2^[k]`, every nonempty subset is
covered.

Finally `s<=k`, because an ordered partition of a `k`-element set has at most
`k` blocks.  The array length is

\[
  s+(W-1)\le k+W-1.
\]

This proves the claim.  ∎

This theorem handles all ranks simultaneously.  There is no separate union-
shadow theorem and no coordinate-pinning SAT instance: those jobs have been
absorbed into the fact that the assigned chains form an SCD.

### Theorem 2 (approximate version)

Suppose a move-to-front walk visits `L` ordered partitions and the union of
their prefix chains misses exactly `q` nonempty subsets of `[k]`.  Then

\[
  \nu(k)\le L+k-1+q.
\]

In particular, if

\[
  L=(1+o(1))W(k),\qquad q=o(W(k)),
\]

then `nu(k)=(1+o(1))W(k)`.

#### Proof

Initialize the first state in at most `k` entries and use one entry for each
of the remaining `L-1` transitions.  Append every missing set literally as a
one-entry mask.  Appending entries cannot destroy witnesses that already
exist.  ∎

The approximate formulation may be substantially easier than an exact tour.

## 3. Greene--Kleitman chain templates

Fix the standard Greene--Kleitman SCD.  A chain can be encoded by a word over
`{0,1,*}` of the form

\[
  C=w_0 * w_1 * \cdots * w_{h-1} * w_h,
\]

where each `w_i` is a Dyck word (with `0` as an opening symbol and `1` as a
closing symbol).  Let the star coordinates, from left to right, be

\[
  e_1,e_2,\ldots,e_h,
\]

and let `B` be the set of fixed `1` coordinates.  The sets in the chain are

\[
  B,\quad B\cup\{e_1\},\quad
  B\cup\{e_1,e_2\},\quad\ldots,\quad
  B\cup\{e_1,\ldots,e_h\}.
\]

Consequently, any ordered partition beginning with

\[
  B,e_1,e_2,\ldots,e_h
\]

(omitting `B` when empty and allowing arbitrary blocks after `e_h`) exposes
the chain `C` as prefix unions.

## 4. A genuine one-step transition

For `h>=2`, define `ell(C)` by replacing the last two stars of `C` by `0` and
`1`, respectively.  In template notation,

\[
\begin{aligned}
 C&=w_0*\cdots*w_{h-2}*w_{h-1}*w_h,\\
 \ell(C)&=w_0*\cdots*w_{h-2}\,0\,w_{h-1}\,1\,w_h.
\end{aligned}
\]

The latter is again a valid Greene--Kleitman template: the new substring
`0 w_(h-1) 1` is a Dyck word.

### Lemma 3 (last-pair exposure lemma)

Suppose the current ordered partition has the form

\[
  \Pi=(B,e_1,e_2,\ldots,e_h,R_1,\ldots,R_t),
\]

where `R_1,...,R_t` partition the fixed-zero coordinates (and `B` is omitted
if empty).  Put

\[
  X=B\cup\{e_h\}.
\]

Then the single update `M_X` produces a state whose prefix chain contains
`ell(C)`.

#### Proof, including the block-tie audit

All elements of `X` receive the same new last-occurrence time, so the new
first block is the single block `B union {e_h}`.  The old block `B` disappears
after subtracting `X`; the singleton block `{e_h}` also disappears.  Every
other star singleton and every `R_j` is disjoint from `X`, so their relative
order is unchanged.  Thus

\[
  M_X(\Pi)
   =(B\cup\{e_h\},e_1,e_2,\ldots,e_{h-1},R_1,\ldots,R_t).
\]

The minimum of `ell(C)` is `B union {e_h}`, and its remaining star increments
are `e_1,...,e_(h-2)`.  Therefore the prefix unions stopping just before
`e_(h-1)` are exactly the members of `ell(C)`.  The later block `e_(h-1)` and
the `R_j` create only extra prefix sets, which are harmless.  ∎

The same argument may be iterated as long as the current chain has at least
two stars.  The unused zero from each removed pair simply remains in the tail.

## 5. What fails: `ell` is not injective

It is tempting, but wrong, to infer that the `ell` edges automatically split
all Greene--Kleitman chains into only `Theta(W/k)` disjoint paths.

### Counterexample

In dimension four, both templates

```text
**01
01**
```

are valid and distinct.  Applying `ell` to either one gives

```text
0101
```

because in the first case the terminal `01` was already present, whereas in
the second case the initial `01` was already present.  Hence `ell` is many-to-
one.

More generally, a child template can have several preimages: any primitive
Dyck factor in its final Dyck block may be opened into two stars.

### Exact image of `ell`

A Greene--Kleitman template lies in the image of `ell` if and only if its
final Dyck block (the block after its last star, or the whole word if there is
no star) is nonempty.

* Necessity: applying `ell` inserts a nonempty Dyck factor
  `0 w_(h-1) 1` after the last surviving star.
* Sufficiency: choose any primitive factor `0u1` in the final Dyck block and
  replace its outer `0,1` by stars.  This gives a valid parent template that
  maps back to the child.

The templates outside the image are precisely those ending in a star.
Deleting that final star gives an arbitrary Greene--Kleitman template in
dimension `k-1`, and appending a star reverses the bijection.  Therefore

\[
  |\operatorname{im}(\ell)|=W(k)-W(k-1).
\]

So `ell` alone leaves at least `W(k-1)`, asymptotically about `W(k)/2`, path
starts in any injectively selected `ell`-edge path cover.  The one-step lemma
is useful local structure, but it is not by itself a constant-one
construction.

## 6. The exact remaining global lemma

The clean global state space is the following directed graph.

* A vertex is a pair `(C,Pi)`, where `C` is a chain of a fixed SCD and `Pi` is
  an ordered partition exposing `C`.
* There is an arc `(C,Pi) -> (C',Pi')` when some nonempty `X` satisfies
  `Pi'=M_X(Pi)` and `Pi'` exposes `C'`.

Different vertices may use the same chain `C`; choosing one state for each
chain is therefore a transversal condition.

### Missing lemma (state-transversal Hamilton path)

For every `k` (or merely asymptotically), there exists an SCD `D` of `2^[k]`
and a directed path in the state graph that contains exactly one vertex above
each chain of `D`.

By Theorem 1, this lemma would give

\[
  \nu(k)\le W(k)+k-1
       =(1+o(1))W(k).
\]

A weaker form is already enough: a path of `(1+o(1))W(k)` states whose prefix
chains miss only `o(W(k))` subsets.  Theorem 2 then gives the same asymptotic
conclusion.

### A more local path-cover/SDR formulation

Lemma 3 supplies certified arcs `C -> ell(C)`.  One can select at most one
parent from each fiber `ell^{-1}(D)`; this is an SDR choice and yields a
vertex-disjoint path cover.  The remaining task is to choose the SDR, the
exposing tail states, and one-step bridge arcs between the resulting paths so
that all paths splice into one directed transversal path.

The collision above shows why the SDR and bridge conditions cannot be
discarded.  A Hamilton cycle in the hypercube that contains the Greene--
Kleitman SCD also does not automatically solve them: cube adjacency of chain
endpoints is not the same relation as one-step move-to-front exposure of the
next chain.

## 7. Why this is the right big-picture target

This formulation has three advantages over a fixed central-row search.

1. An SCD covers every rank exactly once, so upper union shadows and lower
   coordinate pins are handled by one global object.
2. Every seam has exact cost one: it is an actual move-to-front arc exposing
   the next assigned chain.  There is no recursively accumulated padding.
3. The desired length is immediately `W(k)+O(k)`, stronger than merely
   `(1+o(1))W(k)`.

The proved progress is therefore the reduction and the last-pair transition,
not the existence of the tour.  The exact mathematical frontier is the
state-transversal Hamilton-path lemma above.
