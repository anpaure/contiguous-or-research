# Audit of the PBBS all-depth fan theorem and its multiplicity boundary

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, web
input, or asymptotic experiment is used.

Audited reports:

* `MATH_THEOREM_PBBS_Q_FAN_SUPPORT_Q2_AND_GAUSSIAN_MULTIPLICITY_20260726.md`;
* `MATH_ATTACK_AD15_DIRECT_PBBS_ALLQ_EROSION_AUDIT_20260725.md`;
* `PBBS_GENERAL_MARK_LADDER_AUDIT_20260725.md`.

## 0. Verdict

The all-depth lower-support theorem and the correct-fibre cap pass with
their full quantifiers.  For

\[
 n=2m+1,\qquad 1\le q\le m,\qquad
 S\in\binom{[n]}{m-q},
\]

there are consecutive directed states under \(g=f^2\),

\[
 B_0\longrightarrow B_1\longrightarrow\cdots\longrightarrow B_q,
\]

such that

\[
 \bigcap_{t=0}^qB_t=S,
\]

and the number of based correct-rank occurrences satisfies

\[
 \boxed{
 1\le\mu_q^-(S)\le\binom{2q+1}{q}.}
 \tag{0.1}
\]

This is exactly AD15 Theorem 5.1, not a strengthening with hidden extra
hypotheses.  It is valid at \(q=1\), at \(q=m\), and for shared
forward/reverse unmatched coordinates.

Two local proof expansions should be read into Section 4 of the new
theorem report.

1. After the \(C_0,\ldots,C_{r-1}\) flips, the selected
   \(A_0,\ldots,A_{t-1}\) really are still current forward marks.  The
   exact index inequality proving this is recorded in Section 2 below.
2. In the cap proof, every deleted label lies in the original
   \(U_-(S)\) because repeated clean-label contraction gives
   \(U_-(K_t)\subseteq U_-(S)\) for every overlap core.  Section 3 gives
   the complete argument.

These are expository omissions, not gaps in the theorem: both facts were
already explicit in AD15 and follow directly from the lemmas stated in the
new report.

The upper-fan identity

\[
 \mu_q^+(U)=\mu_{q-1}^-(U^c)
 \tag{0.2}
\]

also passes, including multiplicities and wrong-rank correspondence.  The
complete \(q=2\) row and its constants are consistent with the independent
deficit-five audit.

The rotational multiplicity theorem is correct but must not be read as an
exponential obstruction.  It proves, in every fixed Gaussian window, an
actual family with

\[
 \mu_q^-(S)\ge2q+1,
 \tag{0.3}
\]

and therefore refutes an \(O_A(1)\) cap.  It does not refute a polynomial
cap.  No actual PBBS family of superpolynomial, let alone
\(\exp(\Omega(q))\), correct-fan multiplicity is presently proved.

The precise surviving question is therefore

\[
 \max_{q\le A\sqrt m}\max_S\mu_q^-(S)
 \stackrel{?}{\le}m^{O_A(1)}.
 \tag{0.4}
\]

The audited binomial cap is exponential in \(q\), while the proved lower
bound is linear in \(q\).  The interval between them remains open.

## 1. Chronology and the clean-label lemmas

On an oriented \(f\)-orbit, let

\[
 \lambda_i=[n]\setminus(A_i\cup A_{i+1}).
\]

The two-step recurrence is

\[
 A_{i+2}=A_i-\{\lambda_{i+1}\}+\{\lambda_i\}.
 \tag{1.1}
\]

Thus every \(g\)-edge is one Johnson exchange.  For a word of positive
odd deficit \(d\), flipping one zero to one removes two old forward
unmatched marks and two old reverse unmatched marks.  Equivalently, the
new forward set consists of the \(d-2\) old marks immediately preceding
the flipped coordinate, while the reverse set consists of the \(d-2\)
old marks immediately succeeding it.  This is the clean-label deletion
lemma used in both reports.

At a coordinate shared by the two unmatched sets, the expanded order must
be

\[
 C_x,A_x.
 \tag{1.2}
\]

With this convention the global-maximum boundary supplies labels

\[
 C_0,C_1,\ldots,C_{2q},qquad
 A_0,A_1,\ldots,A_{2q}
\]

such that

\[
 x_j\le j,qquad y_j\le j.
 \tag{1.3}
\]

If \(C_j=A_h\) physically, the local order (1.2) gives

\[
 x_j=2q-h,
\]

and hence

\[
 \boxed{C_j=A_h\Longrightarrow j+h\ge2q.}
 \tag{1.4}
\]

This one inequality handles every shared-coordinate issue in the selected
fan.

## 2. Audit of every arrow in the all-depth fan

Define

\[
 P_t=\{C_0,\ldots,C_{q-t-1}\}
      \cup\{A_0,\ldots,A_{t-1}\},
 \qquad B_t=S\cup P_t.
 \tag{2.1}
\]

If a selected \(C_j\) equalled a selected \(A_h\), then

\[
 j+h\le(q-t-1)+(t-1)=q-2,
\]

