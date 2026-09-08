# Promotion rings at the critical top height: the one-hole owner factor, exact fractional flags, and the nested-tag gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or
external input is used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 q_0=\lceil m^{1/4}\rceil,
\]

and set

\[
 H=\left\lfloor\sqrt{m\log m}\right\rfloor,
 \qquad M=m+H,\qquad \lambda_q={W\over N_q}.
 \tag{0.1}
\]

For every top (U\in\binom{[2m]}M), Theorem 3.6 of
`MATH_THEOREM_EP_MULTISCALE_ROTOR_AND_CONTEXT_HALL_OBSTRUCTION_20260726.md`
gives an (M)-phase promotion ring.  The critical observation is

\[
 MN_H=W+O(WH/m),\qquad N_H=(1+o(1)){W\over m}.
 \tag{0.2}
\]

Consequently one promotion path per top costs only

\[
 2HN_H=O(WH/m)=o(W),\qquad
 N_H=o(W/H).
 \tag{0.3}
\]

This note gives a precise global formulation and settles its complete
fractional and owner-only local geometry.

1. There is an exact symmetric fractional **factor-compatible** solution:
   one cyclic frame per top, one contiguous active block, one tag-(H)
   phase, and the exact retained-SCD tag census
   
   \[
     N_d-N_{d+1}\quad(q_0\le d<H),\qquad N_H\quad(d=H).
   \]
   Every signed target at every depth (q_0\le q\le H) has fractional
   load exactly one.  At shallower depths the load is exactly
   (N_{q_0}/N_q), which is the correct one-baseline partial-SCD load.

2. Delete one phase from a ring and retain its other (M-1) middle
   owners.  In the augmented hypergraph whose vertices are tops and
   middle owners, these repaired rings have exact degrees

   \[
    D_U=M!,\qquad
    D_X={(m!)^2(M-1)\over(m-H)!},
    \qquad {D_X\over D_U}={M-1\over\lambda_H}=1+O(H/m).
    \tag{0.4}
   \]

   For two middle owners at Johnson distance (d), the normalized
   codegree is

   \[
    {D(X,Y)\over D_X}=
    \begin{cases}
     \displaystyle {2(M-2)\over(M-1)\binom md^2},&1\le d<H,\\[2mm]
     \displaystyle {(M-2)(m-H+1)\over
          (M-1)\binom mH^2},&d=H,\\[2mm]
     0,&d>H.
    \end{cases}
    \tag{0.5}
   \]

   Hence the maximum relative pair codegree is
   ((2+o(1))/m^2).

3. The owner-only fractional matching number is exactly

   \[
                         \boxed{\nu^*={W\over M-1}}.
   \tag{0.6}
   \]

   Thus there is no owner-side fractional or weighted Hall obstruction.
   For the exact truncated census, the number of full repaired rings
   required is

   \[
    K_0=\left\lfloor {N_{q_0}-N_H\over M-2}\right\rfloor,
   \tag{0.7}
   \]

   up to one partial terminal ring, and

   \[
    \boxed{
    {W\over M-1}-K_0=(1+o(1)){N_H\over\sqrt m}.}
   \tag{0.8}
   \]

   Formula (0.8) is the exact owner-rounding precision available from the
   deliberate (q_0=m^{1/4}) shallow leave.

4. No presently audited growing-uniformity nibble theorem supplies this
   matching.  For edge size (k=M), vertex census
   (V=W+N_H), and (D_{\min}=D_U),

   \[
    {k\Delta_2\log V\over D_{\min}}
      =4\log2+o(1),
   \tag{0.9}
   \]

   while the variable-rank Grable hypothesis requires (o(1)).  The
   newer full-codegree hierarchy also does not diagonalize at
   (k\asymp m).  The one-hole deletion therefore preserves the exact
   critical boundary of the full-cycle catalogue; it does not move the
   problem inside a black-box nibble range.

