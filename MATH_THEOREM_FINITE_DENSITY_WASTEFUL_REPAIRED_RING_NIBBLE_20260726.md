# Finite-density repaired-ring nibble: exact waste ledger, weighted quarantine, and the bridge-energy gate

Date: 2026-07-26

Scope: repaired promotion-ring owner packing.  This note does not invoke a
fixed-uniformity Pippenger--Spencer theorem.  It gives a self-contained
finite-density reduction which is strictly weaker than the previously stated
hereditary `RPRN(z)` condition.

## 0. Outcome

Use the notation of
`MATH_AUDIT_REPAIRED_PROMOTION_RING_OWNER_HYPERGRAPH_CODEGREES_AND_NIBBLE_GATE_20260726.md`:

\[
 N=N_H,\qquad W=\binom{2m}{m},\qquad r=m+H-k\sim m,
\]

and let (R) and (D=\rho R), (\rho=1-o(1)), be the root and owner
degrees.  Every edge consists of one root and (r) owners.

There are three conclusions.

1.  There is an exact **wasteful bite** whose primitive choices are
    independent.  Mark each current edge with probability

    \[
       p={\gamma\over rR},                                      \tag{0.1}
    \]

    put every isolated marked edge into the matching, and delete every
    vertex lying in *any* marked edge.  Thus vertices of colliding marked
    edges are waste.  Independent compensating coins can make every current
    vertex have exactly the same survival probability (q).

    For every vertex set (S), the compensated survivor law has the exact
    formula

    \[
      \boxed{
      \Pr(S\subseteq V^*)
       =q^{|S|}(1-p)^{-J(S)},\qquad
      J(S):=\sum_{v\in S}d(v)-\left|\bigcup_{v\in S}{\cal E}(v)\right|.}
                                                                  \tag{0.2}
    \]

    In particular, the only departure from product thinning is the
    multiplicity excess (J(S)), and

    \[
       0\le J(S)\le\sum_{\{u,v\}\subseteq S}d(u,v).              \tag{0.3}
    \]

2.  At time zero every repaired edge (e) satisfies

    \[
       \sum_{\{u,v\}\subseteq e}d(u,v)
          \le {3+o(1)\over m}R.                                \tag{0.4}
    \]

    Consequently one compensated bite has, for the **virtual** residual
    degree (the number of edges through (v) whose other vertices survive),

    \[
       \mathbb E d^*(v)
        =d(v)q^r\bigl(1+O(\gamma/m^2)\bigr).                   \tag{0.5}
    \]

    Together with the already proved owner width-two influence bound, the
    same bite has, for every owner (X) and (0<\eta\le1),

    \[
      \Pr\left(\left|d^*(X)-\mathbb E d^*(X)\right|>
                         \eta d(X)q^r\right)
       \le 2\exp\left[-c_z{m^2\eta^2\over\gamma+\eta}\right]   \tag{0.6}
    \]

    as long as the current density is at least a fixed (z>0), the current
    degrees are on a common scale, and the scaled versions of (0.4) and
    the owner width-two bound hold.  The constant in (0.6) may depend on
    (z), but not on (m).  This (m^2)-exponent is not proved for current
    roots from those hypotheses alone.  For roots they imply only an
    (m)-scale exponent unless a separate root--path influence estimate is
    assumed; the superpolynomial time-zero pair formula does not
    automatically scale in an endogenous residual.

3.  The earlier exception clause, requiring exceptional owners to touch
    only (o(N)) roots, is unnecessarily strong.  The correct quantity is
    their **root-link weight**.  For every owner set (B), deleting all
    edges meeting (B) causes total root-degree loss at most

    \[
                         \sum_{X\in B}d(X).                     \tag{0.7}
    \]

    Hence (B) is harmless whenever

    \[
                         \sum_{X\in B}d(X)=o(NR).                \tag{0.8}
    \]

    In the near-regular regime it is enough that
    (|B|=o(W/m)=o(N)).  The support-reachable family in
    `MATH_THEOREM_RPRN_REACHABLE_EXCEPTIONAL_LINK_COUNTEREXAMPLE_20260726.md`
    has size (Wm^2/\binom{m+H}{H}=o(W/m^C)) for every fixed (C), so it
    does not obstruct (0.8), despite statically containing an owner above
    almost every root.

The waste arithmetic closes the finite-density problem once the path
influence **and near-regular degree scales** regenerate.  With, for example,

\[
              \gamma={1\over\log m},\qquad
              \eta={1\over\sqrt{\log m}},                       \tag{0.9}
\]

