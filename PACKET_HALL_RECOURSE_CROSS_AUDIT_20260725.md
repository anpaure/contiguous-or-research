# Independent cross-audit of Packet Hall and common-threshold recourse

Date: 2026-07-25

Audited files:

- `PACKET_HALL_RECOURSE_20260725.md`;
- `PACKET_HALL_RECOURSE_AUDIT_20260725.md`.

Method: adversarial theorem-by-theorem rederivation, with particular
attention to quantifier order, the direction of every flow cut, and the
normalization by (t=W/n).  No computation, search, or external theorem is
used.

## 0. Verdict

\[
 \boxed{\text{PASS, with one minor domain clarification.}}
\]

The packetization, bounded-rank rounding, compressed dual, overload
transfer, fixed-window implication, and both common-threshold recourse
statements are mathematically correct.  The note does not hide a proof of
the fractional packet theorem and therefore does not overclaim MWB.

The only correction was editorial but logically useful: where the old
fractional multicover is introduced around (3.5), explicitly include

\[
 0\le x_E\le1.
\]

The proof of (3.6) uses this upper bound.  It was already stated immediately
after (3.5), is part of the earlier deletion LP, and is used correctly in
both the source and its self-audit.  I applied the clarification directly
to the source.  No theorem changes.

## 1. Binary owner incidences and survival packets

Fix a cyclic order on (n) distinct coordinates and a proper length
(1\le r<n).  Two different cyclic position intervals of length (r)
cannot give the same coordinate set: the coordinate labelling is a
bijection, so equality of label sets would imply equality of the two
position intervals.  A nonempty proper cyclic interval has no nonzero
translation fixing it.

Thus a wreath contributes either zero or one occurrence to a given
resource (a=(q,S)), and its owner object

\[
 \mathcal O_a=\{E\in F:E\text{ owns }S\}
\]

is an ordinary set.  Consequently, after deleting (B\subseteq F), the
residual load is exactly

\[
 \mu_q^{F\setminus B}(S)=|\mathcal O_a\setminus B|.
\]

For an integral quota (\beta(a)\ge0),

\[
 |\mathcal O_a\setminus B|\le\beta(a)
\]

if and only if (B) meets every (\bigl(\beta(a)+1\bigr))-subset of
(\mathcal O_a).  Both implications are exact:

- if too many owners survive, choose any (\beta+1) of them;
- if one such packet avoids (B), all its (\beta+1) owners survive.

Taking the union over every depth and target still uses one common set
(B), so no rankwise-gluing assumption enters.  Resource-labelled
parallel packets do not change the cover constraints, while retaining the
labels is necessary for the later resourcewise dual decomposition.

This verifies Theorem 2.1 and the identification

\[
 \tau(F,\beta)=\tau(\mathcal P(F,\beta)).
\]

## 2. Packet rank and threshold rounding

A balanced quota has value (c_q) or (c_q+1), so a nonempty packet has
size (c_q+1) or (c_q+2).  Hence

\[
 R(F,\beta)\le2+\max_qc_q.
\]

For (q\le A\sqrt m),

\[
 \log\frac{W}{N_q}
 =\frac{q(q+1)}m+O_A(m^{-1/2}),
\]

and therefore (c_q\le C_A) for each fixed (A), uniformly in large
(m).  The rank (R_A=C_A+2) is consequently a genuine constant only
after (A) is fixed.  The source preserves this quantifier order.

Let (x\) be a fractional packet cover and set

\[
 B=\{E:x_E\ge1/R\}.
\]

If a packet (P) avoided (B), every one of its at most (R) entries
would be strictly below (1/R), giving

\[
 \sum_{E\in P}x_E<|P|/R\le1,
\]

a contradiction.  Moreover, with nonnegative vertex costs,

\[
 \sum_{E\in B}w_E\le R\sum_Ew_Ex_E.
\]

This proves both the unweighted and weighted forms of

\[
 \vartheta\le\tau\le R\vartheta.
\]

The empty-packet convention (R=1) is harmless: then both optima are
zero.

## 3. Comparison with the old multicover relaxation

For one violating resource, put

\[
 h=|\mathcal O_a|,\qquad
 d=h-\beta>0,
\]

and let (P\subseteq\mathcal O_a) have size (\beta+1).  Then

\[
 |\mathcal O_a\setminus P|=d-1.
\]

For (x\in[0,1]^F), the old multicover inequality

\[
 \sum_{E\in\mathcal O_a}x_E\ge d
\]

therefore implies

\[
 \sum_{E\in P}x_E
 \ge d-\sum_{E\in\mathcal O_a\setminus P}x_E
 \ge d-(d-1)=1.
\]

Thus every feasible point of the bounded old deletion LP is a packet
cover, and

\[
 \vartheta\le\tau_{\rm frac}\le\tau.
\]

The bound (x_E\le1) is essential to this *pointwise feasible-set*
implication.  This is the minor display clarification noted in the verdict.
For example, without the box constraints, a weight larger than one on a
single shared owner can satisfy a multiunit row in a way that does not
cover all packets.  The source does invoke (x\in[0,1]^F), so its actual
argument is sound.

