# Independent audit of `GLOBAL_PORTAL_CONSTRUCTION_AFTER_DRAY_20260724.md`

Date: 2026-07-25

## Verdict

**PASS AFTER ONE MATERIAL SCOPE CORRECTION AND TWO CLARIFICATIONS.**

The probabilistic collision theorem, the SCD and target-family counts, the
collision-to-incidence conversion, the literal common-endpoint word, the
central-band endpoint lower bound, and the arm-start identity are all
correct.  They prove the advertised theorem-level conclusion:

\[
 \Theta_\varepsilon(W/\sqrt k)
 \quad\hbox{literal right endpoints can carry}\quad
 \Theta(\varepsilon W)
\]

useful endpoint--product-box incidences in a word of length at most
\(\varepsilon W\), while any near-width universal word needs
\(\Omega(W/\sqrt k)\) physical positions supporting its forced central-band
endpoint sharing.

The original fusion discussion did contain one genuine overstatement.  A
legal one-update transition between full core-leading flags need not be a
canonical rotor exchange with \(y\in R\).  The general necessary conclusion
proved there is Johnson adjacency of the two cores.  The delayed identity
(7.8) is exact only for the canonical rotor subclass.  I patched the source
to make this distinction explicit.  This correction does not touch any of
Sections 1--6 or the portal construction itself.

I also patched two points of exposition:

1. "distinct product boxes" in the opening verdict now explicitly means
   distinct boxes **within each endpoint flag**; boxes may of course recur
   at different physical endpoints;
2. the source now includes the short averaging argument which extracts
   \(\Theta(W/\sqrt k)\) genuinely high-incidence,
   radius-\(\Theta(\sqrt k)\) flags from Theorem 4.1.

No web source, self-audit assertion, or finite computation is used in this
audit.

---

## 1. Product-box cover counts

Let a product box be the product of three saturated factor chains.  If
\(S\) belongs to that box, an upper Boolean cover can advance at most one
of the three factor-chain coordinates, so at most three upper neighbours
remain in the box.

If \(S\notin\mathcal B\) and two distinct upper neighbours \(S+x,S+y\)
were in \(\mathcal B\), then:

* when \(x,y\) are in one coordinate block, one factor chain would contain
  two different sets at the same rank;
* when they are in different blocks, the unchanged block components seen
  in the two neighbours force all three components of \(S\) into the three
  factor chains, contrary to \(S\notin\mathcal B\).

Thus Lemma 1.1 is exact.  At the \(t\)-th greedy step of Corollary 1.2,
at most \(3+t\) upper neighbours return to the \(t+1\) boxes already used,
whereas the number of upper neighbours is \(k-a-t\).  The assumed inequality

\[
 k-a>2L+1
\]

gives \(k-a-t>t+3\) for every \(t\le L-1\).  The greedy flag proof is
therefore valid, including its strict inequality at the last step.

---

## 2. Random relabeling and the same-box probability

An SCD of \(B_k\), for even \(k\), has exactly
\(W=\binom{k}{k/2}\) chains because every symmetric chain contains exactly
one middle-layer set.

Fix a comparable pair \(S\subset T\), with \(|S|=r\) and
\(|T\setminus S|=d\).  Conditional on the exact image \(\sigma S=A\), the
image of \(T\setminus S\) under a uniform coordinate permutation is a
uniform \(d\)-subset of \([k]\setminus A\).  Hence \(\sigma T\) is uniform
over the \(\binom{k-r}{d}\) rank-\(r+d\) supersets of \(A\).

Inside the unique product box containing \(A\), an extension by \(d\)
ranks is determined by a nonnegative triple of factor-chain advances with
sum \(d\).  There are \(\binom{d+2}{2}\) such triples, and infeasible triples
only reduce the count.  Therefore

\[
 \Pr(\sigma S,\sigma T\hbox{ are in one product box})
 \le {\binom{d+2}{2}\over\binom{k-r}{d}}
\]

is correct for arbitrary factor SCDs and translated box bottoms.

At fixed ranks \(r,r+d\), each global SCD chain contributes at most one
pair, so the number of pairs is at most \(W\), not \(W^2\).  This verifies
the multiplicity in (2.7).

For

\[
 a_d={\binom{d+2}{2}\over\binom Kd},\qquad K=k-r,
\]

direct cancellation gives

\[
 {a_{d+1}\over a_d}={d+3\over K-d}.
\]

In the stated range, \(K\ge5k/12\) and \(d\le2H\le k/6\), so the ratio is
at most \(3/4\) for all sufficiently large \(k\).  Since \(a_1=3/K=O(1/k)\),
the full \(d\)-sum is \(O(1/k)\).  There are \(O(H)\) lower ranks.  Thus

\[
 \mathbb E\operatorname{Col}_H=O(HW/k)
\]

