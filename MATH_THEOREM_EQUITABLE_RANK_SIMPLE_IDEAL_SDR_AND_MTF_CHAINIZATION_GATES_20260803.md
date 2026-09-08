# Equitable rank-simple ideal SDRs and the exact MTF chainization gates

**Date:** 2026-08-03

**Status:** unconditional equitable containment theorem, exact equitable
chain-ladder reduction, a sharp move-to-front obstruction, and conditional
`B(k)+1` compiler theorem.  The ideal SDR can be made perfectly load-balanced
and rank-simple, but nestedness and one common chronology remain genuinely
stronger correlation problems.  No unconditional `B(k)+O(1)` result is
claimed.

## 0. Parameters and conclusion

Assume `k>=3`; the smaller cases are immediate.  Put

\[
 r=\left\lceil\frac k2\right\rceil,
 \qquad W={k\choose r},
 \qquad
 \mathcal L=\{S\subseteq[k]:1\le |S|<r\},
 \qquad \Lambda=|\mathcal L|,
\]

\[
 \rho=\frac{\Lambda}{W},\qquad
 a=\lfloor\rho\rfloor,\qquad
 b=\Lambda-aW,\qquad
 D=\lceil\rho\rceil,
\]

and

\[
 d=\min\left\{q:qW+{q+1\choose2}\ge\Lambda\right\},
 \qquad B(k)=W+d.
\]

The ideal containment theorem
`MATH_THEOREM_IDEAL_CONTAINMENT_SDR_DEPTH_DPLUS1_AND_CHAINIZATION_GATE_20260801.md`
gives `d<=D<=d+1`.  The new unconditional
strengthening is:

> Every lower target can be assigned to a containing rank-`r` owner so that
> exactly `b` owners receive `a+1` targets, every other owner receives `a`,
> and no owner receives two targets of one rank.

Thus scalar load imbalance and repeated-rank collisions are not the
chainization obstruction.  The remaining implications are

\[
\boxed{
\begin{array}{c}
\text{equitable rank-simple owner bundles}\quad\text{(proved)}\\
\Downarrow\quad\text{global adjacent-slice Hall}\quad\text{(open all-}k\text{)}\\
\text{equitable nested owner chains}\\
\Downarrow\quad\text{state-lifted MTF / near-Euler trace choice}\quad\text{(open)}\\
\text{one lower--central chronology}\\
\Downarrow\quad\text{upper completion on the same word}\quad\text{(open)}\\
\nu(k)\le B(k)+O(1).
\end{array}}
\]

Section 3 gives the exact chronology test on a fixed odd contracted
middle-levels skeleton.  Section 5 proves a separate sufficient joint
theorem with the numerical conclusion `nu(k)<=B(k)+1`; it is not a converse
characterization of every near-optimal word.

## 1. Equitable rank-simple containment

Call an owner assignment **rank-simple** if no owner receives two targets
of the same cardinality.

### Theorem 1.1 (equitable rank-port SDR)

There is a map

\[
                         \phi:\mathcal L\longrightarrow { [k]\choose r}
\]

such that

1. \(S\subseteq\phi(S)\) for every target `S`;
2. exactly `b` owner fibres have size `a+1` and the other `W-b` have size
   `a`; and
3. every fibre is rank-simple.

In particular, the maximum owner load is `D<=d+1`.

#### Proof

Make a flow network with a vertex for every target, a port `(T,s)` for every
owner `T` and lower rank `s`, and a vertex for every owner.  A rank-`s`
target `S` may enter `(T,s)` exactly when \(S\subset T\).  Give every target
unit supply, every port capacity one, and every owner-to-sink arc lower and
upper capacities `a,a+1`.

Send each target uniformly to its containing owners.  A rank-`s` target has
\(\binom{k-s}{r-s}\) such owners.  The fractional load on one port is therefore

\[
 { {r\choose s}\over {k-s\choose r-s}}
 ={{k\choose s}\over{k\choose r}}\le1.              \tag{1.1}
\]