5. More importantly, even an owner matching is not the all-rank theorem.
   Conditional on fixed frames and distinct middle owners, the remaining
   problem is one nested two-sided transversal system.  At depth (q_0)
   every retained high-tag slot is already active, so a collision in its
   lower or upper (q_0)-trace cannot be repaired by changing tags.  The
   first unresolved coloured gate is therefore present before the deeper
   thresholds are assigned.

Thus the promotion-ring capacity coincidence is genuine and the natural
LP has no deficit.  The route is not constructed: the integral common-frame
selection and its nested two-sided trace transversals remain open.

## 1. Critical capacity

The exact ratio is

\[
 \lambda_q=\prod_{j=1}^q {m+j\over m-j+1}.
 \tag{1.1}
\]

Uniformly for (q=O(\sqrt{m\log m})), Taylor expansion gives

\[
 \log\lambda_q={q^2\over m}-{q^2\over2m^2}
  +O\left({q^4\over m^3}+{q\over m^2}\right).
 \tag{1.2}
\]

Since (H^2/m\le\log m), (1.2) gives

\[
 \lambda_H\le m\exp(o(H/m))<m+H=M
 \tag{1.3}
\]

for all sufficiently large (m).  It also gives

\[
 {M\over\lambda_H}=1+O(H/m),
 \tag{1.4}
\]

which proves (0.2).  At the inner cutoff,

\[
 {N_{q_0}\over W}
 =1-{1\over\sqrt m}+O(m^{-3/4}).
 \tag{1.5}
\]

In particular

\[
 {N_{q_0}\over N_H}<M
 \tag{1.6}
\]

and a top ring has enough slots for the retained-SCD census.

The additive choice of (H) matters for a literal full-ring packing, but
not for the statements here: (1.3)--(1.6) are the covering-side
calibration, and unused phases are allowed.

## 2. The global promotion-ring factorization target

Fix a directed cyclic frame

\[
 \pi_U=(c_0,\ldots,c_{M-1})
 \tag{2.1}
\]

on every top (U\in\binom{[2m]}M).  A phase (i), truncated to tag
(d_i\), owns at signed rank (m+r), (|r|\le d_i\),

\[
 C_{U,i}(r)
 =U\setminus
   \{c_{i+H+r},c_{i+H+r+1},\ldots,c_{i+2H-1}\}.
 \tag{2.2}
\]

The omitted cyclic interval has length (H-r).  At most one phase in a
top may have tag (H).

Call a selection a (\operatorname{PRSF}(q_0,H)) if:

* the active phases in every top form one cyclic interval (and hence one
  promotion path after one cut);
* exactly one active phase in every top has tag (H);
* the aggregate tag census is
  
  \[
   \#\{i:d_i=d\}=N_d-N_{d+1}quad(q_0\le d<H),
   \qquad \#\{i:d_i=H\}=N_H;
   \tag{2.3}
  \]
* the selected chains are pairwise mask-disjoint.

Pairwise disjointness may be weakened.  Let

\[
 E_r=\sum_{S\in\binom{[2m]}{m+r}}
             (\mu_r(S)-1)_+.
 \tag{2.4}
\]

An **approximate PRSF** only asks

\[
                         \sum_{r=-H}^{H}E_r=o(W).
 \tag{2.5}
\]

### Theorem 2.1 (one-baseline implication)

An approximate (\operatorname{PRSF}(q_0,H)) implies the coefficient-one
theorem in the standing Boolean-OR reduction.

#### Proof

There are (N_{q_0}) selected chain states and at most (N_H) promotion
paths.  Their literal compilation has length

\[
                         N_{q_0}+2HN_H.
 \tag{2.6}
\]

At a controlled signed depth (q_0\le |r|\le H), (2.3) gives total
occurrence mass (N_{|r|}).  Therefore its hole count equals (E_r).
At a shallow signed depth (|r|<q_0), every selected chain is active, so
the occurrence mass is (N_{q_0}) and the hole count is