For one isolated resource, the packet system is the complete
(k)-uniform hypergraph with (k=\beta+1).  Symmetry gives

\[
 \vartheta=h/k,
 \qquad
 \tau=h-k+1=h-\beta.
\]

The old one-row fractional multicover optimum is also (h-\beta), so the
example ((h,\beta)=(3,1)) correctly proves strict weakening.

## 4. Order statistics and the prebalance ledger

For a fixed owner set (O) and (k=\beta+1), the minimum packet sum is
exactly the sum of the (k) smallest owner weights.  Hence all packet
constraints for this resource are equivalent to

\[
 \operatorname{Bot}_k(x;O)\ge1.
\]

Averaging the (\binom hk) packet inequalities counts each owner
(\binom{h-1}{k-1}) times and gives

\[
 \sum_{E\in O}x_E\ge\frac hk.
\]

When this is summed over all over-capacity resources in a window of
(K_A) depths, a wreath weight occurs at most (nK_A) times: one cyclic
order owns exactly (n) distinct targets at each proper length.  Thus

\[
 \sum_{a\in\mathcal V}\frac{h_a}{k_a}
 \le nK_A\|x\|_1.
\]

Since (h_a/k_a\ge1) and (k_a\le R_A),

\[
 |\mathcal V|\le nK_A\|x\|_1,
 \qquad
 \sum_{a\in\mathcal V}h_a
 \le R_AnK_A\|x\|_1.
\]

At the target scale
(\|x\|_1=o_A(t/\sqrt m)), with
(K_A=O_A(\sqrt m)) and (nt=W), both right sides are (o_A(W)).
There is no lost factor of (n), (m), or (A).

## 5. Compressed packet-flow dual: all cut directions

The ordinary packet-packing dual is

\[
 \max\sum_{a,P}y_{a,P}
 \quad\text{subject to}\quad
 \sum_{a,P\ni E}y_{a,P}\le1.
\]

For each resource define

\[
 Y_a=\sum_{P\in\mathcal P_a}y_{a,P},
 \qquad
 z_{a,E}=\sum_{P\ni E}y_{a,P}.
\]

Then

\[
 0\le z_{a,E}\le Y_a,
 \quad
 \sum_{E\in\mathcal O_a}z_{a,E}=k_aY_a,
 \quad
 \sum_az_{a,E}\le1.
\]

Conversely, for (Y_a>0), the vector (z_a/Y_a) belongs to the
hypersimplex

\[
 \{p\in[0,1]^{\mathcal O_a}:\sum p_E=k_a\},
\]

whose vertices are exactly incidence vectors of (k_a)-subsets.  A convex
decomposition therefore reconstructs the resource-labelled packet
weights.  The case (Y_a=0) forces (z_a=0) and is harmless.

For fixed (Y), form the flow network

\[
 s\to a\to E\to t
\]

with capacities (k_aY_a), (Y_a), and (1), respectively, and demand
that all (s\to a) arcs be saturated.  Let (X) be the resources and
(Z) the owners on the source side of a cut.  Its capacity is

\[
 \sum_{a\notin X}k_aY_a
 +\sum_{a\in X}|\mathcal O_a\setminus Z|Y_a
 +|Z|.
\]

Comparing this with total demand (\sum_ak_aY_a) yields exactly

\[
 \sum_{a\in X}
 Y_a\bigl(k_a-|\mathcal O_a\setminus Z|\bigr)
 \le |Z|.
\]

This verifies the cut direction in the source.  Conversely, every
(s)-(t) cut is specified by some pair ((X,Z)), so no cut class is
missing.  For fixed (Z), the maximizing (X) contains precisely the
resources with positive coefficient; zero coefficients are irrelevant and
negative ones are optimally omitted.  Hence the full cut family is
equivalent to

\[
 \sum_aY_a
 \bigl(k_a-|\mathcal O_a\setminus Z|\bigr)_+
 \le|Z|
 \qquad(Z\subseteq F).
\]

Real max-flow/min-cut supplies the required (z).  This is an LP identity,
not an assertion of integral flow, and the source states it at the correct
level.

## 6. Direct packet-cover-to-overload transfer

Fix the chosen balanced quotas.  They are admissible competitors in the
definition of (O_q(F)), so

\[
 O_q(F)\le
 \sum_{a\text{ at }q}(h_a-\beta(a))_+.
\]

Only (h_a\ge k_a=\beta(a)+1) contribute, and for them

\[
 h_a-\beta(a)=h_a-k_a+1\le h_a.
\]

Because (k_a\in\{c_q+1,c_q+2\}) and (c_q\ge1),

\[
 \frac{k_a}{c_q}\le3.
\]

It follows that

\[
 \sum_{q\le H}\frac{O_q(F)}{c_q}
 \le3\sum_{a\in\mathcal V}\frac{h_a}{k_a}.
\]

The averaged packet inequality and the (nH) owner-incidence count give

\[
 \sum_{q\le H}\frac{O_q(F)}{c_q}
 \le3nH\|x\|_1.
\]

This proof uses neither bounded rank nor a fixed window.  Since (W=nt),

