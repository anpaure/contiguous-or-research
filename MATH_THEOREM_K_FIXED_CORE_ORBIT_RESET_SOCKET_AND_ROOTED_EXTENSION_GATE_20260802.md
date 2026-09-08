# Fixed-core orbit chainization, four-flag reset sockets, and the rooted extension gate

**Date:** 2026-08-02  
**Status:** exact interface theorem.  The K19 and K21 static factors are
unconditional inputs.  The address-drift and reset ledgers are exact.  The
result below identifies the precise extra Hall condition imposed by a
protected literal socket bank; it does **not** prove that such a bank exists.
No residence, upper-shadow, source, common-cap, compiler, or word claim is
made.

## 0. Verdict

The fixed-core orbit theorem and the four-flag theorem compose, but not by
post-processing an arbitrary static factor.

1. On every literal depth-three long row, legal chronology arcs satisfy
   \(\alpha\leq\beta\) in the order

   \[
        12/1<12/2<23/2<23/3.                         \tag{0.1}
   \]

   Orbit contraction cannot create a downward long-to-long arc.  Hence every
   long-only cycle is constant-flag and every descent uses a short row or a
   genuine macro.

2. The K19 and K21 fixed-core constructions provide optimal-depth anchored
   factors, and Theorem 7.3 of the fixed-core note reduces unprotected static
   chainization for any **fixed** chronology to a polynomial product-order
   max-flow.  The word “fixed” is load-bearing: deterministic lexicographic
   next-fit fails this flow at K17 and K21.

3. A prescribed literal reset socket removes named left and right resources.
   After that deletion, the residual graph is generally no longer
   orbit-biregular.  The old type flow is then only necessary.  The exact
   missing clause is residual occurrence-level Hall.

4. Orbit max-flow remains necessary and sufficient after planting when the
   protected bank is itself symmetry-balanced, so that every residual
   type-pair incidence graph remains biregular.  For a bounded asymmetric
   collar this balance is not automatic.

Thus the new static theorem supplies the correct prospective host, but does
not by itself plant reset sockets.  The smallest remaining lemma is a
**rooted orbit-extension theorem**, stated in Section 6.

## 1. Pointwise drift survives every quotient

Let a long row have strict targets

\[
                 L\subset M\subset U\subset T,        \tag{1.1}
\]

and put \(K=M\setminus L\), \(U\setminus M=\{p\}\).  With
\(B=K\cup Y\), \(Y\subseteq L\), and
\(A=\{p\}\cup Z\), \(Z\subseteq M\), the four exhaustive contiguous
three-cell normal forms are

\[
 (L,B,A),\quad(B,L,A),\quad(A,L,B),\quad(A,B,L).      \tag{1.2}
\]

For a transition from row \(j\), flag \(\alpha\), to row \(i\), flag
\(\beta\), the shared cells obey \(g_2=h_1\), \(g_3=h_2\).  If
\(\alpha>\beta\), direct substitution forces one of

\[
                 L_i=L_j\qquad\text{or}\qquad M_i=M_j. \tag{1.3}
\]

The exact target partition forbids either equality for distinct rows.  A
self arc is also impossible: all source cells lie in \(U_i\), so the entering
cell cannot enlarge \(U_i\) to the strict owner \(T_i\).  Therefore

\[
                         \boxed{\alpha\leq\beta}.       \tag{1.4}
\]

This proof is literal and pointwise.  Consequently averaging over a
fixed-core group, aggregating by orbit type, or contracting a static chain
factor cannot introduce a negative-drift long arc.  Any quotient transition
matrix is upper triangular as well.

Around a directed long-only cycle, (1.4) holds cyclically, so every flag is
equal.  A full-chain reinsertion still belonging to flag 3 is not a reset.
Only a short role, a noncontiguous state, or a certified macro outside the
four normal forms can lower the flag.

## 2. Exact reset budget of a depth-three factor