there are (O_z(m\log m)) bites, and, conditional on that trajectory
regularity, the aggregate collision and compensation waste is (o(N)).
The one-bite owner failure bound in (0.6) is at most
\(2\exp[-c m^2/\sqrt{\log m}]\).  A union bound with the displayed
(\eta), however, does not control the accumulated multiplicative degree
drift over all bites.  Such cumulative control must either be proved by a
stopped martingale argument or included in the regeneration hypothesis.

The first missing bridge observable is the two-path count

\[
 b_X(e,g):=
 \bigl|\{f:X\in f,\ f\cap e\ne\varnothing,\ f\cap g\ne\varnothing\}\bigr|.
                                                                  \tag{0.10}
\]

Concentration of the next residual influence (a_X^*(e)) requires scaled
maximum and summed-square control of (b_X(e,g)), together with the
analogous compensation-coin sensitivities.  Concentration of those
quantities leads to three-path counts, and so on.  The complete static
codegree spine is consistent with such a hierarchy, but the hierarchy and
the cumulative degree martingale have not been proved along the endogenous
trajectory.  This is a smaller and more accurately weighted target than
`RPRN(z)`, but it remains a theorem, not bookkeeping.

## 1. The wasteful compensated bite

Let ({\cal H}=(V,{\cal E})) be a current residual repaired-ring
catalogue.  Its two vertex shores are roots and owners.  Assume only for
this section that all degrees are positive.

Independently mark every (e\in{\cal E}) with probability (p).  Let
\({\cal M}\) be the marked edges which meet no other marked edge.  Then
\({\cal M}\) is a matching.  Put

\[
 C=\{v:\text{(v) lies in at least one marked edge}\}.
\]

Unlike the ordinary isolated bite, delete all of (C), not merely the
vertices of ({\cal M}).  This makes every collision an explicitly charged
waste event.

For (v\in V), write

\[
 h_v=\Pr(v\in C)=1-(1-p)^{d(v)},\qquad
 \theta=\max_v h_v,\qquad q=1-\theta.                          \tag{1.1}
\]

Independently of the marks, attach to every vertex a compensation coin
with deletion probability

\[
 c_v={\theta-h_v\over1-h_v}.                                   \tag{1.2}
\]

Delete a vertex if it is in (C) or its compensation coin succeeds.
Every vertex then survives with probability exactly (q).

### Lemma 1.1 (exact joint survivor law)

For every (S\subseteq V), (0.2) holds.

#### Proof

Let ({\cal E}(v)) be the star of (v).  No vertex of (S) is hit by a
mark precisely when no member of
\(\bigcup_{v\in S}{\cal E}(v)\) is marked.  The marks and compensation
coins are mutually independent, so

\[
 \Pr(S\subseteq V^*)
 =(1-p)^{|\cup_{v\in S}{\cal E}(v)|}
   \prod_{v\in S}(1-c_v).
\]

Equation (1.2) gives

\[
 1-c_v={q\over1-h_v}={q\over(1-p)^{d(v)}}.
\]

Substitution proves (0.2).  Finally an edge counted (j\ge1) times in
\(\sum_{v\in S}d(v)\) contributes (j-1\) to (J(S)), and at least
\(j-1\) to \(\binom j2\).  Summing over catalogue edges proves (0.3).
\(\square\)

This identity is the main advantage of wasting every touched vertex.  No
conditioning on which marked edges were isolated appears in the residual
law.

## 2. Internal pair mass of one repaired path

We verify (0.4) in the complete repaired catalogue.  The owner--owner
pair formula is

\[
 {d(X,Y)\over D}
 ={2b_k(s)\over r\binom ms^2}\le {2\over\binom ms^2}
 \qquad(1\le s<H),                                     \tag{2.1}
\]

where (s=d_J(X,Y)).  In a retained phase path, at most (r) unordered
owner pairs have any prescribed start separation (s).  Therefore the
contribution from (1\le s<H) is at most

\[
 2rD\sum_{s=1}^{H-1}{1\over\binom ms^2}
 ={2+o(1)\over m}D.                                    \tag{2.2}
\]

Pairs at distance (H) contribute at most

\[
 r^2D\,{m-H+1\over\binom mH^2}=o(D/m).                \tag{2.3}
\]

No owner pair at greater Johnson distance occurs in one catalogue edge.
Since (D=\rho R\), (2.2)--(2.3) are at most
\((2+o(1))R/m\).

For a root--owner pair (A\subset X),