contradicting (1.4).  Thus \(|P_t|=q\).  A shared coordinate can belong
to every \(P_t\) only if the initial \(C\)-range and terminal \(A\)-range
overlap in time, which is exactly the condition

\[
 j+h\le q-1.
\]

Again (1.4) excludes it.  Therefore

\[
 \bigcap_{t=0}^qP_t=\varnothing,
 \qquad
 \bigcap_{t=0}^qB_t=S.
 \tag{2.2}
\]

Fix \(0\le t<q\), put

\[
 r=q-t-1,
\]

and let

\[
 K_t=S\cup\{C_0,\ldots,C_{r-1}\}
          \cup\{A_0,\ldots,A_{t-1}\}.
 \tag{2.3}
\]

Then

\[
 B_t=K_t\cup\{C_r\},
 \qquad
 B_{t+1}=K_t\cup\{A_t\}.
 \tag{2.4}
\]

Number the original forward marks by

\[
 F_0=A_0,F_1,\ldots,F_{2q},
 \qquad A_h=F_{2q+1-h}\quad(h\ge1).
 \tag{2.5}
\]

The corridor inequality \(x_j\le j\) and clean-label deletion show
inductively that flipping \(C_0,\ldots,C_{r-1}\) removes exactly

\[
 F_1,F_2,\ldots,F_{2r}.
 \tag{2.6}
\]

Here is the survival check left implicit in the new report.  The mark
\(A_0=F_0\) survives (2.6).  For \(1\le h<t\),

\[
 2q+1-h\ge2q-t+2>2q-2t-2=2r.
 \tag{2.7}
\]

Thus every selected \(A_h\) also survives (2.6).  They can consequently
be flipped in the prescribed order.  Each is then a current forward mark:
\(A_0\) removes \(F_0\) and \(F_{2r+1}\), and each following
\(A_h=F_{2q+1-h}\) removes itself at the high-index end and the next
surviving low-index mark.  The three survivors are exactly

\[
 U_+(K_t)=\{A_t,A_{t+1},A_{t+2}\}.
 \tag{2.8}
\]

The reverse calculation, using \(y_j\le j\), gives

\[
 U_-(K_t)=\{C_r,C_{r+1},C_{r+2}\}.
 \tag{2.9}
\]

The same corridor inequalities put \(A_t\) immediately before \(C_r\)
in (2.8) and \(C_r\) immediately after \(A_t\) in (2.9), in the strict
cyclic senses required by the deficit-three law.  Hence

\[
 g(K_t\cup\{C_r\})=K_t\cup\{A_t\}.
 \tag{2.10}
\]

This proves every arrow.  The argument is uniform when \(r=0\), when
\(t=0\), and when \(q=m\).

## 3. Audit of the binomial cap

Let

\[
 D_0\longrightarrow D_1\longrightarrow\cdots\longrightarrow D_q
 \tag{3.1}
\]

be any based correct-rank fan with

\[
 \bigcap_{t=0}^qD_t=S.
\]

Each arrow deletes one coordinate.  Every one of the \(q\) initial extras
in \(D_0\setminus S\) is absent from at least one later state, so each is
deleted at least once.  There are only \(q\) arrows.  Therefore the
deleted labels are exactly those \(q\) distinct initial extras; no
deletion is spent on a label inserted earlier in the fan.

At arrow \(t\), write

\[
 D_t=K_t\cup\{x_t\},
 \qquad
 D_{t+1}=K_t\cup\{y_t\}.
\]

The one-edge criterion gives

\[
 x_t\in U_-(K_t).
 \tag{3.2}
\]

The core \(K_t\) contains \(S\) and has exactly \(q-1\) other
coordinates.  Obtain it from \(S\) by flipping those \(q-1\) zeroes to
ones in any order.  Every clean-label flip replaces the reverse-unmatched
set by a subset of its old value.  Induction gives

\[
 U_-(K_t)\subseteq U_-(S).
 \tag{3.3}
\]

Equations (3.2)--(3.3) show

\[
 D_0\setminus S\subseteq U_-(S).
 \tag{3.4}
\]

The left side is a \(q\)-set, while \(|U_-(S)|=2q+1\).  Its value
determines \(D_0\), and the deterministic permutation \(g\) determines
the entire based fan.  Hence the map

\[
 (D_0,\ldots,D_q)\longmapsto D_0\setminus S
\]

is injective into \(\binom{U_-(S)}q\), proving

\[
 \mu_q^-(S)\le\binom{2q+1}{q}.
 \tag{3.5}
\]

This proves the cap with no uncounted orbit, phase, or orientation
multiplicity.

## 4. Upper fans and the (q=2) row

For consecutive \(f\)-states,

\[
 A_{j+1}=[n]\setminus(A_j\cup A_{j+2}).
\]

Therefore

\[
 [n]\setminus\bigcup_{t=0}^qA_{i+2t}
 =\bigcap_{t=0}^{q-1}A_{i+2t+1}.
 \tag{4.1}
\]

Shifting the based position by one is a bijection, so (4.1) proves (0.2)
with exact multiplicity.