Let \(n_\ell\) be the number of chains of length \(\ell\),
\(\ell=1,2,3\), in an optimal-depth factor with \(W\) owner-anchored chains.
Let

\[
 \Lambda=\#\{\text{strict-lower targets}\},\qquad
 \delta=3W-\Lambda.                                  \tag{2.1}
\]

Then

\[
 n_1+n_2+n_3=W,\qquad 2n_1+n_2=\delta.              \tag{2.2}
\]

The number of short roles is

\[
 S=n_1+n_2=\delta-n_1,qquad
 \left\lceil{\delta\over2}\right\rceil\leq S\leq\delta. \tag{2.3}
\]

In any one-copy chronology let \(b\) be the number of maximal nonempty long
blocks.  Deleting the short roles gives exactly \(b\) long paths, and every
mixed block consumes at least one short role.  Hence

\[
                              b\leq S.                 \tag{2.4}
\]

For the selected long arcs define the three upward cut loads

\[
 D_t=\#\{\alpha\to\beta:\alpha\leq t<\beta\},
       \qquad t=0,1,2.                                \tag{2.5}
\]

The minimum number of anonymous nonneutral interval resets is

\[
 \rho(D)=D_0+(D_1-D_0)_+ +(D_2-D_1)_+
 =\max\{D_0,D_1,D_2,D_0+D_2-D_1\}.                  \tag{2.6}
\]

Therefore every literal completion satisfies

\[
                         \boxed{\rho(D)\leq b\leq S}. \tag{2.7}
\]

This is necessary, not sufficient: a physical short role may fail to attach
to the requested exit and entrance, and several consecutive short roles may
form only one socket block.

For K19, the generic count is

\[
 W={19\choose9}=92\,378,\quad \Lambda=2^{18}-1,\quad
 \delta=14\,991,                                     \tag{2.8}
\]

so every depth-three factor has

\[
                         7\,496\leq S\leq14\,991.      \tag{2.9}
\]

For K21, the generic count is

\[
 W={21\choose10}=352\,716,\quad \Lambda=2^{20}-1,\quad
 \delta=9\,573,                                      \tag{2.10}
\]

and

\[
                         4\,787\leq S\leq9\,573.       \tag{2.11}
\]

The proved fixed splits sharpen these ranges.  At K19, the three antichain
blocks have sizes

\[
                 W-15,\qquad W-14\,976,\qquad W.      \tag{2.12}
\]

Every final chain contains the last-block target.  Exactly 15 chains miss the
first block and exactly 14,976 miss the second.  If \(x\) chains miss both,
then \(0\leq x\leq15\), and the number of short chains is the union size

\[
                    S=14,991-x,qquad
                    14,976\leq S\leq14,991.         \tag{2.13}
\]

At K21, the three block sizes are

\[
                 W-837,\qquad W-8\,736,\qquad W.      \tag{2.14}
\]

Writing \(x\) for the number of chains missing both early blocks gives
\(0\leq x\leq837\) and hence

\[
                     S=9,573-x,qquad
                     8,736\leq S\leq9,573.          \tag{2.15}
\]

These are potential short-role counts, not certified reset sockets.  The
K19/K21 existence proofs do not select \(x\), do not expose socket states on
those short chains, and do not imply (2.7) for a later chronology.

## 3. The unprotected fixed-core product-order flow

Fix a core \(H\), let \(\Gamma\) be the symmetric group on its complement,
and let \(I\) and \(J\) be the left and right fixed-core types in the
product-order matching graph of a chronology \(\tau\).  Write

\[
                 s_i=|\mathcal O_i|,qquad c_j=|\mathcal O_j|. \tag{3.1}
\]

An arc \(i\to j\) exists exactly when the literal containment and time
conditions hold.  Theorem 7.3 of the fixed-core note says that the
unprotected anchored factor exists exactly when this finite type network has
a flow saturating every supply \(s_i\), with right capacities \(c_j\).
Every allowed literal type-pair graph is biregular, so a feasible type flow
spreads to a fractional literal matching, and ordinary bipartite integrality
gives an integral anchored factor.