\[
 {d(A,X)\over R}={r\over\binom{m+H}{H}}.               \tag{2.4}
\]

There are (r) such pairs in one edge, so their total is

\[
 {r^2R\over\binom{m+H}{H}}=o(R/m).                     \tag{2.5}
\]

Equations (2.2)--(2.5) prove (0.4).

### Corollary 2.1 (one-bite expectation)

Suppose the scaled version of (0.4) holds in the current residual, with
(R_t) in place of (R), and suppose its vertex degrees are
((1+o(1))R_t).  Then, uniformly in (v),

\[
\mathbb E d^*(v)=d(v)q^r(1+O(\gamma/m^2)).
\]

Here (d^*(v)) is the virtual residual degree

\[
 d^*(v):=|\{f\ni v:f\setminus\{v\}\subseteq V^*\}|.     \tag{2.6}
\]

On the event (v\in V^*) this is the ordinary degree of (v) in the
induced residual.  Formula (0.5) is an unconditional statement about the
virtual variable.  Conditioning on (v\in V^*) changes its mean by only
the same relative (O(\gamma/m^2)) term: apply (0.2) to (S=f) and divide
by (q), observing that the additional multiplicity excess is at most
\(\sum_{u\in f\setminus\{v\}}d(u,v)=O(R_t/m)\).

#### Proof

For each (f\ni v), apply Lemma 1.1 to
(S=f\setminus\{v\}).  Equations (0.3)--(0.4) and
\(-\log(1-p)\le2p\) give

\[
 1\le {\Pr(f\setminus\{v\}\subseteq V^*)\over q^r}
 \le\exp\left(O\left(p{R_t\over m}\right)\right)
 =1+O(\gamma/m^2).
\]

Sum over (f\ni v). \(\square\)

## 3. One-bite concentration at growing uniformity

For a current owner (X) and an edge (g), define the virtual influence

\[
 a_X(g)=\bigl|\{f:X\in f,\ (f\setminus\{X\})
                     \cap(g\setminus\{X\})\ne\varnothing\}\bigr|.
                                                                  \tag{3.1}
\]

At time zero the width-two argument in the repaired catalogue gives

\[
                  a_X(g)\le {C\over m^2}D                    \tag{3.2}
\]

also when (X\in g): in that case sum the pair links from (X) to the
other vertices of the same repaired path.  Equations (2.1)--(2.5) give
the same bound, with a different absolute (C).  In a later residual,
(3.2) is a regeneration hypothesis, not a consequence of the time-zero
calculation.

Moreover, reversing the conflict count gives

\[
                  \sum_g a_X(g)\le D(R+rD)=O(mD^2).          \tag{3.3}
\]

Changing one mark bit at (g) changes the virtual residual degree
(d^*(X)) by at most (a_X(g)).  Changing the compensation coin at a
vertex (Y) changes it by at most (d(X,Y)).  The Bernoulli variance
proxy is consequently

\[
\begin{aligned}
 V_X
 &\le p\sum_g a_X(g)^2+\sum_Yc_Yd(X,Y)^2\\
 &\le {C\gamma\over m^2}D^2,                              \tag{3.4}
\end{aligned}
\]

where (3.2)--(3.3) handle the first term, and

\[
 \sum_{Y\ne X}d(X,Y)^2
 \le \Delta_2\sum_Yd(X,Y)
 \le {C D\over m^2}\,Dr=O(D^2/m)                       \tag{3.5}
\]

handles the compensation term; here (c_Y=O(\gamma/r)).

The Bernstein bounded-difference inequality for independent Bernoulli
coordinates, with maximum change (CD/m^2), now gives

\[
 \Pr(|d^*(X)-\mathbb E d^*(X)|>\eta D)
 \le2\exp\left[-c{m^2\eta^2\over\gamma+\eta}\right].    \tag{3.6}
\]

At a fixed residual density (z), (d^*(X)\asymp_z D) within one bite,
so (3.6) is (0.6).  The same conclusion holds conditionally on
(X\in V^*) after dividing the failure probability by (q=1-o(1)) and
absorbing the mean shift described after (2.6).

The corresponding claim for a root does **not** follow at the same scale
from (0.4) and the owner bound (3.2).  If (A) is a root, those hypotheses
give only

\[
 a_A(g):=|\{f:A\in f,\ (f\setminus\{A\})
                    \cap(g\setminus\{A\})\ne\varnothing\}|
       \le {C\over m}R_t.                               \tag{3.6a}
\]