and Theorem 2.1 follows by averaging.  No independence between different
pairs is being assumed.

---

## 3. Collision loss converts correctly to box incidence

For a fixed global chain \(D\), if it visits one product box \(u\ge1\)
times in the selected band, the loss from occurrences to distinct boxes is
\(u-1\), while the collision ledger charges \(\binom u2\).  Since

\[
 u-1\le\binom u2,
\]

summing over boxes and global chains gives (2.11).  This also counts
nonconsecutive returns; no chronology assumption is hidden here.

Restriction to a subfamily of targets only deletes occurrence pairs, so the
same collision count bounds the repeated-box loss for \(\mathcal T\).  As
the global SCD chains partition every Boolean mask, the total number of
selected target occurrences is exactly \(|\mathcal T|\).  Consequently

\[
 \sum_Dd_D(\mathcal T)
 \ge |\mathcal T|-\operatorname{Col}_H,
\]

which is precisely (3.4).

---

## 4. Independent check of the target-family size

The number of chains of an \(s\)-cube SCD beginning in rank \(a\), hence of
height \(s-2a\), is forced to be

\[
 \binom sa-\binom s{a-1}.
\]

Summing over a contiguous height window telescopes.  Using

\[
 {\binom{s}{s/2-x\sqrt s}\over W_s}\longrightarrow e^{-2x^2},
\]

the fractions of chains with heights in the low and high windows are

\[
 \kappa_L=e^{-1/2}-e^{-121/200},\qquad
 \kappa_H=e^{-9/2}-e^{-961/200},
\]

respectively.  Thus the number of dominant product boxes is

\[
 (\kappa_L^2\kappa_H+o(1))W_s^3.
\]

For such a box, \(r>p+q\).  Every grid rank from \(p+q\) through \(r\)
has exactly \((p+1)(q+1)\ge s\) points.  The number of these plateau ranks
is

\[
 r-p-q+1\ge0.8\sqrt s+1,
\]

so the deliberately weaker \(0.7\sqrt s\) bound is safe.  Finally,

\[
 {sW_s^3\over W}\to{2\sqrt3\over\pi},\qquad
 {s^{3/2}W_s^3\over W\sqrt k}\to{2\over\pi}
 \quad(k=3s).
\]

It follows that any fixed

\[
 0<\tau<{1.4\over\pi}\kappa_L^2\kappa_H
\]

works eventually in (3.2).  The slab is centered at global rank \(k/2\):
its half-width is \((r-p-q)/2\le0.55\sqrt s<\sqrt k\).  Non-dominant boxes
contribute only their global middle layer.  Hence every target really lies
in the band used in Theorem 2.1.

---

## 5. Selecting a width-budget family

Order the \(W\) global chains by decreasing \(d_D(\mathcal T)\), and set

\[
 P=\left\lfloor{\varepsilon W\over2H+1}\right\rfloor,
 \qquad H=\lceil\sqrt k\rceil.
\]

The mean of the top \(P\) nonnegative values is at least the mean of all
\(W\) values.  Therefore (3.4) gives

\[
 \sum_{i\le P}d_{D_i}(\mathcal T)
 \ge {P\over W}\bigl(\tau W\sqrt k-O(W/\sqrt k)\bigr)
 =\Omega(\varepsilon W).
\]

The floor is harmless because \(W\) is exponential and \(\varepsilon>0\)
is fixed.  Also \(P=\Theta_\varepsilon(W/\sqrt k)\).

Since every selected degree is at most its band length, which is at most
\(2H+1\), the selected average degree is a positive constant times \(H\).
A standard threshold at half this average retains a constant fraction of
the flags and a constant fraction of the incidence.  Every retained flag
has degree, and therefore band length and radius, \(\Theta(\sqrt k)\).  This
justifies the high-incidence formulation used in the final fusion gate.

---

## 6. Literal suffix word

For a saturated segment

\[
 S_a\subset S_{a+1}\subset\cdots\subset S_b,
 \qquad E_t=S_t\setminus S_{t-1},
\]

the block

\[
 E_b,E_{b-1},\ldots,E_{a+1},S_a
\]

has exactly \(b-a+1\) nonempty letters.  The interval beginning at \(E_t\)
and ending at the last position is

\[
 E_t,E_{t-1},\ldots,E_{a+1},S_a,
\]

whose union is exactly \(S_t\).  The target \(S_a\) uses the one-letter
interval at the endpoint.  Because \(a\ge m-H>0\), the core is nonempty;
the other letters are singletons.  Concatenation leaves every internal
certificate contiguous.  Each block has at most \(2H+1\) letters, so the
total length is at most \(\varepsilon W\).

This verifies Theorem 4.1 literally, rather than merely at the state or
incidence level.

---

## 7. Central-band endpoint cap

