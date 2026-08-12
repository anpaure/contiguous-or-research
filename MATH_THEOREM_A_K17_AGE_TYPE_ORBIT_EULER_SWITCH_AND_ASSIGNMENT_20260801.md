# The `k=17` age certificate: free-orbit rounding, the isolated-loop obstruction, and an exact Euler repair

Date: 2026-08-01  
Lane: A / age-composition one-copy quotient rounding  
Status: **unconditional quotient-level assignment theorem; correction of the displayed arc matrix**

> **Frozen-word scope.**  The legal switch proved below remains a valid
> alternative connected circulation.  It is not the switch used by the
> authoritative frozen 1430-position word
> `scratch/k17_age_type_euler_word_20260801.tsv` (SHA `e55bea55...`).  That
> word instead uses the unit two-way `F<->I` attachment recorded in
> `MATH_THEOREM_K17_EXACT_AGE_COMPOSITION_FRACTIONAL_ST_CERTIFICATE_20260801.md`.
> Do not mix the two arc ledgers in one physical encoding.

## 0. Verdict

The denominator `1430` of the exact `ST_(17,9,3)` certificate is perfectly
compatible with the `Z_17` owner quotient.  Every rank-nine owner orbit has
size `17`, so there are exactly

\[
                    {1\over17}{17\choose9}=1430       \tag{0.1}
\]

free owner orbits.  The nine integer type masses therefore assign one type
to each owner orbit with no stabilizer or divisibility loss.

There is, however, a precise error in using the **displayed** directed arc
counts as one cyclic type word.  The type

\[
                         e=(4,3,1,1)                  \tag{0.2}
\]

has mass `140`, and all of that mass is the isolated loop

\[
                         e\longrightarrow e:140.     \tag{0.3}
\]

No displayed arc enters or leaves `e`.  Hence those exact arc counts admit
a permutation of the 1430 quotient positions, but they do not admit one
1430-cycle.  Balance alone is insufficient for an Euler circuit; connected
support is also necessary.

This obstruction is removable without changing a single stationary type
mass or marked-rank capacity.  Replace one copy each of

\[
 (3,4,1,1)\to(3,3,2,1),qquad
 (4,3,1,1)\to(4,3,1,1)                               \tag{0.4}
\]

by

\[
 (3,4,1,1)\to(4,3,1,1),qquad
 (4,3,1,1)\to(3,3,2,1).                              \tag{0.5}
\]

Both new arcs satisfy every age-transition inequality.  The switch
preserves all row and column sums and makes the support strongly connected.
The repaired integral multigraph therefore has an Euler circuit of length
1430.  Reading its tail types around any prescribed cyclic ordering of the
1430 owner orbits assigns exactly one certified type to every orbit and
realizes the repaired transition multiplicities exactly.

Thus there is no quotient divisibility obstruction.  The first obstruction
was only the isolated circulation component in the particular published
arc decomposition, and the one-unit switch (0.4)--(0.5) removes it.

This theorem does not construct the cyclic ordering as a quotient Johnson
Hamilton cycle, choose edge voltages, or lift the type word to globally
consistent literal age partitions.  Those physical rows remain separate.

## 1. A general integral orbit-assignment theorem

Let `Omega` be a set of `N` quotient objects, let `T` be a finite type set,
and let `A subseteq T x T` be the allowed transition relation.  Suppose

\[
 b_t\in\mathbb Z_{\ge0},\qquad
 a_{tu}\in\mathbb Z_{\ge0}\quad((t,u)\in A)           \tag{1.1}
\]

satisfy

\[
 sum_t b_t=N,qquad
 sum_u a_{tu}=b_t=\sum_u a_{ut}quad(t\in T).        \tag{1.2}
\]

Write `G_a` for the directed multigraph having `a_tu` copies of `t->u`.

### Theorem 1.1 (permutation and one-cycle forms)

Under (1.1)--(1.2):

1. there are a type map `tau:Omega->T` with fibres of sizes `b_t` and a
   permutation `sigma` of `Omega` such that

   \[
      |\{x:\tau(x)=t,\ \tau(\sigma x)=u\}|=a_{tu};   \tag{1.3}
   \]

2. there are such data with `sigma` one `N`-cycle if and only if every
   positive-degree vertex of `G_a` lies in one weak component; equivalently,
   `G_a` has one Euler circuit containing all its arcs; and