The separate first-to-last maximum calculation in the new report proves
that every lower \(2\)-fan has rank \(m-2\).  This agrees with the
independently audited no-gap-three theorem.  Consequently every upper
\(2\)-fan has rank \(m+2\) by (4.1).  The bounds

\[
 1\le\mu_2^-(S)\le10,
 \qquad
 1\le\mu_2^+(U)\le3
\]

and, for \(m\ge8\),

\[
 Q_2^-<48\operatorname {Cat}_m,
 \qquad
 Q_2^+<2\operatorname {Cat}_m
\]

have the correct floors, constants, and quantifiers.

## 5. Rotational multiplicity

Let the rotational stabilizer of \(S\) have order \(h\).  It acts freely
on the \(n\) coordinates, so

\[
 h\mid n,
 \qquad
 h\mid|S|=m-q.
\]

Consequently

\[
 h\mid n-2(m-q)=2q+1.
 \tag{5.1}
\]

The stabilizer also acts freely on based occurrence roots.  Indeed, if a
nonidentity rotation of order \(d\) fixed an \(m\)-set, then \(d\mid m\),
while \(d\mid n=2m+1\); hence \(d=1\), a contradiction.  Rotation
equivariance of PBBS now gives

\[
 h\mid\mu_q^-(S).
 \tag{5.2}
\]

For odd \(h\), set

\[
 q=\frac{h-1}{2},
 \qquad
 n=hp,
 \qquad
 m=\frac{hp-1}{2},
\]

where \(p\) is odd.  Repeating a primitive length-\(p\) binary block of
weight \((p-1)/2\) exactly \(h\) times gives an \((m-q)\)-target with
stabilizer exactly \(h=2q+1\).  Complete support and (5.2) imply

\[
 \mu_q^-(S)\ge2q+1.
 \tag{5.3}
\]

For every fixed \(A>0\), choosing \(p\) sufficiently large makes

\[
 q^2\le A^2m.
\]

Thus (5.3) genuinely lies in every fixed Gaussian window.  Every
arithmetic and primitivity condition in the construction is necessary and
is satisfied.

## 6. Polynomial normal forms versus exponential multiplicity

Three exact conclusions are available.

First, every occurrence has the injective deletion-set code

\[
 D_0\setminus S\in\binom{U_-(S)}q.
 \tag{6.1}
\]

This is a complete finite normal form, but its state space has cardinality

\[
 \binom{2q+1}{q}
 =\left(\frac{2}{\sqrt{\pi q}}+o(q^{-1/2})\right)4^q.
 \tag{6.2}
\]

It is therefore not a polynomial-count normal form.

Second, not every occurrence is one of the global-maximum corridor
witnesses used in the support proof.  Already at \(m=q=2\) and
\(S=\varnothing\), the expanded mark potential is constant and has five
possible \(C\)-boundaries, so the corridor construction produces at most
five based fans.  But the pointwise \(q=2\) theorem gives

\[
 \mu_2^-(\varnothing)=\binom52=10.
 \tag{6.3}
\]

Thus a normal form consisting only of one selected boundary is false.
Any polynomial classification would need genuinely more information than
the support corridor.

Third, the rotational family proves only the linear lower bound (5.3).
The stabilizer mechanism cannot force more, because (5.1) gives

\[
 h\le2q+1.
\]

Consequently the present rigorous boundary is

\[
 2q+1
 \le
 \sup_{m,S}\mu_q^-(S)
 \le
 \binom{2q+1}{q}
 \tag{6.4}
\]

along suitable growing parameter sequences.  The left side is actual PBBS
multiplicity; the right side is the universal exact cap.

For \(q=O(\log m)\), (6.2) is automatically polynomial in \(m\).  For
\(q\le A\sqrt m\), it is only \(\exp(O_A(\sqrt m))\).  No theorem in the
audited package proves that all deletion-set codes are controlled by
polynomially many boundaries or lattice paths, and no theorem realizes an
exponential number of them for one target.

Hence the honest conclusion is:

\[
 \boxed{
 \text{polynomial Gaussian multiplicity and superpolynomial actual
 multiplicity are both open.}}
 \tag{6.5}
\]

The all-depth support theorem is complete; this multiplicity problem is a
strictly separate gate.

## 7. Exact proved and unproved boundary

### Proved

1. Complete lower support at every \(1\le q\le m\).
2. The exact cap \(\binom{2q+1}{q}\), with no hidden multiplicity.
3. Complete upper support by the cross-shore complement identity.
4. The full lower and upper \(q=2\) row with Catalan collision cost.
5. An actual Gaussian-window family with multiplicity at least \(2q+1\).
6. Failure of a boundary-only classification of all occurrences.

### Unproved

1. A bound \(m^{O_A(1)}\) for all \(q\le A\sqrt m\).
2. Any actual family with superpolynomial or exponential multiplicity.
3. A polynomial-count normal form for arbitrary correct occurrences.

No stronger multiplicity conclusion, positive or negative, follows from
the audited reports.
