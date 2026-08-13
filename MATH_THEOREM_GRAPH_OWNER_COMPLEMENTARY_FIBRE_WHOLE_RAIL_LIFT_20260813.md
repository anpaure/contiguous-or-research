# A graph-owner identity lifts functorially to a biresident whole-rail identity

Date: 2026-08-13  
Status: proved local theorem; structured-leave consequence only  
Source audited: `/Users/amir.nuriyev/.codex/attachments/92d98fcf-75a1-4de4-8d0b-3216490f0909/pasted-text.txt`  
Source SHA-256: `d1d1432d1c31c01103a90aa21daf7f2d6d6927b497b97ddf5075772c04f3f94f`

## 1. Statement

Let

\[
 q\ge 2,\qquad |D|=R-2q,\qquad |V|=2q+2,
\]

where `D` and `V` are disjoint subsets of `[k]`.  For each graph edge
`e` of the complete graph on `V`, put

\[
 \Omega(e)=D\cup(V\setminus e).                 \tag{1.1}
\]

Thus `Omega(e)` has rank `R`.  Assume

\[
 R\ge 3q,\qquad k-R\ge q+2.                    \tag{1.2}
\]

Choose a `q`-set `W` in `D`, choose a fresh `q`-set

\[
 Z\subseteq [k]\setminus(D\cup V),
\]

and cyclically order

\[
 T=W\sqcup Z=(w_0,\ldots,w_{q-1},z_0,\ldots,z_{q-1}). \tag{1.3}
\]

For `j` modulo `2q` and `0 <= ell <= 2q`, let `I_j^ell` be the cyclic
interval of length `ell` in this order.  In particular,

\[
 I_0^q=W.                                       \tag{1.4}
\]

For a graph edge `e`, define

\[
 C_e=(D\setminus W)\cup(V\setminus e),          \tag{1.5}
\]

and the period-`2q` pure rail

\[
 \mathcal B(e)=
 \left\{,O_{e,j}=C_e\cup I_j^q:j\in\mathbb Z_{2q}\,\right\}. \tag{1.6}
\]

Then:

1. `C_e` has size `R-q`, every `O_{e,j}` has rank `R`, and consecutive
   owners are Johnson adjacent.  Thus `B(e)` is a literal closed pure
   rank-`R` rail of period `2q`.

2. Every active coordinate has cyclic owner trace `1^q 0^q`.  Hence the
   rail has both positive and zero residence exactly `q`; all core
   coordinates are constant.  Its trace boundary is zero.

3. The original graph owner is a distinguished owner of its fibre:

   \[
   O_{e,0}=C_e\cup W=\Omega(e).                  \tag{1.7}
   \]

4. If `e` and `f` are distinct, then `B(e)` and `B(f)` are
   owner-disjoint.  More strongly, for every proper width
   `1 <= ell <= 2q-1`, all targets

   \[
   P_{e,j}^{\ell}=C_e\cup I_j^\ell              \tag{1.8}
   \]

   are distinct as `(e,j,ell)` varies.  In particular, both immediate
   palettes (`ell=q-1` and `ell=q+1`) are globally simple across an
   arbitrary union of fibres.

5. For an edge family `F`, put

   \[
   \mathcal B(F)=\bigsqcup_{e\in F}\mathcal B(e). \tag{1.9}
   \]

   If `F_1=F_0 disjoint-union {h}`, then there is a literal owner identity

   \[
   \mathcal B(F_1)=\mathcal B(F_0)\sqcup\mathcal B(h), \tag{1.10}
   \]

   and, at every proper interval width `ell`, the corresponding deck
   identity is

   \[
   \mathcal P_\ell(\mathcal B(F_1))
   =\mathcal P_\ell(\mathcal B(F_0))
    \sqcup\mathcal P_\ell(\mathcal B(h)).        \tag{1.11}
   \]

   The full-union target also obeys the same componentwise identity.
   Therefore the construction is functorial for owner and all interval-deck
   currents; it does not merely preserve point degrees.

We call (1.10) the **complementary-fibre whole-rail lift** of the graph-edge
identity `F_1=F_0 disjoint-union {h}`.

## 2. Proof

The core calculation is

\[
 |C_e|=(R-2q-q)+2q=R-q.                           \tag{2.1}
\]

The hypotheses in (1.2) are exactly what is needed for the choices made
above: `R-2q >= q` supplies `W`, while

\[
 |D\cup V|=(R-2q)+(2q+2)=R+2
\]

and `k-(R+2) >= q` supplies `Z`.