\[
                         N_{|r|}-N_{q_0}+E_r.
 \tag{2.7}
\]

Append every missing mask once.  Including the middle layer, the resulting
length is at most

\[
 W+2HN_H
 +2\sum_{q=1}^{q_0-1}(N_q-N_{q_0})
 +\sum_{r=-H}^{H}E_r.
 \tag{2.8}
\]

The second term is (o(W)) by (0.3), the shallow sum is
(O(Wq_0^3/m)=o(W)), and (2.5) handles the last term.  Finally
(H/\sqrt m\to\infty), so the audited product-SCD exterior word costs
(o(W)).  This is one baseline, not a concatenation of two (W)-scale
words. \(\square\)

## 3. Exact symmetric fractional PRSF

Put

\[
                         a_q={N_q\over N_H}
       \qquad(q_0\le q\le H).
 \tag{3.1}
\]

The sequence is nonincreasing, (a_H=1), and (a_{q_0}<M).  Take one
random variable (Z\) uniform on ([0,1)) and set

\[
                         K_q=\lfloor a_q+Z\rfloor.
 \tag{3.2}
\]

Then

\[
 K_{q_0}\ge K_{q_0+1}\ge\cdots\ge K_H=1,
 \qquad \mathbb E K_q=a_q.
 \tag{3.3}
\]

In every top independently of its label:

1. choose a uniform directed cyclic frame;
2. choose a uniform cyclic block (B\) of (K_{q_0}) phase positions;
3. choose a uniform ordering of (B), and let (A_q\) be its first
   (K_q) positions;
4. give a position of (A_q\setminus A_{q+1}) tag (q), and give the
   unique position of (A_H) tag (H).

The active set (B) is one promotion path.  Also

\[
 \mathbb E\#\{\hbox{tag }d\}=a_d-a_{d+1}
 ={N_d-N_{d+1}\over N_H},
 \tag{3.4}
\]

so the aggregate census is exact fractionally.

### Theorem 3.1 (exact target marginals)

For every signed rank (m+r), (q_0\le |r|\le H), every target has
fractional load one.  For (|r|<q_0), every target has fractional load

\[
                         {N_{q_0}\over N_{|r|}}.
 \tag{3.5}
\]

#### Proof

Fix (S\in\binom{[2m]}{m+r}) and a containing top (U).  Its complement
(U\setminus S) has size (H-r).  In a uniform cyclic frame this fixed
set is an interval with probability