This argument is existential.  It does not say that an arbitrary prescribed
literal edge or path is contained in some completion.

### 3.1 Fixed chronology is essential

The deterministic logarithmic-core next-fit/lex chronology has now been
tested by the exact product-order max-flow itself.  Its frozen output gives

\[
\begin{array}{c|c|c|c}
k&\Lambda&\text{maximum flow}&\text{deficiency}\\ \hline
17&65,535&65,249&286,\\
21&1,048,575&1,039,071&9,504.
\end{array}                                             \tag{3.2}
\]

The corresponding exact reachable shores are

\[
 37,323>37,037\quad(k=17),\qquad
 493,000>483,496\quad(k=21).                         \tag{3.3}
\]

Thus these fixed chronologies fail before any flag, residence, upper, or
compiler row is imposed.  This does not contradict the custom K19/K21 split
theorems: the K21 construction uses a different \(|H|=8\) orbit and a
different order, while K19 happens to pass this particular next-fit flow.

Consequently the within-rank orbit order cannot be chosen independently and
then decorated with sockets.  It is part of the existential protected-host
state.

## 4. Exact protected-fragment extension theorem

Let \(G_\tau=(L,R;E)\) be the literal product-order graph.  Let \(P\subseteq E\)
be a prescribed matching consisting of all static chain edges forced by a
protected pivot/reset fragment bank.  Put

\[
 L_P=\{\text{tails used by }P\},\qquad
 R_P=\{\text{heads used by }P\}.                      \tag{4.1}
\]

### Theorem 4.1 (rooted residual Hall)

The protected bank \(P\) extends to an anchored factor if and only if

\[
 \boxed{
 |N_{G_\tau}(X)\setminus R_P|\geq |X|
 \quad\text{for every }X\subseteq L\setminus L_P.}   \tag{4.2}
\]

#### Proof

The edges of \(P\) already match \(L_P\) to \(R_P\).  Every remaining left
vertex must be matched into an unused right vertex, so the residual problem
is precisely the bipartite graph

\[
       G_\tau[(L\setminus L_P),(R\setminus R_P)].     \tag{4.3}
\]

Hall's theorem applied to (4.3) is (4.2).  Appending its saturating matching
to \(P\) proves sufficiency.  \(\square\)

The full-shore type flow is a necessary projection of (4.2), but is not
sufficient after an asymmetric literal deletion: the remaining incidences
inside a type pair need not be biregular.

### Corollary 4.2 (symmetry-balanced planting)

Suppose the protected deletion is \(\Gamma\)-balanced in the following exact
sense:

* \(L\setminus L_P\) and \(R\setminus R_P\) are unions of transitive residual
  types; and
* every nonempty allowed residual type-pair incidence graph is biregular.

Let \(p_i=|L_P\cap\mathcal O_i|\) and
\(q_j=|R_P\cap\mathcal O_j|\).  Then (4.2) is equivalent to the residual
type max-flow with

\[
                         s_i'=s_i-p_i,qquad c_j'=c_j-q_j. \tag{4.4}
\]

Equivalently, for every set \(X\) of residual left types,

\[
          \sum_{i\in X}s_i'
          \leq\sum_{j\in N(X)}c_j'.                  \tag{4.5}
\]

#### Proof

Necessity follows by aggregation.  Under the two balance hypotheses, spread
a feasible residual type flow uniformly on every residual type-pair graph.
This gives a fractional matching saturating all residual left vertices;
bipartite integrality and Theorem 4.1 complete the proof.  \(\square\)

A full developed orbit of pairwise disjoint sockets is one way to meet the
hypotheses.  Merely choosing equal **numbers** of protected vertices in each
original orbit is not enough: their deletion can still destroy residual
biregularity.  Likewise a single literal collar is generally not covered by
Corollary 4.2.

