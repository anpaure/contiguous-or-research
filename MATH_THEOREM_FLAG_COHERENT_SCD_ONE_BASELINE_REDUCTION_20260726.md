# Flag-coherent SCD packets: a one-baseline reduction to one path-cover gate

Date: 2026-07-26

Method: pure mathematics only.  This note combines the exact SCD scaffold,
the corrected shallow packet ledger, and the audited economical exterior
compiler.  It does not assume an unproved matching or rounding theorem.

## 0. Result

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q}.
\]

Choose integer functions \(q_0=q_0(m)\) and \(H=H(m)\), with
\(1\le q_0\le H<m\) for all sufficiently large \(m\), satisfying

\[
 q_0=o(m^{1/3}),\qquad
 {H\over\sqrt m}\longrightarrow\infty,qquad H=o(m).
\tag{0.1}
\]

Let \(\mathcal D\) be a full symmetric-chain decomposition of
\(B_{2m}\), and retain

\[
 \Omega=\mathcal D_{\ge q_0}.
\tag{0.2}
\]

Thus \(|\Omega|=N_{q_0}\).  For every retained chain use its original
middle member.  If its radius is at least \(H\), restrict its original
lower and upper SCD flags to radius \(H\); if its radius is below \(H\),
retain its original flags through its full radius and extend the two outer
collars arbitrarily to a complete radius-\(H\) state.  Call these states
**inner-flag coherent**.

### Theorem (one-baseline flag-coherent reduction)

Suppose that for some choices \(\mathcal D_m\) and of the outer collars,
the inner-flag-coherent states in \(\Omega\) have a vertex-disjoint
bridge-one directed path cover with \(p_m\) paths, where

\[
                         p_m=o(W/H).
\tag{0.3}
\]

Then the central and Gaussian bands admit one literal Boolean-OR word of
length \(W+o(W)\).  Appending the audited product-SCD exterior word covers
every nonempty Boolean target at coefficient one (the empty target is
handled by the standing empty-interval convention, or by one harmless
additive entry), and hence gives the constant-one asymptotic theorem in the
standing reduction.

More precisely, before the economical exterior is appended, the length is
at most

\[
 \boxed{
 W+2Hp_m+2\sum_{q=1}^{q_0-1}(N_q-N_{q_0}).}
\tag{0.4}
\]

The final sum has the uniform expansion

\[
 2\sum_{q=1}^{q_0-1}(N_q-N_{q_0})
 ={W\over3m}(q_0-1)q_0(4q_0+1)
 +O\!\left(W{q_0^5+q_0^3\over m^2}\right)=o(W).
\tag{0.5}
\]

If in addition \(q_0\to\infty\), its leading form is

\[
 \left({4\over3}+o(1)\right){Wq_0^3\over m}.
\tag{0.5a}
\]

Thus no PBBS/annulus overlay, no second \(W\)-baseline, and no shallow
collision estimate are needed.  The entire remaining assertion is the
single path-cover estimate (0.3) for an inner-flag-coherent SCD.

One concrete admissible scale is

\[
 q_0=\lceil m^{1/4}\rceil,qquad
 H=\lceil\sqrt m\,\log\log(m+3)\rceil.
\tag{0.6}
\]

## 1. Exact shallow simplicity

Write a chain \(C\in\mathcal D\) of radius \(d\) as

\[
 C_{-d}\subset\cdots\subset C_{-1}\subset C_0
 \subset C_1\subset\cdots\subset C_d,
 \qquad |C_j|=m+j.
\tag{1.1}
\]

For every \(q<q_0\), each retained chain has radius at least \(q_0>q\),
so its inner-flag-coherent state has signed depth-\(q\) targets

\[
                         C_{-q},\qquad C_q.
\tag{1.2}
\]

Because an SCD partitions every Boolean rank, the maps

\[
 C\longmapsto C_{-q},\qquad C\longmapsto C_q
 \quad(C\in\Omega)
\tag{1.3}
\]

are injective.  Hence the selected states have no repeated target at any
omitted shallow depth:

\[
                         E_q^-=E_q^+=0
                         \qquad(1\le q<q_0).
\tag{1.4}
\]

There are \(N_q\) targets on either signed rank and \(|\Omega|=N_{q_0}\)
selected states.  Therefore the number of missing shallow targets is not
merely bounded but exact:

\[
                         M_q^-=M_q^+=N_q-N_{q_0}.
\tag{1.5}
\]

This is the SCD-flag-coherent specialization of the corrected identity

\[
 M_q^\sigma=N_q-N_{q_0}+E_q^\sigma
\]

with no packet-floor remainder, because a path cover uses all
\(N_{q_0}\) states rather than first rounding their number to a multiple
of \(2m\).

## 2. Exact annular coverage

Fix \(q_0\le q\le H\).  Every depth-\(q\) target lies in exactly one SCD
chain, and that chain has radius at least \(q\).  Consequently

\[
 \mathcal D_{\ge q}\longrightarrow\binom{[2m]}{m-q},
 \quad C\longmapsto C_{-q},
\tag{2.1}
\]