The equality is the usual double count of pairs \(S\subset T\); the final
inequality uses that rank `r` is a largest Boolean rank.  Summing (1.1) over
`s<r` gives every owner load exactly `rho`, which lies in `[a,a+1]`.
Hence the lower/upper-capacitated network has a feasible fractional flow.

All capacities and supplies are integral, so network-flow integrality gives
an integral flow.  Every target then uses one containing owner, every rank
port carries at most one target, and every owner load is the integer `a` or
`a+1`.  Since the total load is `aW+b`, precisely `b` owners have the larger
load.  \(\square\)

The theorem is stronger than a `D`-slot SDR, but it does not say that two
targets in one fibre are comparable.

### Corollary 1.2 (odd coatom-rooted equitable bundles)

Let `k=2r-1` and put

\[
                         \mathcal Q={ [k]\choose r-1}.
\]

Then the complete strict lower ideal can be partitioned into `W` rooted
bundles `E_Q`, one for each \(Q\in\mathcal Q\), with the following properties:

* every member of `E_Q` is contained in `Q`;
* `Q in E_Q`;
* every bundle is rank-simple; and
* exactly `b` bundles have size `a+1`, while the others have size `a`.

Moreover the roots can be matched to distinct rank-`r` owners `T_Q` with

\[
                         S\subseteq Q\subset T_Q
                 \qquad(S\in E_Q).                         \tag{1.2}
\]

#### Proof

Apply the rank-port network of Theorem 1.1 to ranks `1,...,r-2`, using the
rank-`r-1` coatoms as the right shore.  The two middle ranks have equal size
`W`, and the uniform fractional load at a coatom is

\[
 \sum_{s=1}^{r-2}
 { {r-1\choose s}\over{k-s\choose r-1-s}}
 =\frac{\Lambda-W}{W}=\rho-1.                       \tag{1.3}
\]

Thus `b` coatoms receive `a` residual targets and every other coatom receives
`a-1`; rank ports again make these targets rank-simple.  Adjoin the coatom
itself.  The resulting bundle sizes are `a+1` and `a` as asserted.

The incidence graph between ranks `r-1` and `r` is `r`-regular on two shores
of size `W`, hence has a perfect matching.  Match every coatom to a distinct
owner and use transitivity of containment.  \(\square\)

### Proposition 1.3 (equity and rank simplicity do not uncross)

At `k=5,r=3`, the following is a complete ideal assignment:

\[
\begin{array}{c|c@{\qquad}c|c}
123&13,2&124&12,4\\
125&15&134&14\\
135&35,1&145&45\\
234&23&235&25,3\\
245&24,5&345&34.
\end{array}                                             \tag{1.4}
\]

Every singleton and pair occurs once, every target lies in its displayed
owner, five fibres have size two and five have size one, and no fibre repeats
a rank.  Yet every size-two fibre consists of a pair and a singleton outside
that pair, so its two targets are incomparable.  With owners frozen, at most
one target can be retained from each heavy fibre; the maximum nested
retention is `10/15`.

Thus even the exact histogram and rank ports do not permit ownerwise sorting
or lattice uncrossing.  Any positive Boolean chainization theorem must make
global exchanges between owners.  \(\square\)

## 2. Equitable chains are an exact Hall ladder

The next statement is most transparent in odd dimension, where every one of
the `W` chains must contain one coatom root.

### Theorem 2.1 (equitable ladder equivalence)

Let `k=2r-1`, set \(A_1=\mathcal Q\), and partition the remaining lower targets
into ordered slices `A_2,...,A_q`.  There is a coatom-rooted chain partition
whose member at distance `j-1` from the root lies in `A_j` if and only if,
for every `1<=j<q`, the containment graph admits an injection

\[
 m_j:A_{j+1}\hookrightarrow A_j,
 \qquad S\subsetneq m_j(S).                           \tag{2.1}
\]

Equivalently, every adjacent slice satisfies the Hall inequalities