When the residual type-neighborhood graph is unchanged, define the original
type-cut slack

\[
 \sigma_\tau(X)=
 \sum_{j\in N_\tau(X)}c_j-\sum_{i\in X}s_i.           \tag{4.6}
\]

Then (4.5) is exactly the cut-charge condition

\[
 \boxed{
 \sum_{j\in N_\tau(X)}q_j-\sum_{i\in X}p_i
 \leq \sigma_\tau(X)
 \quad\text{for every left-type set }X.}             \tag{4.7}
\]

Thus a protected bank is safe precisely when its net charge on every tight
or nearly tight type cut fits the pre-existing slack.  Total equality
\(\sum_i p_i=\sum_jq_j\) checks only the full cut and is insufficient.

The smallest counterexample is a single biregular type pair whose literal
graph is the eight-cycle

\[
\begin{aligned}
 l_1&\sim r_1,r_4,& l_2&\sim r_1,r_2,\\
 l_3&\sim r_2,r_3,& l_4&\sim r_3,r_4.
\end{aligned}                                         \tag{4.8}
\]

Protect \(l_1r_1\) and \(l_4r_3\).  Two left and two right vertices remain,
so type-count balance passes, but both remaining left vertices see only
\(r_2\).  Literal Hall fails.  This is exactly why residual equitability,
not merely balanced orbit counts, is required in Corollary 4.2.

## 5. Coupling reset demand to the type flow

Refine every long role type by its flag \(q\in\{0,1,2,3\}\), and refine every
short or macro type by its certified exit/entrance menu.  Let \(x_e\) select
long chronology arcs, and let \(y_{uv,\sigma}\) select sockets of physical
type \(\sigma\) which join a long exit of flag \(v\) to a long entrance of
flag \(u\).  A proof-safe joint quotient must impose all of the following:

\[
\begin{aligned}
 &\text{static product-order supply/capacity balance},\tag{5.1}\\
 &\text{one state/rectangle choice per physical role},\tag{5.2}\\
 &\text{one incoming and one outgoing chronology arc per selected state},\tag{5.3}\\
 &D_t(x)=\sum_{u<v,\sigma}y_{uv,\sigma}{\bf1}_{u\leq t<v}
       \quad(t=0,1,2),\tag{5.4}\\
 &\text{the rooted residual Hall condition (4.2), or (4.5) when balanced},\tag{5.5}\\
 &\text{literal endpoint, address, and propagated-history compatibility}.\tag{5.6}
\end{aligned}
\]

The number of fixed-core types is polynomial, and the four flag refinements
are constant.  Thus (5.1), (5.4), and the balanced form (5.5) remain a
polynomial max-flow/transportation system.  The nonlinear row is (5.2): a
role's incoming and outgoing menus must come from the same literal state.
The rooted asymmetric form (4.2) is also not compressed by orbit counts
without an additional extension theorem.

If the chronology is not frozen, introduce binary variables \(w_{it}\) which
place type \(i\) in block/time \(t\), with

\[
       \sum_t w_{it}=1,qquad
       \sum_i |\mathcal O_i|w_{it}\leq W.             \tag{5.7}
\]

Refine a successor-flow variable by both endpoint times and allow it only
when \(t<u\) and the two fixed-core types are product-order compatible.
This is a polynomial-size integer extended formulation, but no longer one
ordinary max-flow: chronology assignment, static flow, flag drift, and socket
selection are correlated decisions.  The failures in (3.2) prove that this
extra selection row cannot be dropped.

This gives the exact meaning of "planting without breaking the type flow":
the socket bank must either be selected inside the same completed factor, or
its removal must pass Theorem 4.1; a symmetry-balanced bank may use the
smaller Corollary 4.2 test.

## 6. Application to the K19/K21 orbit chronologies