and

\[
 \mathcal D_{\ge q}\longrightarrow\binom{[2m]}{m+q},
 \quad C\longmapsto C_q,
\tag{2.2}
\]

are bijections.  Since
\(\mathcal D_{\ge q}\subseteq\Omega\), the selected states cover every
target at both signed depth-\(q\) ranks.  Chains with radius in
\([q_0,q)\) may add witnesses through their arbitrary outer extensions,
but they cannot create a hole.

Thus the same states simultaneously have

* exact distinct shallow flags through \(q_0-1\); and
* complete target support at every depth from \(q_0\) through \(H\).

This is the correlation which a rank-\(q_0\) packet matching does not
supply.

## 3. Literal compilation and the length ledger

A bridge-one directed path on \(s\) complete radius-\(H\) states has a
literal realization of length \(s+2H\).  Realize the \(p_m\) paths
separately.  Their total length is

\[
                         N_{q_0}+2Hp_m.
\tag{3.1}
\]

The original SCD middle members of the retained chains are distinct.
Append once each of the other \(W-N_{q_0}\) middle masks.  The middle
layer is then complete and the length is

\[
                         W+2Hp_m.
\tag{3.2}
\]

Section 2 says no target repair is needed at depths
\(q_0\le q\le H\).  At every shallower signed depth, append precisely the
missing targets counted in (1.5).  This proves the exact bound (0.4).

It remains to estimate its last term.  Uniformly for
\(q\le q_0=o(\sqrt m)\),

\[
 {N_q\over W}=1-{q^2\over m}
 +O\!\left({q_0^4\over m^2}+{q_0^2\over m^2}\right).
\tag{3.3}
\]

Hence

\[
 \begin{aligned}
 2\sum_{q=1}^{q_0-1}(N_q-N_{q_0})
 &= {2W\over m}
    \sum_{q=1}^{q_0-1}(q_0^2-q^2)
    +o(Wq_0^3/m)\\
 &= {W\over3m}(q_0-1)q_0(4q_0+1)
    +O\!\left(W{q_0^5+q_0^3\over m^2}\right),
 \end{aligned}
\tag{3.4}

which is (0.5), and gives (0.5a) when \(q_0\to\infty\).  Assumption
(0.3) makes \(2Hp_m=o(W)\), and
\(q_0=o(m^{1/3})\) makes (3.4) \(o(W)\).  The central-through-\(H\) word
therefore has length \(W+o(W)\).

Finally, the independently audited product-SCD exterior compiler costs
\(o(W)\) whenever \(H/\sqrt m\to\infty\) and \(H=o(m)\).  Appending it
does not destroy any internal witness and covers every remaining nonempty
Boolean target.  The standard one-coordinate trimmed lift then transfers
the even-dimensional coefficient-one bound to odd dimensions, completing
the standing conditional conclusion.

## 4. Exact surviving gate

Define

\[
 \operatorname{fcpath}_{q_0,H}(\mathcal D)
 =\min p,
\tag{4.1}
\]

where the minimum is over choices of outer collars on the original-corner,
inner-flag-coherent states of \(\mathcal D_{\ge q_0}\), and over
bridge-one directed path covers of those states.  Then the sole hypothesis
of the theorem is

\[
 \boxed{
   \min_{\mathcal D\ {\rm an\ SCD}}
   \operatorname{fcpath}_{q_0,H}(\mathcal D)
   =o(W/H).}
\tag{4.2}
\]

For fixed selected states this is exactly the minimum, over total orders
\(\prec\), of the bipartite Hall deficiency of the forward bridge graph
\(v_Lw_R\) with \(v\prec w\).  Indeed, a forward matching is a directed
linear forest, and every directed path cover admits a total order extending
its path orders.  The difficulty is the outer minimization over one SCD and
one simultaneous collar choice.  Independent depthwise Hall matchings do
not imply (4.2), because their chosen parents need not be nested into one
history.

The gate is stronger than the annulus-only SCD scaffold: arbitrary middle
corners there supplied \((2q_0)!\) inner-port freedom, whereas inner-flag
coherence fixes the central corner and its two inner orders.  It is weaker
than a cyclic factorization of the whole SCD: radius-below-\(q_0\) chains
are omitted and then restored only as middle singletons, and paths rather
than cycles are sufficient.

## 5. Boundary

Proved here:

1. inner-flag coherence forces zero shallow repeat excess exactly;
2. the omitted shallow repair bill has the exact leading term (0.5);
3. the same retained SCD states cover the entire annulus through \(H\);
4. one path cover satisfying (0.3) yields one baseline of length
   \(W+o(W)\); and
5. the economical exterior compiler then completes the standing
   coefficient-one reduction.

Not proved here:

1. the path-cover estimate (4.2);
2. a noncanonical SCD with the required flag-shift/rotor compatibility;
   or
3. the final constant-one theorem.

The corrected frontier is therefore one theorem rather than an invalid
fusion claim: construct an inner-flag-coherent high-radius SCD whose
bridge-one ordered-Hall deficiency is \(o(W/H)\).