\[
 |X|\le |N_{A_j}(X)|\qquad(X\subseteq A_{j+1}).       \tag{2.2}
\]

If `n_j=|A_j|` and `n_(q+1)=0`, the resulting chain-size histogram is

\[
 \#\{C:|C|\ge j\}=n_j,
 \qquad
 \#\{C:|C|=j\}=n_j-n_{j+1}.                         \tag{2.3}
\]

Consequently an equitable rooted chain partition with sizes `a` and `a+1`
exists exactly when one can choose such a Hall ladder with

\[
 n_1=\cdots=n_a=W,
 \qquad n_{a+1}=b,                                   \tag{2.4}
\]

where the last slice is omitted when `b=0`.

#### Proof

Given the injections, orient every matched edge from `A_(j+1)` toward
`A_j`.  Every vertex has one upward edge except at `A_1`, and injectivity
gives indegree at most one.  Slice indices decrease, so the components are
disjoint inclusion paths ending at distinct coatoms.  They partition every
slice and are the desired rooted chains.

Conversely, consecutive members of the rooted chains give the injections.
Exactly the chains reaching slice `j` have length at least `j`, proving the
first identity in (2.3); subtraction gives the second.  The histogram is
equitable precisely for (2.4).  Hall's theorem makes (2.1) and (2.2)
equivalent.  \(\square\)

Theorem 1.1 supplies the cardinalities in (2.4) only after forgetting
comparability.  It supplies none of the correlated adjacent Hall rows
(2.2).  Theorem 2.1 is the odd, equitable specialization of the ordered-slice
Hall reduction developed in
`MATH_THEOREM_IDEAL_CHAINIZATION_NORMALIZED_LADDER_AND_SCD_FRAGMENTATION_GAP_20260801.md`;
the exact histogram (2.3)--(2.4) is recorded here because it is the load
interface needed below.

### Relation to equitable Boolean chain decompositions

Appending the distinct rank-`r` owner to every rooted lower chain identifies
an equitable factor in Theorem 2.1 with an equitable partition of

\[
                 \{S\subseteq[k]:1\le |S|\le r\}
\]

into exactly `W` chains.  The chain sizes are `a+1` and `a+2`, the two
integers surrounding the average `rho+1`.

This is not a routine consequence of normalized matching.  In particular,
even the weaker assertion of a maximum-`D` anchored factor has a strong
full-lattice consequence.  In odd dimension, pair the lower chains under
complementation as follows.  Each lower chain contains a unique coatom
`A_T`; the map from owners to these coatoms is a bijection.  Choose the
permutation `psi` of owner labels satisfying

\[
                         A_{\psi(T)}=[k]\setminus T.
\]

Then

\[
                         C_T\cup\overline{C_{\psi(T)}}       \tag{2.5}
\]

is a chain, and these `W` chains partition all nonempty proper subsets.
Adding \(\varnothing\) and \([k]\) to two chains gives maximum size at most
`2D+1`.  Since

\[
                         \frac{2^k}{W}=2\rho+\frac2W,
\]

this maximum is strictly below the full-lattice average plus three.

That is a one-sided additive-constant uniform-chain theorem, not the full
Füredi floor/ceiling conjecture: it controls only the maximum, and it does
not impose rank symmetry or pair long and short half-chains equitably.
Tomon's normalized-matching theorem gives only a factor-two maximum at this
scale, while the Sudakov--Tomon--Wagner upper-half construction makes almost
all chains asymptotically uniform but leaves an exceptional family; neither
gives this all-chain additive maximum.  Therefore an unconditional
`ideal SDR => nested depth D` theorem would cross a major static frontier.
The precise inherited bounds are recorded in
`MATH_THEOREM_OWNER_CHAINIZATION_CONSTANT_FACTOR_SHARP_BARRIER_20260801.md`
and
`MATH_THEOREM_ASYMPTOTIC_SHARP_ANCHORED_CHAIN_FACTOR_FROM_STW_20260801.md`.