A cyclic `q`-window in a `2q`-cycle changes to the next window by deleting
one point and inserting one point, so consecutive owners in (1.6) are
Johnson adjacent.  Every point of `T` occurs in precisely `q` consecutive
windows and is absent for the complementary `q` consecutive windows.
This proves legality, closure, and biresidence.  Equation (1.7) follows
from `I_0^q=W`.

To prove simplicity, observe that

\[
 O_{e,j}\cap V=V\setminus e.                     \tag{2.2}
\]

Hence an owner determines its graph edge `e`.  Having recovered `e`, its
intersection with `T` is the cyclic `q`-interval `I_j^q`, and proper cyclic
intervals have distinct starts.  This recovers `j`.

The same argument works for (1.8).  Equality of two such targets first
gives equality of cardinalities and hence equality of `ell`; intersection
with `V` then recovers `e`, and intersection with `T` recovers the start
`j`.  This proves global proper-deck simplicity.  Equations (1.10) and
(1.11) are now disjoint-union identities, not signed cancellations.
This proves the theorem.

## 3. Application to the star--cycle graph absorber

Use the notation of the audited attachment.  There

\[
 H=D\cup L,\qquad V=L\cup\{u,v\},\qquad \Omega(uv)=H, \tag{3.1}
\]

and the explicit graph satisfies

\[
 S=G\sqcup\{uv\},\qquad |E(G)|=q(q+2).            \tag{3.2}
\]

Apply the construction edge by edge.  It gives the exact common-reserve
identity

\[
 \boxed{\mathcal B(S)=\mathcal B(G)\sqcup\mathcal B(uv).} \tag{3.3}
\]

Both shores are disjoint unions of legal, owner-simple, biresident,
period-`2q` pure rails.  The difference is one whole legal rail, and that
rail contains the original exceptional owner:

\[
 H=O_{uv,0}\in\mathcal B(uv).                     \tag{3.4}
\]

The lifted common reserve has

\[
 |\mathcal B(G)|=2q\,q(q+2)=2q^2(q+2)             \tag{3.5}
\]

owners, and the residual rail has `2q` owners.  Its point-degree vector is

\[
 2q\,\mathbf 1_{C_{uv}}+q\,\mathbf 1_T,           \tag{3.6}
\]

where

\[
 C_{uv}=(D\setminus W)\cup L,qquad
 H=C_{uv}\cup W.                                  \tag{3.7}
\]

The old short star and cycle periods `q+1` and `q+2` are no longer used as
rail periods.  Their zero-residence defect is therefore removed rather
than patched.  Indeed, (3.3) only needs the graph identity `S=G+uv`; the
star/cycle decompositions are useful for obtaining that identity but are
not used in the vertical rail factorization.

The attachment assumes `c >= 2q`, which is equivalent to `R >= 3q` and
therefore supplies `W`.  Its displayed condition `k-R >= 3` does **not**
by itself supply the fresh set `Z`.  The fibre lift needs the stronger

\[
 k-R\ge q+2.                                      \tag{3.8}
\]

This does hold in the intended central asymptotic range, but it must be
stated explicitly in any finite theorem using this lift.

## 4. Structured-leave absorber corollary

Suppose a cover-down theorem produces an owner leave which is a disjoint
union of at most `s` fibres of the form `B(h)`, with their proper interval
decks interpreted componentwise.  Then (1.10) fills or removes each such
leave by switching between the corresponding two graph-edge shores.  The
terminal object is a union of at most `s` complete legal biresident rails,
not a collection of `2qs` unrelated owner defects.

Consequently, any compiler whose terminal alphabet charges one bounded
cost per **complete rail component** rather than per owner turns a bounded
number of these structured leaves into `O(s)` additive cost.  This is a
rigorous structured-leave reduction.  It is not an unconditional
`B(k)+O(1)` theorem because no cited result currently proves either that
the global leave has this form or that the compiler charges a whole rail
as one terminal object.

## 5. Exact scope and nonclaims

The theorem proves more than a point-degree lift: it preserves literal
owners, owner adjacency, closure, positive and zero residence, and every
proper interval-deck identity.  It also gives a distinguished copy of the
original graph owner in its fibre.

It does **not** prove any of the following.

1. It does not retain a singleton residue.  It replaces the one-owner
   residue `H` by the whole rail `B(uv)`, containing `H` and `2q-1`
   auxiliary owners.
2. It does not by itself match arbitrary compulsory socket, cap, Ferrers,
   protected-history, or occurrence-labelled tickets between the two
   shores.  Such rows must be included in a later structured-leave
   compiler or supplied with compatible fibre decorations.