Indeed, sum (d(A,Y)) over the at most (r) owners (Y) of (g), and use
(3.2) on an edge containing (A,Y) to bound each nonzero pair link by
(CR_t/m^2).  Reversing incidences then yields

\[
 \Pr(|d^*(A)-\mathbb E d^*(A)|>\eta R_t)
 \le2\exp\left[-c{m\eta^2\over\gamma+\eta}\right].     \tag{3.6b}
\]

At time zero, (2.4) gives a much stronger root bound.  It cannot be used
at a later time merely by replacing (R) with (R_t), because restriction
can increase the normalized root--owner links.  An (m^2)-scale root tail
therefore requires a separately regenerated bound
(a_A(g)=O(R_t/m^2)).  The weaker (3.6b) is still enough to show that the
*fraction* of bad roots in one of polynomially many rounds is (o(1)); it
is not enough for the all-root union bound claimed for owners.

The owner proof of (3.6) is completely uniform in (r\sim m).  In
particular, with (0.9), a union bound over all owners and over
(O_z(m\log m)) rounds is harmless if (0.4) and (3.2) regenerate.  This is
only a one-round deviation screen; it does not by itself bound the sum of
the accepted relative deviations over (O_z(m\log m)) rounds.

## 4. Accepted matching versus waste

Let (n(e)) be the number of other current edges meeting (e).  Degree
regularity and (0.4) give

\[
 n(e)=\sum_{v\in e}(d(v)-1)+O(R/m)
      =(1+o(1))rR.                                        \tag{4.1}
\]

Hence a fixed edge is an isolated mark with probability

\[
 p(1-p)^{n(e)}
 ={\gamma e^{-\gamma}+o(\gamma)\over rR}.              \tag{4.2}
\]

Put (\beta=\gamma e^{-\gamma}).  A root is matched in one bite with
probability

\[
                         {\beta+o(\gamma)\over r},        \tag{4.3}
\]

whereas its total deletion probability is

\[
 \theta={\gamma+o(\gamma)\over r}.                       \tag{4.4}
\]

Thus the fraction of deleted roots charged to collision or compensation
waste is

\[
 {\theta-\beta/r\over\theta}
=1-e^{-\gamma}+o(1)=O(\gamma).                          \tag{4.5}
\]

Conditional on the displayed current near-regularity, these counts
concentrate, uniformly for growing (r).  Indeed, expose the
mark bits one at a time.  Changing one bit changes the number of isolated
marked edges by at most (r+2): besides the toggled edge, at most one
previously isolated marked edge can be lost through each vertex of it.
The sum of the Bernoulli variance proxies is therefore at most

\[
 |{\cal E}|p(r+2)^2=O(\gamma Nr).
\]

The mean number of isolated marks is
((\beta+o(\gamma))N/r).  Bernstein's inequality consequently gives

\[
 |{\cal M}|={\beta+o(\gamma)\over r}N                 \tag{4.5a}
\]

with probability (1-o(1)), since (N) is exponential in (m).  The number
of vertices hit by marks and the number deleted by compensation satisfy
the same bounded-difference estimate (one mark changes either count by at
most (r+1)); ordinary Chernoff applies to the independent compensation
coins.  Thus (4.3)--(4.5) hold simultaneously as actual one-bite counts,
not only in expectation.

The owner shore has the same common deletion probability after
compensation.  Provided the root and owner degree scales remain in their
initial ratio up to (1+o(1)), the additional owner compensation caused by
\(1-\rho=O((H+k)/m)\) has aggregate relative cost
\(O_z((H+k)/m)=o(1)\) down to any fixed density (z).

If the bite can be regenerated with uniform near-regularity until common
survivor density (z), then
the union of its isolated marked edges is a matching (later bites occur
inside earlier survivor sets), and

\[
 \begin{aligned}
 \#\{\text{unmatched roots}\}
   &\le zN+O(\gamma N)+o(N),\\
 \#\{\text{wasted owners}\}
   &\le O((\gamma+(H+k)/m)W)+o(W).                    \tag{4.6}
 \end{aligned}
\]

Thus (4.6) is an exact ledger consequence of the stated trajectory
hypotheses, not an unconditional concentration theorem.  Taking
(\gamma\to0) proves the desired fixed-(z) statement under those
hypotheses.  Taking a
slow diagonal (z=z(m)\to0) then misses (o(N)) roots, which by the exact
packing ledger leaves (o(W)) owners.

## 5. Weighted quarantine is the correct exception notion

### Lemma 5.1 (root-link weighted quarantine)