## 3. Exact age flags for one MTF chronology

Now fix odd `k=2r-1` and a cyclic middle-levels order

\[
 Q_0,Q_1,\ldots,Q_{W-1},
 \qquad
 Q_{i+1}=Q_i-\{\alpha_i\}+\{\beta_i\},              \tag{3.1}
\]

with indices modulo `W`, such that the `Q_i` are all coatoms and

\[
                         T_{i+1}=Q_i\cup Q_{i+1}      \tag{3.2}
\]

are all rank-`r` owners.  The unmarked skeleton is supplied by a middle
levels Hamilton cycle.  Its compatibility with prescribed lower chains is
not automatic.

Let a rooted chain `C_i` be refined to a weak `q`-flag

\[
 F^i_0\subseteq F^i_1\subseteq\cdots\subseteq
 F^i_{q-1}=Q_i,                                      \tag{3.3}
\]

where every member of `C_i` occurs among the displayed values.  Put

\[
 D^i_0=F^i_0,
 \qquad D^i_t=F^i_t\setminus F^i_{t-1}\quad(1\le t<q).
                                                               \tag{3.4}
\]

### Theorem 3.1 (exact MTF flag transport)

The flags (3.3) arise from one cyclic depth-`q` source word if and only if,
for every `i`,

\[
 \boxed{
 \alpha_i\in D^i_{q-1},
 \qquad
 D^{i+1}_{t+1}\subseteq D^i_t\quad(0\le t<q-1).}     \tag{3.5}
\]

When (3.5) holds, the appended letter entering `Q_(i+1)` is

\[
                         A_{i+1}=D^{i+1}_0.           \tag{3.6}
\]

It is nonempty because it contains the newborn coordinate `beta_i`.

#### Proof

Interpret `D^i_t` as the coordinates whose most recent occurrence has age
`t` in the last `q` letters.  A surviving positive-age coordinate at the
next state must have had age one less, giving the inclusions in (3.5).  The
departing coordinate is not refreshed and must leave from the oldest class,
giving the first condition.

Conversely, append (3.6).  Since the `D` classes partition `Q_i` and
`Q_(i+1)`, and the owners differ only by deleting `alpha_i` and inserting
`beta_i`, the complement of the displayed survivor classes in
`Q_(i+1)` is exactly

\[
 \{\beta_i\}\mathbin{\dot\cup}
 (D^i_{q-1}\setminus\{\alpha_i\})
 \mathbin{\dot\cup}
 \mathop{\dot\bigcup}_{t=0}^{q-2}
       (D^i_t\setminus D^{i+1}_{t+1}).               \tag{3.7}
\]

This is \(D^{i+1}_0\); every other coordinate ages by one.  Hence the new age
classes are exactly those prescribed in (3.4), proving sufficiency.
\(\square\)

### Corollary 3.2 (conditional `B+1` lower--central spelling)

Suppose the complete strict lower ideal has a coatom-rooted chain partition
of maximum size `q`, and its chains admit flags (3.3) satisfying (3.5) on a
rainbow middle-levels cycle.  Then one word of length

\[
                             W+q                         \tag{3.8}
\]

contains every strict-lower target and every rank-`r` owner as a contiguous
union.  In particular, `q=D<=d+1` gives a lower--central word of length at
most `B(k)+1`.

#### Proof

The closing predecessor forces \(\beta_{W-1}\in D^0_0\), so this class is
nonempty.  Choose `x in D^0_0`.  Initialize the age state by the `q`
nonempty letters

\[
 D^0_{q-1}\cup\{x\},\ldots,
 D^0_1\cup\{x\},D^0_0.                              \tag{3.9}
\]

Their suffix unions are the flag values `F^0_t`.  Append the `W` cyclic
letters (3.6), including the closing turn back to `Q_0`.  Theorem 3.1 shows
that every rooted chain is exposed at its coatom state.