3. if the condition in item 2 holds, then for **every already prescribed**
   cyclic ordering `x_0,...,x_(N-1)` of `Omega`, types can be assigned so
   that the transition counts along `x_i->x_(i+1)` are exactly `a_tu`.

#### Proof

For item 1, partition the `b_t` objects of type `t` into source boxes
`S_tu` of sizes `a_tu`.  Independently partition the `b_u` objects of type
`u` into target boxes `H_tu` of the same sizes.  Choose a bijection

\[
                         S_{tu}\longrightarrow H_{tu} \tag{1.4}
\]

for every ordered pair.  Every object has exactly one image and one
preimage by (1.2), so their union is a permutation satisfying (1.3).

If the permutation is one cycle, its successive type transitions form an
Euler tour of `G_a`; hence the nonzero support is weakly connected.  This
proves necessity in item 2.

Conversely, a finite balanced directed multigraph whose nonzero support is
weakly connected has an Euler circuit.  List the tails of its `N` successive
arcs as

\[
                         t_0,t_1,\ldots,t_{N-1}.       \tag{1.5}
\]

Assign `tau(x_i)=t_i` around any cyclic ordering of `Omega`.  The number of
occurrences of `t` is its outdegree `b_t`, and each arc copy is used exactly
once.  This proves items 2 and 3. \(\square\)

### Stabilizer qualification

If physical quotient objects have unequal orbit sizes, a type assigned to
one quotient object contributes the full size of that orbit, and extra
weighted divisibility conditions are unavoidable.  Theorem 1.1 concerns
the quotient count itself.  Section 2 proves that at `k=17` every relevant
owner orbit has the same size `17`, so no weighted qualification is needed.

## 2. The `Z_17` owner action is free

### Lemma 2.1 (no owner stabilizers)

The cyclic rotation group `Z_17` acts freely on the rank-nine subsets of
`[17]`.  The same is true at every rank `1,...,16`.

#### Proof

Because `17` is prime, every nonidentity rotation is one 17-cycle on the
ground coordinates.  A subset invariant under it is a union of its ground
orbits, hence is either empty or all of `[17]`.  A proper nonempty subset
cannot be fixed. \(\square\)

Therefore each selected owner-orbit type contributes exactly 17 literal
owners.  If `b_t` is its quotient mass, its literal mass is `17b_t`, which
is exactly

\[
 {b_t\over1430}{17\choose9}=17b_t.                   \tag{2.1}
\]

Likewise an integral quotient transition count `a_tu` lifts equivariantly
to `17a_tu` physical transitions.  Decorating a representative owner by an
age partition introduces no smaller decorated orbit: any stabilizer of the
decorated object would stabilize its underlying owner, and is therefore
trivial.

## 3. Exact obstruction in the displayed certificate

Use the type order

\[
\begin{array}{lll}
t_0=(1,5,2,1),&t_1=(1,6,1,1),&t_2=(2,5,1,1),\\
t_3=(3,3,2,1),&t_4=(3,4,1,1),&t_5=(4,3,1,1),\\
t_6=(5,1,2,1),&t_7=(5,2,1,1),&t_8=(6,1,1,1).
\end{array}                                           \tag{3.1}
\]

Their stationary masses are

\[
          (139,297,8,20,20,140,127,237,442),          \tag{3.2}
\]

which sum to 1430.  Thus type assignment to owner orbits is arithmetically
exact.

For the displayed arc matrix, however,

\[
 a_{55}=140,qquad a_{5u}=a_{u5}=0\quad(u\ne5).       \tag{3.3}
\]

Put `S={t_5}`.  Then

\[
 a(S,T-S)=a(T-S,S)=0,qquad 0<b(S)=140<1430.         \tag{3.4}
\]

Equation (3.4) is the smallest possible explicit Euler-support cut.  A
cyclic word containing a `t_5` position can never leave the `t_5` block,
while a word containing any other type can never enter it.  Since both
banks are nonempty, no single cyclic word realizes the displayed counts.

The other eight types lie in one strongly connected component: one may
trace the support through

\[
 t_0\to t_8\to t_4\to t_3\to t_7\to t_0,
 \qquad t_8\to t_1\to t_6\to t_2\to t_8,            \tag{3.5}
\]

