# Audit: the shared-prefix packet is the ordinary cyclic-order packet, and the owner near-factor is unnecessary

Date: 2026-07-26

Audited source:
`MATH_THEOREM_GAUSSIAN_SHARED_PREFIX_PACKET_FRACTIONAL_BRAID_20260726.md`.

## 0. Verdict

The elementary packet geometry, the delay-factor length, and the labelled
orbit double counts (0.6)--(0.9) are correct.  There is no hidden rank or
normalization error, provided that \(\mathscr O\) is read exactly as the
source says: a \(S_{2m}\)-indexed **multiset**, retaining all labels.

There are, however, two important scope corrections.

1.  The packet is not a new kind of owner cycle.  It is exactly the standard
    cyclic-interval packet of one directed cyclic order on \([2m]\).  Hence
    (0.6)--(0.9) are the usual all-cyclic-orders fractional design, already
    appearing as Proposition 5.1 of
    `MATH_ATTACK_AD30_SINGLE_CYCLIC_INTERVAL_NEAR_DESIGN_20260725.md`.
    The new useful observation is only the moving-frame interpretation of
    consecutive subsegments and the fact that one delay collar is shared by
    all of them.

2.  The condition \(R(\mathcal F)=o(W)\) in Proposition 5.1 is not used and
    is not needed for a coefficient-one literal annulus compiler.  Even an
    owner-disjoint family with a linear owner leave can append the missing
    middle masks at exact baseline cost.  More generally, owner disjointness
    may be weakened to \(o(W)\) total owner collisions.

Thus the source gives a sound statewise refutation of an independent-prefix
toll, but the fractional incidence theorem is symmetry averaging, not an
integrality advance.  The genuine remaining theorem is a partial cyclic-
interval annulus design, stated precisely in Section 5 below.

## 1. Identification with an ordinary directed cyclic order

Set

\[
 \pi=(u_1,u_2,\ldots,u_m,v_1,v_2,\ldots,v_m)
\]

as a directed cyclic order.  Its length-\(m\) cyclic intervals are

\[
 I_\pi(j,m)
 =Z_0-\{u_1,\ldots,u_j\}+\{v_1,\ldots,v_j\}
 =Z_j
 \qquad(0\le j\le m),
\]

and, after the halfway point,

\[
 I_\pi(m+j,m)
 =Z_0^c-\{v_1,\ldots,v_j\}+\{u_1,\ldots,u_j\}
 =Z_{m+j}.
\]

Consequently

\[
 \boxed{\mathcal C=(I_\pi(j,m))_{j\in\mathbb Z_{2m}}.}
\]

Conversely every directed cyclic order has this form, with opposite
positions paired as \(e_i=\{\pi_i,\pi_{i+m}\}\).  Therefore the full
coordinate-conjugacy orbit in the source is precisely the complete
catalogue of directed cyclic orders, with rotation multiplicity retained.

The lower and upper windows also reduce to the standard interval identities

\[
 \bigcap_{t=0}^{q}I_\pi(j+t,m)=I_\pi(j+q,m-q),
 \qquad
 \bigcup_{t=0}^{q}I_\pi(j+t,m)=I_\pi(j,m+q).
\]

In particular, the target-incidence LP in Section 3 is exactly the cyclic-
interval incidence LP.  It is not a smaller quotient of that problem.

## 2. Geometry and literal factorization audit

The following checks pass.

* The states are simple and antipodal.  The bit pattern on the opposite
  pairs \(e_i\) is a prefix in the first half and its complement in the
  second half, so only the cyclic endpoint repeats.
* The support word is
  \(e_1\cdots e_m e_1\cdots e_m\).  A block of at most \(m\) consecutive
  transitions never contains both occurrences of an \(e_i\), so all lower
  intersections and upper unions through depth \(m\) have ranks
  \(m-q\) and \(m+q\).
* Cutting the cycle, copying the first \(H\) owner states, and applying the
  finite delay-\(H\) factor lemma emits at most \(2m+2H\) factor letters.
  Equivalently, for this particular cycle one may use the explicit erosion
  word consisting of the \(2m\) consecutive length-\((m-H)\) intervals
  followed by its first \(2H\) entries.  Thus an exact
  \(2m+2H\)-letter realization exists and no empty-letter issue occurs.
* Complement-antipodality gives
  \(L_{j+m,q}=U_{j,q}^c\), and therefore the lower and upper hole ledgers
  are identical after complementation.

There is one minor wording correction.  Lemma 1.2 requires

\[
 h\equiv m\pmod 2,
\]

because \((m-h)/2\) must be integral.  Outcome item 3 should therefore say
"for every admissible \(h=\Theta(\sqrt m)\)," or "for a choice within one
of every prescribed Gaussian scale."  This does not affect any asymptotic
count.

Likewise, the phrase "entire all-depth state sequence" in Outcome item 4
should be read as "all controlled depths \(q\le H\)."  The displayed
compiler makes no claim for \(q>H\).

The product-atom decomposition is also correct: a monotone length-\(h\)
segment can be placed in a local \(m+m\) frame with endpoint ranks
\((m-h)/2\) and \((m+h)/2\), and coordinate conjugacy realizes its chosen
increment order.  But this decomposition is auxiliary.  Neither the orbit
incidences nor the integral target conditions use the frames.

## 3. Normalization audit