Let (B) be any owner set in any residual catalogue.  Delete all catalogue
edges meeting (B).  Then

\[
 \sum_A\bigl(d(A)-d_{-B}(A)\bigr)
 \le\sum_{X\in B}d(X).                                  \tag{5.1}
\]

Consequently, for every (\tau>0), the number of roots losing more than
\(\tau R_t\) options is at most

\[
             {\sum_{X\in B}d(X)\over\tau R_t}.           \tag{5.2}
\]

#### Proof

Every deleted catalogue edge is counted at least once on the right of
(5.1), once for each of its owners in (B), and exactly once on the left,
at its unique root.  Markov's inequality gives (5.2). \(\square\)

If (d(X)=O(R_t)), (N_t\asymp W_t/m), and
(|B|=\delta_mW_t), (5.2) is (o(N_t)) as soon as

\[
                         m\delta_m=o(1).               \tag{5.3}
\]

Thus a per-owner bad probability
\(\exp[-c m^2/\sqrt{\log m}]\), or even \(\exp[-cm]\), is far more than
enough through polynomially many rounds.  Static containment of one bad
owner above a root is irrelevant; the root loses only the corresponding
pair-link, not its whole star.

For the reachable construction, (\delta_m=m^2/\binom{m+H}{H}\), and
(m^C\delta_m=o(1)) for every fixed (C).  This proves the assertion in
Section 0 that the construction is harmless under the weighted criterion.

## 6. The remaining bridge and cumulative-drift gates

The first new nonhereditary sensitivity in trying to regenerate the owner
influence occurs at the following place.  For a surviving edge (e) and
surviving owner (X\notin e), put

\[
 a_X^*(e)=|\{f\in{\cal H}^*:X\in f,\ f\cap e\ne\varnothing\}|.
\]

Up to constants depending on the fixed one-bite density, its expectation
is at the desired scale

\[
             \mathbb E[a_X^*(e)\mid X\cup e\subseteq V^*]
             \asymp q^{r-1}a_X(e),                       \tag{6.1}
\]

because at least one intersection vertex is already conditioned to
survive (terms with multiple intersection vertices only change the
one-bite constant).  To concentrate (6.1), however, changing the mark bit
at (g) can alter
(a_X^*(e)) by as much as

\[
 b_X(e,g)=
 |\{f:X\in f,\ f\cap e\ne\varnothing,\ f\cap g\ne\varnothing\}|.
                                                               \tag{6.2}
\]

The time-zero path geometry suggests, away from overlapping exceptional
configurations,

\[
             b_X(e,g)\lesssim {1\over m^2}a_X(e)          \tag{6.3}
\]

for disjoint (X,e,g), but neither (6.3) in every endogenous residual nor
the required summed-square estimate has been proved.  Compensation coins
also require the analogous count with a prescribed vertex in place of
(g).  Iterating the same argument leads to the (j)-path bridge counts

\[
 B_X(e_1,\ldots,e_j)
 =|\{f:X\in f,\ f\cap e_i\ne\varnothing\ (1\le i\le j)\}|. \tag{6.4}
\]

The static all-order codegree spine rules out a bounded projective-plane
obstruction and is compatible with a factor (m^{-2}) per additional
transverse path.  It does not by itself prove that (6.4) remains dispersed
after previous bites.  Conversely, the support-reachable exceptional-link
construction deliberately concentrates precisely such transverse bridge
counts.

This motivates the structural part of the corrected finite-density
target.  It is a proposed sufficient route to (6.6b), not a proof of
`WBR+(z)` or a claim that the single maximum bound (6.3) alone suffices.

### WBR+(z) (full weighted trajectory regeneration)

For fixed (z>0), say that `WBR+(z)` holds if, with probability (1-o(1)),
the wasteful compensated trajectory down to common survivor density (z)
admits owner quarantines (B_t) satisfying

\[
       \sum_t {\sum_{X\in B_t}d_t(X)\over N_tR_t}=o(1), \tag{6.5}
\]

and, after deleting the edges meeting those owners and discarding roots
whose cumulative normalized quarantine loss is nonnegligible, a core on
which, uniformly at every bite,

\[
 \begin{gathered}
 d_t(v)=(1+o(1))R_t,\qquad \max_vd_t(v)=O_z(R_t),       \tag{6.6a}\\
 \max_e\sum_{\{u,v\}\subset e}d_t(u,v)
       \le {C_z\over m}R_t,
 \qquad
 \max_{X,e}a_{X,t}(e)\le {C_z\over m^2}d_t(X).         \tag{6.6b}
 \end{gathered}
\]