At a fixed right endpoint, all suffix ORs form an inclusion chain.  At a
fixed left endpoint, the ORs obtained by increasing the right endpoint also
form an inclusion chain.  An inclusion chain contains at most one distinct
set of each cardinality.  Since product boxes partition the masks, choosing
one selected target for each incident box proves

\[
 \ell_j,r_j\le2H+1.
\]

Therefore a physical position contributes at most

\[
 ((2H+1)-1)+((2H+1)-1)=4H
\]

to the endpoint-sharing excess.  Combining this with the already audited
dominant-box ledger

\[
 \mathcal C_\partial\ge2\delta_0W-2(n-W)
\]

gives \(P=\Omega(W/H)=\Omega(W/\sqrt k)\) for a word of length
\(n=W+o(W)\).  The lower bound counts physical positions supporting either
left or right sharing; the construction supplies the same order using
right endpoints.  This is a valid scale comparison.

The box-origin and complement observations are also correct.  Distinct
SCD chains have distinct minima, so distinct product boxes have distinct
embedded origins.  Two nonempty complementary masks are incomparable, so
they cannot both occur in one endpoint's inclusion chain.

---

## 8. Arm-start identity and isolated tax

Fix one designated interval for each designated target.  If \(d_j\) distinct
targets end at the same position \(j\), their left endpoints are distinct:
one ordered endpoint pair determines one interval and hence one OR value.
Thus counting the same set of certificates by right and left endpoints gives
the exact identity

\[
 \sum_{j\in J}d_j=\sum_i s_i.
\]

If all starts lie in an appendage of length \(Q\), and one appendage
position starts at most \(\Delta\) chosen certificates, then

\[
 Q\Delta\ge\sum_jd_j.
\]

For the specifically designated internal suffix certificates of the
isolated blocks, every physical start is used once, so \(\Delta=1\).  Hence
\(Q\ge C+|J|\), where \(C=\sum_j(d_j-1)\).  The qualification "specifically
designated" matters: arbitrary seam-crossing certificates could reuse a
start, but none are invoked in the isolated construction.  The source's
linear isolated-arm tax is therefore exact.

---

## 9. One-update MTF classification and the correction

Let the current last-occurrence partition begin

\[
 L,\{z_1\},\ldots,\{z_h\},\qquad |L|=m-h.
\]

After appending a prospective next core \(X\) of the same size, the new
partition begins

\[
 X,\ L\setminus X,\ \{z_1\}\setminus X,\ldots
\]

after empty blocks are removed.  If the new endpoint exposes a saturated
flag beginning at \(X\), the first nonempty block after \(X\) must be a
singleton.  Therefore \(|L\setminus X|\le1\).  Equal cardinalities imply
that \(L=X\) or \(L,X\) are adjacent in \(J(k,m-h)\).  Equation (7.5) is a
valid necessary condition.

For the canonical full-radius rotor, with

\[
 x_t\in L_t,qquad y_t\in R_t,qquad
 L_{t+1}=L_t-x_t+y_t,
\]

the queue update is

\[
 (z_{t+1,1},\ldots,z_{t+1,2h})
 =(x_t,z_{t,1},\ldots,z_{t,2h-1}).
\]

Consequently

\[
 M_{t+1}=M_t-z_{t,h}+y_t,qquad z_{t,h}=x_{t-h},
\]

and a newly entering coordinate has a middle-membership run of at least
\(h+1\) states.  Equations (7.7)--(7.8) are correct for this rotor subclass.

They are not a classification of every legal MTF transition.  A smallest
counterexample to the original wording has \(m=2,h=1\) and ordered state

\[
 L=\{1\},\quad z_1=2,\quad z_2=3,\quad R=\{4\}.
\]

Appending \(X=\{3\}=L-1+3\) produces the leading state

\[
 \{3\},\{1\},\{2\},\{4\},
\]

which again exposes a full radius-one saturated flag.  But the entering
element \(3\) belonged to the old singleton queue, not to \(R\), so this is
not the canonical rotor successor defined in the note.  A no-change update
\(X=L\) is another legal non-rotor possibility.

The patched source now says exactly what has been proved:

* every such one-update transition obeys the Johnson core condition (7.5);
* the canonical rotor is a rigid sufficient subclass and obeys (7.8);
* the general unresolved fusion target is a legal MTF trajectory, while a
  canonical-rotor extraction is a stronger sufficient version.

---

## 10. Exact surviving status

After the correction above, the note establishes an exact and scale-sharp
**endpoint-incidence** construction.  It does not establish a universal
word, a sublinear appendage, or a rotor extraction.  Its remaining statement
is correctly conditional:

\[
 \boxed{
 \begin{gathered}
 \text{portal existence and within-portal chronology are solved;}\\
 \text{middle-productive MTF fusion of the arms is not.}
 \end{gathered}}
\]

Accordingly, the corrected source is theorem-grade and may be incorporated
into the handoff with status **PASS**.