For each fixed owner position \(j\) and middle set \(X\), exactly
\((2m)!/W\) permutations send \(Z_j\) to \(X\).  Thus

\[
 \sum_{g\in S_{2m}}a_X(P_g)=2m\frac{(2m)!}{W}.
\]

With \(\theta_m=W/((2m)!2m)\), the owner load is one.  At depth \(q\),
there are \(2m\) windows in every labelled packet, and transitivity at rank
\(m-q\) gives

\[
 \sum_g\theta_m b^-_{q,T}(P_g)=\frac{W}{N_q}.
\]

The upper formula is identical by complementation.  Finally

\[
 \sum_g\theta_m=\frac{W}{2m},
\qquad
 \frac{W}{2m}(2m+2H)=W+\frac HmW.
\]

Hence (0.6)--(0.9) are exact.

If rotations are quotiented out, the same calculation assigns every
directed cyclic order the standard weight

\[
 \frac1{(m!)^2}.
\]

This is exactly AD30 Proposition 5.1.  More generally, the double count
would work for any transitive labelled family of equal-length safe cycles;
it contains no dispersion or rounding information.

## 4. A stronger fractional correction: full owner mass is unnecessary

Put

\[
 q_0=\lceil a\sqrt m\rceil,
 \qquad
 \alpha_m=\frac{N_{q_0}}W.
\]

Scale the orbit solution by \(\alpha_m\):

\[
 x_{P_g}=\alpha_m\theta_m
 =\frac{N_{q_0}}{(2m)!\,2m}.
\]

Then every middle owner has fractional load \(\alpha_m\), while every
annular target at depth \(q\ge q_0\) has load

\[
 \alpha_m\frac{W}{N_q}=\frac{N_{q_0}}{N_q}\ge1.
\]

Repair the missing middle fraction \(1-\alpha_m\) with singleton middle
columns.  The total fractional literal cost is

\[
 \frac{N_{q_0}}{2m}(2m+2H)+(W-N_{q_0})
 =W+\frac HmN_{q_0}
 =W+O_{a,b}(W/\sqrt m).
\]

The packet mass \(N_{q_0}/(2m)\) is optimal for covering rank
\(m-q_0\), because a packet contains only \(2m\) such targets.  Thus the
natural fractional annulus solution uses only the constant owner density

\[
 \alpha_m=\frac{N_{q_0}}W=e^{-a^2+o(1)},
\]

not a near-perfect owner factor.

## 5. The precise remaining integral packet theorem

For a family \(\Pi\) of directed cyclic orders, define

\[
 D_0(\Pi)
 =\left|\bigcup_{\pi\in\Pi}\{I_\pi(j,m):j\in\mathbb Z_{2m}\}\right|,
\]

\[
 C_0(\Pi)=2m|\Pi|-D_0(\Pi)
\]

and

\[
 h_q(\Pi)
 =N_q-
 \left|\bigcup_{\pi\in\Pi}
       \{I_\pi(j,m-q):j\in\mathbb Z_{2m}\}\right|.
\]

The upper-rank hole count equals \(h_q(\Pi)\) exactly by complementation.

The following is the minimal clean packet-selection theorem sufficient for
the fixed annulus:

> **Partial shared-prefix annulus selection (open).**  For every fixed
> \(0<a<b\), there is a family \(\Pi_m\) of directed cyclic orders such
> that
> \[
>  C_0(\Pi_m)=o(W),
>  \qquad
>  \sum_{q=q_0}^{H}h_q(\Pi_m)=o(W).
> \]

Indeed, concatenate the \(|\Pi_m|\) length-\((2m+2H)\) packet words,
append every missing middle mask, and append every missing signed annular
target.  The resulting length is at most

\[
\begin{aligned}
 |\Pi_m|(2m+2H)+(W-D_0(\Pi_m))
      +2\sum_{q=q_0}^{H}h_q(\Pi_m)
 &=W+C_0(\Pi_m)+2H|\Pi_m|
      +2\sum_qh_q(\Pi_m).
\end{aligned}
\]

The collision hypothesis implies \(2m|\Pi_m|\le W+o(W)\), so the collar
term is \(O(HW/m)=o(W)\).  The whole expression is therefore \(W+o(W)\).

A stronger but convenient version asks for pairwise disjoint middle
supports.  Then \(C_0=0\), and **no condition at all on the owner leave is
needed**.  Rank-\((m-q_0)\) capacity merely forces

\[
 |\Pi_m|\ge \frac{N_{q_0}-o(W)}{2m},
\]

so the natural scale is a constant-density partial packing, not
\((1-o(1))W/(2m)\).

If some separate architecture insists on an exact or near-exact middle
factor, then the source's condition \(R=o(W)\) remains a legitimate
interface hypothesis.  It is not, however, required by Proposition 5.1's
literal compiler and should not be described as the exact minimal gate.

## 6. Final status

What is genuinely established is a useful statewise fact: one ordinary
cyclic-order packet can carry \(\Theta(\sqrt m)\) locally re-framed product
atoms while paying one \(O(\sqrt m)\) collar, hence only \(O(1)\) collar
per atom on average.

What is not established is any integral rounding or annular dispersion.
The orbit equations are the pre-existing exact fractional cyclic-order
design.  After the correction above, the live integrality question is a
constant-density partial cyclic-interval packing with \(o(W)\) aggregate
Gaussian-annulus holes.  That is weaker than a near wreath factor, but it
remains the substantive unsolved step.