At the turn `Q_i -> Q_(i+1)`, the previous `q` letters have union `Q_i` and
the new letter contains `beta_i` but no coordinate outside `Q_(i+1)`.  The
corresponding length-`q+1` window therefore has union

\[
                         Q_i\cup Q_{i+1}=T_{i+1}.     \tag{3.10}
\]

All lower targets and all owners occur.  The total length is `q+W`.
\(\square\)

Theorem 3.1 is the weak-flag form of the exact age criterion in
`MATH_THEOREM_AGE_FLAG_RUN_CRITERION_AND_FULL_FLAG_REFINEMENT_20260802.md`;
it is included here to expose the precise interface with Theorem 2.1.

Corollary 3.2 is deliberately lower--central.  It makes no upper-rank,
residence, or common-cap claim.

## 4. A three-local chronology obstruction

Pairwise existential MTF compatibility is not composable because the first
update coalesces its mask into one tied block.

### Lemma 4.1 (three-minimum aperture sharpening)

For `i=0,1,2`, let

\[
 C_i=(B_i=C_{i,0}\subsetneq C_{i,1}\subsetneq\cdots)
\]

be nontrivial chains with nonempty minima, and put

\[
                         G_2=C_{2,1}\setminus B_2.
\]

Suppose ordered partitions `Pi_i` expose `C_i` and

\[
 \Pi_1=M_{X_1}(\Pi_0),
 \qquad
 \Pi_2=M_{X_2}(\Pi_1)                                \tag{4.1}
\]

for nonempty update masks.  If `|B_0|=|B_1|` and `B_0!=B_1`, then

\[
 \boxed{B_1\setminus(B_0\cup B_2)\subseteq G_2.}     \tag{4.2}
\]

For a saturated first step, `G_2` is a singleton, recovering and sharpening
the older cardinality obstruction
\( |B_1\setminus(B_0\cup B_2)|\le1 \).

#### Proof

The first block of `Pi_1` is `X_1 subseteq B_1`.  In the residual ordered
partition `Pi_0-X_1`, both `B_0-X_1` and `B_1-X_1` are prefix unions and
therefore comparable.  The inclusion

\[
                         B_0-X_1\subseteq B_1-X_1
\]

would imply `B_0 subseteq B_1`, because `X_1 subseteq B_1`; equal
cardinality would force equality.  Hence

\[
 B_1-X_1\subseteq B_0-X_1,
 \qquad B_1\setminus B_0\subseteq X_1.               \tag{4.3}
\]

Now `X_2 subseteq B_2`.  If `X_2` is a proper subset of `B_2`, the first
surviving residual block `X_1-X_2`, when nonempty, must be consumed before
the prefix `B_2` closes, and therefore lies in `B_2`.  Thus
`X_1 subseteq B_2`.  If `X_2=B_2`, the same residual block appears
immediately after the completed minimum and must lie in the first aperture
`G_2`.  In either case

\[
                         X_1\setminus B_2\subseteq G_2.       \tag{4.4}
\]

Combine (4.3) and (4.4).  \(\square\)

The condition depends on three consecutive minima and the next aperture.
It is invisible to owner loads, chain sizes, adjacent containment Hall, and
the projected pairwise quotient graph.

### Corollary 4.2 (pairwise arcs need not lift to a state path)

On `U={a,b,c,d,e,f,g}`, take

\[
\begin{aligned}
C_0&=(ab\subset abg),\\
C_1&=(cd\subset acd\subset abcd\subset abcdg),\\
C_2&=(ef\subset cef\subset cdef\subset acdef
          \subset abcdef\subset U).
\end{aligned}                                             \tag{4.5}
\]

After deleting `cd`, the first and second chains are subchains of one
prefix chain; after deleting `ef`, the second and third are likewise.
Thus the exact quotient-chain test gives existential arcs `C_0->C_1` and
`C_1->C_2`.  But

\[
 B_1\setminus(B_0\cup B_2)=\{c,d\},
 \qquad G_2=\{c\},                                    \tag{4.6}
\]