3. It does not prove a global packing of many such lifts.  Different lifts
   need graph and tag signatures chosen so that their owner and compulsory
   ticket sets are disjoint.
4. The reserve has `Theta(q^3)` owners.  When `q=Theta(sqrt(k))`, exposing
   every one of them costs `Theta(k^(3/2))`.  This is too large for a theorem
   whose hypothesis literally bounds the *total* exposed bank by `o(k)`, but
   it is still `2^{o(k)}`.  It may therefore lie inside a subexponential
   protected-factor theorem if the relevant local exposure parameters are
   separately shown to be `o(k)`.  The scalar bank size alone decides neither
   applicability nor failure of such a theorem.
5. The period is exactly `2q`.  The theorem supplies a bare resident pure
   rail, not automatically a port-rich `2q+2` switch rail.

Within these limits, (3.3) is an unconditional functorial lift of the
graph absorber to legal biresident rails and is the strongest currently
proved positive replacement for the short-period star/cycle factors.

## 6. General-period extension

The value `2q` is not required for the vertical construction.  Let

\[
 m\ge2q,
 \qquad k-R\ge m-q+2.                              \tag{6.1}
\]

Keep a `q`-set `W \subset D`, choose instead a fresh set

\[
 |Z|=m-q,
 \]

and cyclically order `T=W \sqcup Z` with `W` as its first `q` consecutive
points.  With the same core

\[
 C_e=(D\setminus W)\cup(V\setminus e),
\]

define

\[
 \mathcal B_m(e)=
 \{C_e\cup I_j^q:j\in\mathbb Z_m\}.               \tag{6.2}
\]

Every conclusion of Sections 1--2 holds with period `m`: the original
owner is the start-0 window, distinct edges and proper intervals are
recoverable, and every active trace has positive run `q` and zero run
`m-q >= q`.  The ambient inequality in (6.1) follows because the fresh
sector outside `D \cup V` has size `k-R-2`.

For graph families `F_1=F_0 \sqcup \{h\}` one therefore has

\[
 \mathcal B_m(F_1)
 =\mathcal B_m(F_0)\sqcup\mathcal B_m(h)            \tag{6.3}
\]

at the owner and every proper deck width.  The reserve and residual sizes
are respectively

\[
 m q(q+2),\qquad m.                                \tag{6.4}
\]

The exact point current of the residual rail is

\[
 m\,\mathbf1_{C_h}+q\,\mathbf1_T.                 \tag{6.5}
\]

Thus `m=2q+1` and `m=2q+2` are honest longer-period alternatives whenever
the corresponding one or two additional fresh labels are available.  This
extension is relevant because their auxiliary congruence classes differ
from that of period `2q`; it does not by itself solve the compound macro
current.

## 7. Optimality among disjoint componentwise biresident lifts

The whole-rail residual is not an avoidable inefficiency of this particular
clock.

### Proposition 7.1 (no singleton-preserving componentwise dilation)

Consider a positive graph-edge functor which replaces each graph edge `e`
by a nonempty, edge-private union `F(e)` of closed pure rails, and assume
the unions for distinct graph edges are owner-disjoint.  Suppose every
nonconstant toggle trace on every selected rail has positive and zero runs
of length at least `q`.  If

\[
 F(F_1)=F(F_0)\sqcup F(h)
 \qquad\text{whenever }F_1=F_0\sqcup\{h\},          \tag{7.1}
\]

then

\[
 |F(h)|\ge2q.                                      \tag{7.2}
\]

Consequently no such functor can lift a one-edge graph difference while
retaining a one-owner residual.  The period-`2q` complementary-fibre lift
attains the sharp lower bound (7.2).

#### Proof

A nonconstant coordinate on a closed pure rail of period `n` has one
positive run of length `q` and one zero run of length `n-q`.  Biresidence
therefore forces

\[
 n-q\ge q,
 \qquad\text{hence}\qquad n\ge2q.                  \tag{7.3}
\]

Every nonempty fibre contains at least one such rail, and a pure rail has
one distinct owner for each period position.  Thus its fibre has at least
`2q` owners.  Positivity and edge-private disjointness forbid cancelling
those auxiliary owners against another edge fibre.  Equation (7.1) makes
the residual for one added graph edge exactly `F(h)`, proving (7.2).
The construction in Sections 1--3 uses one period-`2q` rail per edge, so
equality holds. \(\square\)

This obstruction is deliberately scoped to disjoint componentwise positive
lifts.  A compound construction may beat it only by allowing different
edge gadgets to share and cancel a common reserve, or by absorbing the
resulting whole rail at a later cover-down stage.  Either mechanism is no
longer a functorial one-edge dilation.