with the remaining positive arcs internal.  Consequently the displayed
circulation has exactly two nonzero support components.  Theorem 1.1 still
realizes it by a successor permutation with two cycles, but never by one
1430-cycle.

This corrects the sentence that balance of the displayed type-transition
multigraph by itself supplies an Euler circuit.

## 4. One legal transportation switch repairs the support

Define a new integer arc matrix `a'` from the displayed one by

\[
\begin{aligned}
a'_{43}&=a_{43}-1=19,& a'_{55}&=a_{55}-1=139,\\
a'_{45}&=a_{45}+1=1,& a'_{53}&=a_{53}+1=1,             \tag{4.1}
\end{aligned}
\]

and leave every other entry unchanged.

### Lemma 4.1 (legality and conservation)

Every positive arc of `a'` satisfies

\[
                         c'_{i+1}\le c_i
                         \quad(0\le i<3),             \tag{4.2}
\]

and `a'` has exactly the same row and column sums (3.2) as the original
matrix.

#### Proof

Only the two new arcs require checking.  For `t_4->t_5`,

\[
                  (3,1,1)\le(3,4,1),                 \tag{4.3}
\]

and for `t_5->t_3`,

\[
                  (3,2,1)\le(4,3,1),                 \tag{4.4}
\]

coordinatewise.  These are exactly (4.2).

At source `t_4`, one outgoing `t_3` arc is replaced by one outgoing `t_5`
arc.  At source `t_5`, one loop is replaced by one outgoing `t_3` arc.
The column of `t_3` loses the former `t_4` arc and gains the new `t_5`
arc; the column of `t_5` loses one loop and gains the new `t_4` arc.  All
other rows and columns are unchanged. \(\square\)

### Theorem 4.2 (connected integral type word)

The repaired multigraph `G_(a')` is strongly connected and has an Euler
circuit of length 1430.  Hence the certified type masses admit one type per
`Z_17` owner orbit around any prescribed 1430-cycle, with exact integral
transition counts `a'`.

#### Proof

The eight-type component (3.5) reaches `t_4`, the new arc `t_4->t_5`
enters the old isolated vertex, and `t_5->t_3` returns to (3.5).  Thus all
nine types are strongly connected.  Lemma 4.1 gives equal indegree and
outdegree at every type, so Euler's theorem supplies a tour using all

\[
                         \sum_t b_t=1430             \tag{4.5}
\]

arcs exactly once.  Apply Theorem 1.1 to the 1430 free owner orbits. \(\square\)

## 5. Marked-rank capacities are unchanged

The marked-rank capacity of the age certificate depends only on the node
masses `b_t`, not on which legal balanced arc matrix realizes them.  The
switch (4.1) therefore leaves the exact table

\[
 (436,8,40,140,364,728,1144,1430)                    \tag{5.1}
\]

at ranks `1,...,8` unchanged.  For ranks `2,...,8`, these values equal the
numbers of `Z_17` target orbits exactly.  At the anonymous quotient-count
level, every available slot at those ranks may therefore be used and
bijections to abstract target-orbit names may be chosen independently;
rank one needs only one of its 436 available slots.

This last sentence is a **capacity assignment**, not a physical suffix-value
theorem.  Once a particular owner orbit and representative age partition
are fixed, the suffix target orbit is determined.  Proving that the actual
determined values are distinct is the still-open coloured quotient Hall
row.

## 6. Exact remaining scope

The theorem proves all of the following, without computation:

1. no owner-orbit stabilizer or weighted divisibility obstruction exists;
2. the nine stationary masses assign integrally one type per owner orbit;
3. the published fixed arc matrix has a one-cut/two-component obstruction
   to a single quotient cycle;
4. one legal unit `2x2` switch preserves all masses and mark capacities and
   yields a connected Eulerian type word; and
5. this word decorates any quotient owner cycle once that cycle is supplied.

It does **not** prove:

* existence of a Hamilton cycle in the quotient Johnson graph with the
  required lower-colour orbit rainbow;
* compatible representative age partitions around the cyclic closure;
* distinct actual suffix target orbits at ranks `2,...,7`;
* nonzero total voltage modulo 17;
* strict-upper interval-union coverage; or
* a literal source/common-cap compiler.

Accordingly the denominator and stabilizers are now discharged.  The
physical one-copy problem begins only after the repaired Euler type word is
coupled to owner-edge, partition-state and target-orbit data.