so Lemma 4.1 forbids a common two-step state lift.  A Hamilton path in the
projected compatibility graph is therefore not a chronology certificate.
The quotient-chain test and the move-to-front block-coalescence rule used
here are the exact criteria proved in `MTF_TRANSVERSAL.md`.

### Proposition 4.3 (perfect nested equity still need not serialize)

For every `N,D>=2` there is an equal-rank owner-containment instance with
`N` owners and `ND` targets such that

* the `D`-slot graph is complete;
* the targets have a perfectly equitable integral partition into `N`
  nested `D`-chains; but
* no one-step MTF transition exists between two distinct selected chains.

#### Construction and proof

Take disjoint blocks

\[
 U_i=B_i\mathbin{\dot\cup}\{e_{i,1},\ldots,e_{i,D-1}\},
 \qquad |B_i|=2,
\]

put \(U=\dot\bigcup_i U_i\), and take a disjoint set `V` of size `|U|+2`.  The
ground set has size `2|U|+2` and central rank `|U|+1`.  Choose distinct
\(y_i\in V\) and owners

\[
                         T_i=U\cup\{y_i\}.
\]

Assign to `T_i` the saturated chain

\[
 B_i\subset B_i+e_{i,1}\subset\cdots\subset
 B_i+e_{i,1}+\cdots+e_{i,D-1}.                     \tag{4.7}
\]

Every target lies in every owner, so the slot graph is complete, and (4.7)
is a perfectly uniform nested factor.

For \(i\ne j\), let `X` be any admissible anchor for a transition into chain
`j`.  If `X` is a proper subset of `B_j`, the nonempty residual minimum
`B_j-X` is incomparable with the disjoint source minimum `B_i`.  If
`X=B_j`, the first target increment is `{e_(j,1)}`, again incomparable with
`B_i`.  The quotient chains cannot lie in one prefix chain, so no one-step
transition exists.  Productive endpoints for the `N` chains therefore have
span at least `2N-1`; fixing `D` and letting `N` grow rules out any uniform
`N+O(D)` consequence from these hypotheses.  \(\square\)

This is an abstract equal-rank containment instance, not a counterexample
to a Boolean-specific all-`k` theorem.  It proves that SDR, nestedness, and
equitable loads alone cannot imply MTF chronology.

## 5. A state-lifted theorem strong enough for `B+O(1)`

For a word prefix, use the **partial last-occurrence state**: the ordered
partition of the coordinates that have appeared so far, from most recent
to oldest occurrence.  Unseen coordinates need not be initialized.  If the
next nonempty letter is `X`, the state changes by

\[
 M_X(R_1,\ldots,R_s)
 =(X,R_1\setminus X,\ldots,R_s\setminus X),          \tag{5.1}
\]

after empty blocks are removed.  Its prefix unions are exactly the suffix
unions ending at that word position.

Indeed, for a prefix of recency blocks, cut the word immediately before the
oldest last-occurrence time represented in that prefix.  The resulting
suffix union is exactly the prefix union; redundant intervening times do not
change it.

### Theorem 5.1 (partial-state `B+1` compiler)

Assume the strict lower ideal has an anchored depth-`D` chain factor

\[
                         (C_T:T\in{[k]\choose r}).
\]

Suppose there are

* an ordering `T_1,...,T_W` of the owners;
* partial ordered-partition states `Pi_1,...,Pi_W`; and
* nonempty update masks `X_2,...,X_W`

such that

1. `Pi_i` exposes every member of `C_(T_i)` and the owner `T_i`;
2. `Pi_i=M_(X_i)(Pi_(i-1))` for `2<=i<=W`;
3. every upper target `S`, `|S|>r`, is a prefix union of some `Pi_i`; and
4. the first state is the coarsest flag of its owner chain.

More explicitly, if

\[
 C_{T_1}=(S_1\subsetneq\cdots\subsetneq S_q),
\]

take