\[
 \|x\|_1=o(t/H)
 \quad\Longrightarrow\quad
 \sum_{q\le H}O_q(F)/c_q=o(W).
\]

The scale is correct.

## 7. Fixed-window quantifiers and implication to MWB

For each *fixed* (A), suppose

\[
 \vartheta_A(F_{m,A})=o_A(t/\sqrt m).
\]

The constant (R_A) may depend arbitrarily on (A), but not on (m).
Threshold rounding produces one common deletion family with

\[
 |B|\le R_A\vartheta_A=o_A(t/\sqrt m).
\]

The residual (G=F\setminus B) is simultaneously dominated by the chosen
balanced quotas at all depths, while (F=G\sqcup B) is already an exact
completion.  This is precisely (HQ_A).  The previously audited
hard-quota charging theorem then gives fixed-window weighted overload
(o_A(W)), and only afterward does diagonalization let (A\to\infty)
slowly.

Equivalently, Theorem 3.3 applies directly because
(K_A=O_A(\sqrt m)):

\[
 3nK_A\,o_A(t/\sqrt m)=o_A(nt)=o_A(W).
\]

The existential equivalence

\[
 \exists(F,\beta):\tau=o(t/\sqrt m)
 \quad\Longleftrightarrow\quad
 \exists(F,\beta):\vartheta=o(t/\sqrt m)
\]

is valid at fixed (A): one direction is relaxation, and the other loses
only the fixed constant (R_A).  The witnesses may depend on (A) and
(m), exactly as fixed-window diagonalization permits.  The source never
uses this equivalence with a growing (A(m)).

## 8. Common-threshold recourse

Choose one threshold uniformly from ((0,1/R]) and set

\[
 z_E^{(j)}=\min\{x_E^{(j)},1/R\}.
\]

Every packet contains some coordinate at least
(1/|P|\ge1/R), so every allowed threshold hits every packet at every
time.  For each vertex,

\[
 \Pr(E\in B_j)=Rz_E^{(j)},
\]

and, because the *same* threshold is used at adjacent times,

\[
 \Pr(E\in B_j\triangle B_{j-1})
 =R|z_E^{(j)}-z_E^{(j-1)}|.
\]

Linearity of expectation proves the aggregate weighted
holding-plus-recourse bound.  Coordinatewise truncation is 1-Lipschitz, so
the untruncated (\ell^1) expression is a valid weaker right side.

For the pointwise version, every
(\theta\in[1/(2R),1/R]) still hits every packet and deterministically

\[
 |B_j(\theta)|\le2R\|x^{(j)}\|_1
\]

for every (j).  The threshold interval has length (1/(2R)), so

\[
 \Pr(E\text{ changes membership})
 \le2R|x_E^{(j)}-x_E^{(j-1)}|.
\]

One threshold attains the expected aggregate recourse bound, while all
pointwise holding inequalities hold for every threshold.  Thus (5.4) and
(5.5) hold simultaneously; there is no union-bound loss in (T).

For a finite exact-factor trajectory, extending each (x^{(j)}) by zero
to the union of all oriented wreath atoms is legitimate.  Since
(\theta>0), the rounded family remains inside (F_j).  The conclusion is
finite-time; no unsupported compactness passage to an infinite trajectory
is claimed.

## 9. Scope and remaining gate

The note proves only a constant-factor integrality and recourse theorem on
each fixed Gaussian window.  It does not construct an exact factor with a
small packet cover.  In fact, its necessary prebalance ledger shows that a
cover of the target size already forces (o_A(W)) total over-capacity
occurrence mass through the window.

The remaining statement is therefore genuinely the correlated
fractional-geometric assertion

\[
 \forall A<\infty\ \exists(F_{m,A},\beta_{m,A}):
 \vartheta(F_{m,A},\beta_{m,A})
 =o_A(t/\sqrt m).
\]

Only after this fixed-(A) family is proved may one diagonalize.  The
source respects these quantifiers and does not claim a direct rounding for
(A=A(m)\to\infty).

## 10. Final audit ledger

### Passed

1. Binary owner incidence and exact survival-packet equivalence.
2. Fixed-window bounded packet rank.
3. Weighted and unweighted (R)-threshold rounding.
4. Strict domination by the old bounded fractional multicover LP.
5. Exact bottom-(k) order-statistic compression.
6. Forced prebalance incidence and scale ledger.
7. Hypersimplex reconstruction and every direction of the compressed
   max-flow/min-cut dual.
8. Direct all-window overload transfer with normalization (W=nt).
9. Fixed-window (\mathrm{FSP}_A\Rightarrow HQ_A\Rightarrow MWB)
   implication and its diagonal quantifiers.
10. Aggregate and pointwise common-threshold recourse, including changing
    factor supports.

### Minor correction (applied)

The old multicover domain accompanying (3.5) now explicitly reads

\[
 x\in[0,1]^F.
\]

This domain was already used in the next sentence and in the proof, so the
correction is presentational, not substantive.

### Still open

The fixed-window fractional survival-packet theorem itself.  Nothing in
the source or either audit proves it, so neither MWB nor the final
coefficient-one theorem is claimed here.