Here (v) ranges over the nonexceptional active roots and owners (the
initial owner/root degree ratio is (1-o(1)), so one common scale is
legitimate).  Condition (6.6a) includes cumulative degree control; it is
not claimed to follow in this note by union-bounding the one-bite estimate.
If one wants the (m^2)-tail for roots as well, the additional root
influence bound following (3.6b) must also be included, but that stronger
tail is not needed once (6.6a) is assumed.

Only outcomes on the actual random trajectory are quantified over; no
claim is made for every support-reachable residual.

### Theorem 6.1 (finite density from WBR+)

If `WBR+(z)` holds for every fixed (z>0), then the repaired promotion-ring
owner hypergraph has a matching missing (o(N_H)) roots and leaving
(o(W)) owners.

#### Proof

The degree regeneration needed in the waste computation is (6.6a), while
(0.2)--(0.6) give its audited one-bite owner calculation.  To see that
the quarantines cost only (o(N)) roots, put (\varepsilon_m) equal to the
left side of (6.5), sum (5.1) after division by (R_t), and discard roots
whose cumulative normalized loss exceeds (\sqrt{\varepsilon_m}); Markov
costs at most (\sqrt{\varepsilon_m}N=o(N)).  Run with (0.9); (4.6) gives,
for fixed (z), a
matching missing at most (zN+o(N)) roots.  Diagonalize through
(z=1,1/2,1/3,\ldots\) sufficiently slowly.  The missed-root fraction is
then (o(1)), and the exact leave identity

\[
                       W-rN+rs
\]

from the repaired-ring packing ledger is (o(W)). \(\square\)

## 7. Status

Proved in this note:

* the exact compensated joint-survival identity (0.2);
* the internal pair-mass estimate (0.4);
* the virtual one-bite expectation and owner concentration calculations
  (0.5)--(0.6), under the scaled current degree and influence hypotheses;
* the matching-versus-waste ledger (4.6), conditional on uniform
  trajectory near-regularity;
* the weighted quarantine lemma (5.1)--(5.3); and
* `WBR+(z)` implies an (o(N_H))-root, (o(W))-owner leave.

Not proved:

* `WBR+(z)` for the endogenous compensated trajectory, including the
  cumulative near-regularity condition (6.6a);
* the maximum, summed-square, and compensation versions of the two-path
  bridge estimate after prior bites;
* an (m^2)-scale root tail without an additional regenerated root--path
  influence bound; or
* the desired near-perfect rooted matching unconditionally.

The main gain over the earlier formulation is conceptual and quantitative:
finite-density matching does not require every exceptional owner to have a
small static containment neighbourhood, and collision waste is not a
barrier.  The remaining work is transverse bridge-energy regeneration
plus cumulative degree control; the one-bite calculation alone does not
supply either trajectory theorem.

## 8. Scope: why this does not give the CCTPF rate

There are two different root-leave requirements in the current project and
they must not be merged.

For the repaired owner hypergraph, a matching missing (s) roots leaves

\[
                         W-rN+rs
\]

owners.  Since (rN=(1-o(1))W), the required conclusion is exactly
(s=o(N)).  Therefore a theorem down to every fixed density (z), followed
by an arbitrarily slow diagonal (z=z(m)\to0), is sufficient.

For the common-core tight-path configuration hypergraph (CCTPF), the exact
synchronized hole identity is

\[
             \mathfrak H=\Delta+k(N-\nu),\qquad
             k=(\sqrt\pi+o(1))m^{3/2},\qquad W\asymp mN.
\]

Consequently CCTPF requires

\[
                         N-\nu=o(N/\sqrt m).             \tag{8.1}
\]

A separate fixed-(z) theorem gives no quantitative rate with which to take
(z\to0), so it does not imply (8.1).  In particular, saying that the same
uncovered root is shared across all ranks does not save another factor
(\sqrt m): that synchronization is already counted exactly by the factor
(k) in the displayed identity.

There is also a local geometric difference.  A repaired owner edge has
internal normalized pair mass (O(1/m)), as in (0.4).  A CCTPF edge has a
vertical-spine normalized pair mass (\Omega(\sqrt m)).  Hence the primitive
survivor identity (0.2) still holds for CCTPF, but its small-correlation
consequence (0.5) does not: the vertical spine must first be contracted and
treated as one structured conflict.  Thus neither classical
Pippenger--Spencer nor the present owner-only wasteful bite supplies an
(o(N/\sqrt m)) CCTPF leave.