\[
 \Pi_1=(S_1,S_2\setminus S_1,\ldots,
         S_q\setminus S_{q-1},T_1\setminus S_q),      \tag{5.2}
\]

with the evident interpretation `Pi_1=(T_1)` when `q=0`.

Then

\[
                         \boxed{\nu(k)\le W+D\le B(k)+1.}     \tag{5.3}
\]

#### Proof

Every block in (5.2) is nonempty and the number of blocks is `q+1<=D+1`.
Write these blocks in reverse order.  Their last-occurrence order is now
exactly `Pi_1`, so all targets in the first chain and its owner are suffix
unions.

Append `X_2,...,X_W`.  The partial move-to-front rule (5.1) proves by
induction that the productive state at step `i` is `Pi_i`.  The owner-chain
factor covers every nonempty rank below `r`; the distinct `T_i` cover rank
`r`; hypothesis 3 covers every higher rank.  Hence the word is universal.
Its length is

\[
 (q+1)+(W-1)=W+q\le W+D\le W+d+1.                  \tag{5.4}
\]

This is (5.3).  \(\square\)

The use of a partial state is load-bearing: initializing the unseen
complement of `T_1` as an artificial last block would waste one unnecessary
letter and give only `B+2`.

### Trace-Euler interpretation

Theorem 5.1 asks for a state-lifted path, not merely an ordering of abstract
chains.  A separate, stronger fixed-window sufficient formulation chooses
one admissible depth-`D` trace edge for every owner-chain in the order-`D`
de Bruijn graph.  Assume explicitly that the selected coloured edges,
together with `C` bridge edges, form one Euler trail.  Its spelled
lower--central word has length `W+D+C`; if that same word also covers the
upper targets, then

\[
                         \nu(k)\le B(k)+C+1.          \tag{5.5}
\]

A bounded number of trace components is not enough: two generic boundary
states cost `D` letters to reset.  The exact required invariant in this
fixed-window formulation is trace-Euler bridge cost `C=O(1)`; a checkable
sufficient condition is total suffix--prefix overlap deficit `O(1)` for an
ordering of its trail components.  This is the scoped trace theorem of
`MATH_THEOREM_BOUNDED_CHAIN_TRACE_EULER_SERIALIZATION_AND_SIDECAR_DISTANCE_20260801.md`.

## 6. Exact remaining theorem

In the load-and-rank-port projection, the ideal SDR has now been pushed as
far as ordinary bipartite integrality allows:

* loads are exactly equitable;
* every owner fibre is rank-simple; and
* in odd dimension every fibre may be rooted at a unique coatom and attached
  to a distinct owner.

None of these statements supplies comparability.  Within the odd,
coatom-rooted, perfectly equitable anchored-`D` route, the exact static
target is the saturated Hall ladder (2.2)--(2.4), a strong one-sided
uniform-chain problem.  It is a sufficient special route, not a necessary
description of every `B+O(1)` construction: the exact endpoint budget also
allows the non-equitable triangular capacity profile recorded in
`MATH_THEOREM_OPTIMAL_TRIANGULAR_FRACTIONAL_CHAIN_FACTOR_20260801.md`.
Even after the equitable ladder is solved, its exact dynamic target on the
fixed odd skeleton is a joint choice of weak flags and a rainbow owner cycle
satisfying (3.5).  A separate, stronger fixed-window sufficient target is a
coloured trace selection with `O(1)` bridge cost.  Finally the same word must
carry the upper targets.

The chronology obstruction is not another load inequality: Lemma 4.1 is
three-local and Proposition 4.3 persists even under perfect integral
nestedness and equity.  Therefore no implication of the form

\[
 \text{ideal SDR with }D\le d+1
 \Longrightarrow
 \text{MTF-compatible nearly uniform endpoint chains}
\]

is valid without a Boolean-specific global exchange theorem and a
state-lifted chronology theorem.  Theorem 5.1 identifies a sufficient joint
object strong enough for `B(k)+O(1)` and fixes its sharp additive accounting;
constructing that object remains open.