\[
                         {M\over\binom M{H-r}}.
 \tag{3.6}

Conditional on that event, its phase is rotationally uniform.  The
probability that this phase lies in (A_{|r|}) is
(a_{|r|}/M).  There are

\[
                         \binom{m-r}{H-r}
 \tag{3.7}

containing tops.  The double-counting identity

\[
 N_H\binom M{H-r}
 =N_{|r|}\binom{m-r}{H-r}
 \tag{3.8}

now gives load one.  If (|r|<q_0), replace (a_{|r|}) by
(a_{q_0}), which gives (3.5). \(\square\)

Thus every linear dual of the natural full configuration LP is cleared by
an actual convex combination of path-respecting, one-anchor-per-top ring
configurations.  The missing issue is integrality, not a fractional tag or
capacity defect.

### Proposition 3.2 (same-rank pair bound and chain diagonal)

In the fractional construction above, let (S,T) be two distinct targets
of the same signed rank (m+r), and put

\[
                         d=|S\setminus T|=|T\setminus S|.
\]

For (1\le d<H-r), their joint load is at most

\[
 \boxed{
 {2+o(1)\over
   \binom{m-r}{d}\binom{m+r}{d}}.}
 \tag{3.9}
\]

The disjoint-interval endpoint (d=H-r) is smaller.  In particular, the
maximum same-rank pair load is

\[
                         {2+o(1)\over m^2}.
 \tag{3.10}

By contrast, let (S\subset T) have signed ranks (m+r<m+s), and put
(q=\max\{|r|,|s|\}).  The contribution in which (S,T) lie on the
same phase chain is exactly

\[
 \boxed{
 \Lambda^{\rm diag}_{r,s}(S,T)
 ={(s-r)!(m-s)!(m+r)!\over(m-q)!(m+q)!}.}
 \tag{3.11}

For adjacent ranks on either one side of the middle, (3.11) is
(1/(m+O(H))\).  This (m^{-1}) diagonal is an intended chain
correlation, not an owner collision.

#### Proof

First ignore tag thinning and activate every phase.  The standard
two-interval count gives joint load

\[
 {MN_H\over N_{|r|}}
 {2\over\binom{m-r}{d}\binom{m+r}{d}}.
 \tag{3.12}

Condition on (K_{q_0}=k_0,K_{|r|}=k).  For any two distinct cyclic
positions, the probability that both lie in the random active block is at
most ((k_0-1)/M).  Conditional on this, the probability that both lie
among the first (k) positions of its random ordering is

\[
                         {k(k-1)\over k_0(k_0-1)}.
\]

Their joint activation probability is therefore at most

\[
 {k(k-1)\over Mk_0}
 \le { (a_{|r|}+1)^2\over M(a_{q_0}-1)}.
 \tag{3.13}

Since (MN_H/N_{|r|}=M/a_{|r|}), while
(1\le a_{|r|}\le a_{q_0}=(1+o(1))m), multiplication of
(3.12)--(3.13) proves (3.9).  The exact two-disjoint-interval count is
smaller, and (3.10) follows because (|r|\le H=o(m)).

For (3.11), write (a=s-r).  A common top is obtained in

\[
                         \binom{m-s}{H-s}
\]

ways.  In a fixed top, the number of directed cyclic frames in which the
two omitted intervals have the same terminal endpoint is

\[
                         a!(H-s)!(m+r)!.
\]

Divide by ((M-1)!), multiply by the activation probability
(a_q/M\), and use

\[
 {a_q}={N_q\over N_H}
 ={(m-H)!M!\over(m-q)!(m+q)!}.
\]

Cancellation gives (3.11). \(\square\)

The codegree audit therefore has a natural two-level reading.  After a
whole phase chain is contracted to one atom, the remaining same-rank
inter-chain geometry is (O(m^{-2})).  Expanding the atom necessarily
restores the (O(m^{-1})) adjacent-rank diagonal.  A black-box matching
theorem which treats all coloured masks as unrelated vertices loses this
distinction and sees the wrong effective parameter.

## 4. The one-hole owner hypergraph

Let (\mathcal R^-\) be the following (M)-uniform multihypergraph.
Its vertices are

\[
 \mathcal U=\binom{[2m]}M,
 \qquad \mathcal X=\binom{[2m]}m.
 \tag{4.1}
\]

For a top (U), choose an oriented cyclic frame modulo rotation and mark
one phase for deletion.  The corresponding edge contains

* the top vertex (U); and
* the (M-1) middle masks from all unmarked phases.

Oriented marked representations are retained as parallel edges.  This
does not affect matchings and makes every count literal.

### Theorem 4.1 (degrees)

Every top and every middle owner have the degrees in (0.4).

#### Proof

There are ((M-1)!) oriented cyclic frames and (M) choices of the
deleted phase, so (D_U=M!).

Fix a middle mask (X).  A containing top is (X\cup J), where
(J\subseteq[2m]\setminus X), (|J|=H), giving \(\binom mH\) choices.
For fixed (J), exactly (H!m!) directed cyclic frames make (J) one
cyclic interval.  The deleted phase may be any of the other (M-1)
phases.  Therefore

\[
 D_X=\binom mH H!m!(M-1)
     ={(m!)^2(M-1)\over(m-H)!}.
\]

Finally \(\lambda_H=M!(m-H)!/(m!)^2\), proving the ratio. \(\square\)

### Theorem 4.2 (pair codegrees)

Equation (0.5) holds.  A top--owner pair (U,X) has codegree zero unless
(X\subset U), and otherwise has codegree

\[
                         H!m!(M-1).
 \tag{4.2}
\]

Distinct top vertices have codegree zero.

#### Proof

Let (d=|X\setminus Y|=|Y\setminus X|).  For (d\le H), the number of
common tops is

\[
                         \binom{m-d}{H-d}.
 \tag{4.3}
\]

For (1\le d<H), the number of directed cyclic frames in a fixed common
top in which both complementary (H)-sets are intervals is

\[
                         2d!^2(H-d)!(m-d)!.
 \tag{4.4}
\]

The deleted phase has (M-2) choices.  Multiplying (4.3)--(4.4) and
dividing by (D_X) gives the first line of (0.5).

For (d=H), the two (H)-intervals are disjoint.  There is one common
top and

\[
                         H!^2(m-H+1)!
 \tag{4.5}

directed cyclic frames; again the mark has (M-2) choices.  This gives
the second line.  No common top exists for (d>H).  Formula (4.2) is the
one-mask count with the marked phase forbidden. \(\square\)

### Theorem 4.3 (exact fractional matching dual)

The fractional matching number of (\mathcal R^-\) is (0.6).

#### Proof

Give every edge weight (1/D_X).  Every owner has load one, while every
top has load

\[
                         {D_U\over D_X}
                         ={\lambda_H\over M-1}<1
 \tag{4.6}
\]

for all sufficiently large (m).  Thus the assignment is a fractional
matching of total weight

\[
 {N_HD_U\over D_X}={N_H\lambda_H\over M-1}
 ={W\over M-1}.
\]

Conversely, every edge uses (M-1) owner vertices, so owner capacity
bounds every fractional matching by (W/(M-1)). \(\square\)

For exact retained tags, a full repaired ring has one tag-(H) anchor and
(M-2) lower-tag slots.  This gives (0.7).  Writing

\[
                         \beta={N_{q_0}\over W}
       =1-m^{-1/2}+O(m^{-3/4}),
 \tag{4.7}
\]

and ignoring the harmless final floor,

\[
\begin{aligned}
 {1\over N_H}\left({W\over M-1}-K_0\right)
 &= {\lambda_H\over M-1}
    -{\lambda_H\beta-1\over M-2}\\
 &= {(M-1)-\lambda_H+(M-1)\lambda_H(1-\beta)
       \over(M-1)(M-2)}\\
 &= (1+o(1))m^{-1/2},
\end{aligned}
 \tag{4.8}
\]

which proves (0.8).

There is a weaker owner-only use which needs no such quantitative leave.
If a matching covers (W-o(W)) owner vertices, then restoring an arbitrary
one-hole frame on every unmatched top creates owner overload at most

\[
 o(W)+\big((M-1)N_H-W\big)=o(W).
 \tag{4.9}
\]

Thus an ordinary near-perfect owner matching is sufficient for the
middle ledger.  It is not sufficient for the nested traces.

## 5. Nibble audit

The smaller degree is (D_U), and Theorem 4.2 gives

\[
 {\Delta_2\over D_U}={2+o(1)\over m^2}.
 \tag{5.1}
\]

Since (k=M=(1+o(1))m) and

\[
                         \log(W+N_H)=2m\log2+O(\log m),
 \tag{5.2}
\]

equations (5.1)--(5.2) give (0.9).  The known variable-rank sufficient
condition asks for this quantity to tend to zero.  Fixed-uniformity
Pippenger--Spencer cannot be invoked after (M\to\infty), and the
audited Gould--Kelly hierarchy is also outside its published diagonal.

The exact local overlap is nevertheless favorable: the normalized pair
mass internal to one repaired edge is (2/m+O(m^{-2})), the same as for
one full ring.  Hence a fresh slow bite is efficient.  What is absent is
a hereditary regeneration theorem keeping the residual away from the
finite-character and clustering traps already exhibited for full
promotion rings.  One-hole deletion does not by itself prove that
trajectory theorem.

There is, in fact, an exact one-hole version of the character warning.

### Proposition 5.1 (one-hole parity classification)

Put (g=\gcd(M,H)).  Fix a coordinate set (P\subseteq[2m]), a top
(U), a cyclic frame (c_0,\ldots,c_{M-1}), and delete phase (j).
Suppose all (M-1) retained middle owners have the same parity of
(|X\cap P|).  Write

\[
                         z_i=\mathbf1_{\{c_i\in P\}}.
 \tag{5.3}

If (g>1), then (z) is constant on every orbit of the shift
(i\mapsto i+H).  In particular

\[
                         |U\cap P|\in
 \left\{0,{M\over g},{2M\over g},\ldots,M\right\}.
 \tag{5.4}

If (g=1), let (a\in\{1,\ldots,M-1\}) satisfy

\[
                         aH\equiv1\pmod M.
 \tag{5.5}

Then

\[
                         |U\cap P|\in\{0,M,a,M-a\}.
 \tag{5.6}

Conversely, the two nonconstant patterns in the coprime case are the two
binary blocks of lengths (a) and (M-a) in the (H)-step cyclic
order, and they do make all retained parities equal.

#### Proof

Let (f_i\) be the parity of the phase-(i) middle owner.  The difference
of consecutive window sums is

\[
                         f_{i+1}-f_i=z_i-z_{i+H}\pmod2.
 \tag{5.7}

Since (f_i\) is constant away from the deleted phase, (5.7) gives

\[
                         z_i=z_{i+H}
       \qquad(i\notin\{j-1,j\}).
 \tag{5.8}

If (g>1), the two exceptional tails lie in two different cycles of the
shift by (H).  Deleting one edge from either cycle still leaves a path
joining all its vertices, so (5.8) makes (z) constant on that cycle;
the other cycles are unchanged.  This proves (5.4).

If (g=1), the shift is one (M)-cycle.  Removing the two exceptional
edges leaves two paths, on each of which (z) is constant.  Their vertex
counts are (a) and (M-a), because (a) is the distance in the
(H)-step cycle between the two exceptional tails.  This proves (5.6)
and the converse. \(\square\)

For example, in the coprime case choose a fixed density
(\rho\in\{1/4,1/2,3/4\}) separated by an absolute constant from
(a/M) and (1-a/M), and take (|P|=2\rho m+O(1)).  One of the two
parity classes of the middle layer has density at least (1/2), while a
hypergeometric large-deviation bound shows that only

\[
                         e^{-\Omega(m)}N_H
 \tag{5.9}

tops can support a repaired ring entirely inside it.  Thus even the
one-hole catalogue has dense statewise residuals with exponentially too
few usable top colours.  This does not obstruct a process-specific
trajectory, but it rigorously rules out any theorem asserting regeneration
for arbitrary dense residuals.

## 6. The chain-atom quotient and its conflict system

The (m^{-1}) diagonal in Proposition 3.2 can be contracted exactly.
This gives a useful two-level normal form, but not a proof.

For a frame (\pi\) on (U) and a phase (i), let

\[
                         a=(U,\pi,i)
 \tag{6.1}
\]

be the **full chain atom** whose signed traces are (C_{U,i}(r)),
(-H\le r\le H).  A tag merely truncates this route.  Its quotient
resource is its middle owner

\[
                         o(a)=C_{U,i}(0).
 \tag{6.2}

The one-hole owner hypergraph is exactly the hypergraph obtained by
replacing every repaired ring by its (M-1) quotient resources and one
top marker.

### Proposition 6.1 (atom degrees and vertical codegrees)

In the unmarked directed-frame catalogue, every middle owner belongs to

\[
                         D_0={(m!)^2\over(m-H)!}
 \tag{6.3}

chain atoms.  A fixed signed-rank target (S\) of rank (m+r) belongs to

\[
                         D_r={(m-r)!(m+r)!\over(m-H)!}
                             =\lambda_{|r|}D_0
 \tag{6.4}

full atoms.  If (S\subset T) have ranks (m+r<m+s), the number of
atoms in which they occur on the same vertical route is

\[
 D_{r,s}^{\rm vert}(S,T)
 ={(s-r)!(m-s)!(m+r)!\over(m-H)!}.
 \tag{6.5}

Consequently

\[
 {D_{r,s}^{\rm vert}\over D_0}
 ={(s-r)!(m-s)!(m+r)!\over(m!)^2}.
 \tag{6.6}

#### Proof

For (6.3), choose the (H) coordinates of (U\setminus o(a)), then
contract this prescribed (H)-interval in the cyclic frame.  This gives

\[
 \binom mH H!m!={(m!)^2\over(m-H)!}.
\]

For (6.4), choose the (H-r) coordinates extending (S) to (U) and
contract their interval:

\[
 \binom{m-r}{H-r}(H-r)!(m+r)!
 ={(m-r)!(m+r)!\over(m-H)!}.
\]

For (6.5), the two omitted intervals must have one terminal endpoint.
The block (T\setminus S), the final omitted block (U\setminus T),
and the remaining (S)-coordinates give

\[
 \binom{m-s}{H-s}(s-r)!(H-s)!(m+r)!,
\]

which is (6.5). \(\square\)

Equation (6.6) is large near the top boundary; that is precisely the
vertical correlation removed by contraction.

Now put a conflict relation on distinct atoms with distinct owners:

\[
 a\sim b
 \quad\Longleftrightarrow\quad
 C_a(r)=C_b(r)\text{ for some signed rank active in both tags}.
 \tag{6.7}

Atoms in the same promotion ring never conflict, by Theorem 3.6.  For an
atom truncated to tag (d), the number of untagged full routes which can
conflict with it is at most

\[
 D_0\left(1+2\sum_{q=1}^d\lambda_q\right).
 \tag{6.8}

At the critical height,

\[
 1+2\sum_{q=1}^H\lambda_q
 =\Theta\left({m^{3/2}\over\sqrt{\log m}}\right).
 \tag{6.9}

The bound follows by summing the target-star degrees (6.4); (6.9) is the
endpoint Laplace estimate for
(\sum_{q\le H}\exp(q^2/m)).

### Theorem 6.2 (exact quotient-plus-conflicts equivalence)

Suppose one selects repaired ring columns which form a matching in the
quotient owner hypergraph, assigns the exact tag census, and satisfies:

1. exactly one tag-(H) atom belongs to every top (using singleton or
   partial terminal columns where necessary); and
2. no two selected atoms from different rings are related by (6.7).

Then the expanded chains are pairwise mask-disjoint.  Conversely, every
promotion-ring SCD factorization projects to such a quotient matching and
conflict-free tagged atom family.

#### Proof

The quotient matching removes all middle-rank collisions and all repeated
top markers.  Theorem 3.6 removes every within-ring collision.  Condition
2 removes every remaining collision at a nonmiddle rank.  This proves the
forward implication.  Projection of a pairwise mask-disjoint factor gives
the converse immediately. \(\square\)

The conflict system is not sparse at the scale of a whole decorated
ring.  Under the exact census, the average number of controlled signed
trace vertices expanded from one top is

\[
 {2\over N_H}\sum_{q=q_0}^{H}N_q
 = (\sqrt\pi+o(1))m^{3/2}.
 \tag{6.10}

At the symmetric fractional point, independent top choices have mean
load one on each target and therefore

\[
                         \Theta(W\sqrt m)
 \tag{6.11}

expected coloured collision pairs in aggregate.  Equivalently, a random
selected ring participates in polynomially many expanded conflicts even
though its quotient-owner codegrees are (O(m^{-2})).

Thus the contraction identifies the right architecture:

\[
 \boxed{
 \text{near-perfect owner-ring matching}
 \quad+\quad
 \text{conflict-free expansion of chain atoms}.}
 \tag{6.12}

But it does not put the second factor inside a current theorem.  Available
conflict-free matching results are proved with fixed base uniformity (or
with a polylogarithmic hierarchy which fails in this diagonal); here the
base rank is (M\asymp m), and expanding one column has the
\(\Theta(m^{3/2})\) census (6.10).  A theorem which ignores the atom
contraction sees the (m^{-1}) vertical diagonal, while a theorem which
uses the quotient must also control the separate conflict system (6.7).

## 7. The residual nested-tag system

Assume that owner-disjoint repaired rings and any required singleton or
partial terminal anchors have been chosen.  Let (\mathcal P\) be their
retained phase positions.  For (v\in\mathcal P\), write

\[
 \phi_q^-(v)\in\binom{[2m]}{m-q},\qquad
 \phi_q^+(v)\in\binom{[2m]}{m+q}
 \tag{7.1}
\]

for its two ring traces at depth (q).  The exact remaining problem is to
find thresholds (y_{v,q}\in\{0,1\}) satisfying

\[
 y_{v,q_0}\ge y_{v,q_0+1}\ge\cdots\ge y_{v,H},
 \tag{7.2}
\]

\[
 \sum_vy_{v,q}=N_q,
 \tag{7.3}
\]

\[
 \sum_{v:\phi_q^-(v)=S}y_{v,q}=1,qquad
 \sum_{v:\phi_q^+(v)=T}y_{v,q}=1,
 \tag{7.4}
\]

for every signed target (S,T), together with exactly one (y_{v,H}=1)
in every top fibre.  Tags are recovered from the differences
(y_{v,q}-y_{v,q+1}).

The census and one-root-per-top subsystem is a transportation problem and
is totally unimodular.  The target equations (6.4) are the sole source of
non-TU coupling.  Most importantly, in an exact truncated factor every
retained high-tag position has

\[
                         y_{v,q_0}=1.
 \tag{7.5}

\]

Therefore both maps (v\mapsto\phi_{q_0}^-(v)) and
(v\mapsto\phi_{q_0}^+(v)) must already be bijections when the owner
packing is chosen.  No later tag assignment can repair a collision at
this entrance layer.

This proves the exact separation:

\[
 \boxed{
 \text{owner repaired-ring matching}
 \quad+\quad
 \text{nested two-sided trace transversals}.}
 \tag{7.6}
\]

The first factor has the favorable census (0.4)--(0.6), but no applicable
black-box factor theorem.  The second is a genuinely coloured common-frame
problem and is not implied by the first.

## 8. Boundary

Proved here:

1. the critical (MN_H=W+o(W)) capacity and one-path-per-top overhead;
2. the exact one-baseline implication of an approximate promotion-ring
   SCD factorization;
3. an exact path-respecting symmetric fractional factor with the correct
   tag and target marginals;
4. all degrees and pair codegrees of the one-hole owner hypergraph;
5. its exact fractional matching number and the (N_H/\sqrt m) integral
   precision exposed by (q_0=m^{1/4});
6. the exact constant-boundary failure of current growing-uniformity
   nibble hypotheses; and
7. the exact chain-atom quotient, its vertical degree formulas, and the
   separate nonmiddle conflict system; and
8. the nested two-sided threshold system which remains after owner
   packing.

Not proved:

1. an owner matching of the required size (or even an owner near-factor)
   for the one-hole cyclic-frame catalogue;
2. an integral entrance-coloured frame selection;
3. the nested threshold system (6.2)--(6.4);
4. an approximate PRSF with aggregate defect (o(W)); or
5. the coefficient-one theorem.

The route is therefore closer in formulation, not closed in strength:
all scalar and linear obstructions vanish, while the remaining assertion
is exactly an integral common-history theorem.