The K19 fixed triple and K21 \(|H|=8\) intersection orbit settle the
unprotected static row.  They also give a finite catalogue of product-order
types in which a prospective socket bank can be represented.  However:

* the Dilworth factors are not rooted at prescribed pivot/reset fragments;
* no protected residual-Hall certificate is supplied;
* no four-flag state or endpoint menu is assigned to the short chains; and
* the strict interval-cut slack used to prove the K21 **uniform couplings** is
  not, by itself, a rooted literal matching slack after named deletions.

Therefore the current theorems neither prove nor disprove reset planting in
these chronologies.  What they do prove is that no new static chain-allocation
theorem is needed once the following smaller lemma is established.

### Rooted Orbit Transport with Sockets, \(\operatorname{ROTS}(k,H)\)

There is a fixed-core chronology \(\tau\), an optimal-depth anchored factor
for \(\tau\), and a protected short/macro bank \(P\) such that

1. every fixed static edge of \(P\) is product-order legal;
2. the flags and socket types of \(P\) satisfy (2.7) and (5.4);
3. \(P\) satisfies rooted residual Hall (4.2);
4. the selected literal states satisfy the endpoint and global address/history
   equations; and
5. the number of short roles used does not exceed the selected factor's
   \(S=n_1+n_2\).

For an orbit-balanced bank, item 3 reduces exactly to the polynomial cut
system (4.5).  For a bounded literal collar, item 3 is the genuine remaining
rooted extension clause.  In either case \(\tau\) must be selected jointly:
the lex-next-fit counterexamples (3.2) exclude a universal “choose order,
then repair” theorem.

Proving \(\operatorname{ROTS}\) would close the **static target allocation +
four-flag reset chronology** interface.  It would still leave residence,
all-width upper witnesses, topology/opening, common-cap, and the compiler.

## 7. K17 calibration and sharp scope

The independently replayed K17 long projection has maximum matching 14,844
into 18,646 hard long heads.  One frozen maximum matching has

\[
                 D=(6620,6003,4857),\qquad \rho(D)=6620. \tag{7.1}
\]

Since K17 has only 5,647 short roles, that particular long matching cannot be
completed even by anonymous reset sockets.  This is a no-go for the witness,
not for every maximum long matching.

The full long-plus-short projection still has matching
\(18115/18646\), deficiency 531.  A one-short correlated census finds only
445 short roles supporting any strict reset, no direct \(3\to0\) socket, and
2,162 short roles with no correlated one-short socket at all.  Multi-short
blocks and enriched macros remain outside that census.

These numbers illustrate why the K19/K21 raw short-chain counts in (2.9) and
(2.11) cannot replace the rooted Hall/socket rows of
\(\operatorname{ROTS}\).

## 8. Sources

This note uses, without strengthening their scope:

* `MATH_THEOREM_K19_K21_FIXED_CORE_NORMAL_SPLITS_AND_ALLK_ORBIT_TRANSPORT_GATE_20260802.md`;
* `MATH_THEOREM_K17_FOUR_FLAG_RESET_DEMAND_AND_CORRELATED_HALL_FLOW_20260802.md`;
* `MATH_AUDIT_K_K17_FOUR_FLAG_ADDRESS_DRIFT_CENSUS_20260802.md`.

The exact decorated-row common-base formulation is recorded separately in
MATH_THEOREM_A_FIXED_CORE_FLAGGED_CHAIN_STATE_COMMON_BASE_AND_RESET_CUTS_20260802.md.

The deterministic chronology diagnostic is
`/home/amodo/or15/work/root_allk_fixed_core_nextfit_flow_20260802`; its frozen
summary and cut SHAs are respectively
`65fb165a51553f912c56642754e49f5d529bc5675b2f19b7ca93ae5db87e56a8`
and
`09a9a2a1a5e0e22da2300df8174b695c1009bae71244f2033ff356723464d3fc`.
