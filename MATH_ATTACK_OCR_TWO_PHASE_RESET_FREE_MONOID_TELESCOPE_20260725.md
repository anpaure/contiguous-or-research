# OCR with two transported phases: reset acceptance telescopes in the free monoid

Date: 2026-07-25  
Method: pure mathematics only; no computation, search, or solver

## 0. Result

Two transported PBBS phases do not supply two independent *terminal
sink* conditions.  On the exact local-transition language, their seam
factorizations are equivalent by literal cancellation.  Their record
coordinates need not have the same numerical maximum.  Once a phase's
incoming record lies below its first-passage depth, its terminal
first-passage word resets every record value which that phase's renewal
segment can produce.

More precisely, if \(\mathscr L_{t,u}\) is any weighted language on which
all PBBS local word identities from phases \(t\) through \(u\) are
retained, let \(E_j\) be its seam event and let
\(I_j=\{p_j^{\rm in}\le b_j\}\) be its source-reset event.  Terminal
sink acceptance adds no further condition after \(I_j\); write
\(A_j=E_j\cap I_j\).  Then

\[
 \boxed{
 \mathbf1_{E_t\cap E_u}=\mathbf1_{E_t}=\mathbf1_{E_u},
 \qquad
 \mathbf1_{A_t\cap A_u}
 =\mathbf1_{E_t}\mathbf1_{I_t}\mathbf1_{I_u}.}
 \tag{0.1}
\]

Consequently, if both source-reset events hold throughout a chosen
subclass, then coefficientwise

\[
 \boxed{
 Z_{t,u}^{\rm joint}(x)=Z_t(x)=Z_u(x).}
 \tag{0.2}
\]

There is no product of two reciprocal-height factors and no second
reset projection.  In a common-atom renewal relaxation, (0.2) is the
product-poset telescope and leaves the exact scalar factor

\[
 \frac1{1-\rho_{s,v}(x)};
 \tag{0.3}
\]

at \(x=1/2\) its mass is \(\Theta(s)\) for a central seam.  For genuinely
interlaced atomizations, (0.1) still shows that terminal sinks impose no
further restriction.  A gain can come only from the joint source event
\(I_t\cap I_u\), or from the prior question whether a formal phase-\(t\)
corridor admits the full transported PBBS block identities at phase
\(u\).

Thus two terminal resets do not multiply.  This note does not identify
the relation between \(p_t^{\rm in}\) and \(p_u^{\rm in}\); their joint
source-reset event is the exact surviving two-phase reset question.

## 1. Exact adjacent-phase equations

For a genuine zero-winding return, retain the canonical words

\[
 D_j=P_j1R_j0S_j.
\]

Put

\[
 Q_j=(S_{j-1}1)(S_{j-2}1)\cdots(S_01)
 \tag{1.1}
\]

and

\[
 V_j=(\overline T_{s-1}1)\cdots
      (\overline T_{j+1}1)\overline T_j.
 \tag{1.2}
\]

The exact forward and dual recursions are

\[
 Q_{j+1}=S_j1Q_j,
 \qquad
 V_j=V_{j+1}1\overline T_j,
 \tag{1.3}
\]

and the literal local transition is

\[
 \boxed{S_j1P_j=P_{j+1}1\overline T_j.}
 \tag{1.4}
\]

Define the phase seam event

\[
 E_j:\quad P_j=Q_jV_j.
 \tag{1.5}
\]

### Lemma 1.1 (adjacent seam equivalence)

On the free-monoid language satisfying (1.3)--(1.4),

\[
 \boxed{E_j\Longleftrightarrow E_{j+1}.}
 \tag{1.6}
\]

#### Proof

If \(P_j=Q_jV_j\), then by (1.3)--(1.4),

\[
 \begin{aligned}
 P_{j+1}1\overline T_j
 &=S_j1P_j\\
 &=S_j1Q_jV_j\\
 &=Q_{j+1}V_{j+1}1\overline T_j.
 \end{aligned}
\]

Right cancellation gives \(P_{j+1}=Q_{j+1}V_{j+1}\).  Conversely,
substitute the latter equality into (1.4), use (1.3), and left-cancel
\(S_j1\). \(\square\)

Iteration gives

\[
 \boxed{E_t\Longleftrightarrow E_u\qquad(0\le t<u<s).}
 \tag{1.7}
\]

In particular, if \(w(\xi)\) is any nonnegative weight on the exact
transition language, then

\[
 \sum_{\xi}w(\xi)\mathbf1_{E_t(\xi)}
                    \mathbf1_{E_u(\xi)}
 =\sum_{\xi}w(\xi)\mathbf1_{E_t(\xi)}.
 \tag{1.8}
\]

This is coefficientwise when \(w(\xi)=x^{|\xi|}\).  It is not an
asymptotic correlation estimate; the second indicator is literally the
first one transported through a cancellative word identity.

## 2. The transported terminal equation

The terminal words satisfy

\[
 \boxed{\overline T_j0R_j=R_{j+1}0S_{j+1}.}
 \tag{2.1}
\]

Iterating from \(t\) to \(u-1\) gives

\[
 \boxed{
 \mathcal A_{t,u}R_t=R_u\mathcal C_{t,u},}
 \tag{2.2}
\]

where

\[
 \mathcal A_{t,u}
 = (\overline T_{u-1}0)\cdots(\overline T_t0),
 \qquad
 \mathcal C_{t,u}
 = (0S_u)\cdots(0S_{t+1}).
 \tag{2.3}
\]

Thus the phase-\(u\) terminal carrier is a literal rebracketing of the
phase-\(t\) data.  The two record parsings may have interlaced block
boundaries, and their record maxima can differ.  Equation (2.2) does not
assert equality of those scalar maxima.  It asserts something stronger
and more relevant to acceptance: once the intervening block words are
fixed, the second parser is a deterministic function of the same literal
carrier.

## 3. Reset sinks accept the entire physical range

Fix a height seam in a terminal corridor.  In forward order write the
corridor as

\[
 F_A0
 (L_11U_10)\cdots(L_k1U_k0)F_b,
 \tag{3.1}
\]

where \(A+b=s-1\).  In reversed carrier order it is

\[
 \operatorname{rev}F_b
 (0\operatorname{rev}U_k1\operatorname{rev}L_k)
 \cdots
 (0\operatorname{rev}U_11\operatorname{rev}L_1)
 0\operatorname{rev}F_A.
 \tag{3.2}
\]

The first word resets every incoming record height at most \(b\) to
zero.  The renewal segment can then produce only record heights
\(0\le q\le A+1\).  The final word
\(0\operatorname{rev}F_A\) resets every such \(q\) to zero.  This is the
record-reset lemma: a word of net \(-d\), all of whose prefix nets are at
least \(-d\), sends every incoming height at most \(d\) to a terminal
record.

Conditional on the source event \(I_j\), let \(S_j^{\rm rec}\) denote
the set of phase-\(j\) intermediate record states accepted by the
physical terminal word.  The preceding paragraph proves

\[
 \boxed{S_j^{\rm rec}=\{
   \hbox{every record state generated by the phase-}j
   \hbox{ renewal segment}\}.}
 \tag{3.3}
\]

Therefore, if \(\Theta_{t,u}\) is the deterministic transported parsing
defined by (1.3)--(1.4) and (2.1), then on \(I_t\cap I_u\),

\[
 \boxed{
 \Theta_{t,u}^{-1}(S_u^{\rm rec})
 =S_t^{\rm rec}=\mathscr L_{t,u}.}
 \tag{3.4}
\]

The notation in (3.4) means acceptance sets inside the exact common-base
transition language after both source conditions have been imposed.  It
does not claim that the two numerical incoming or intermediate record
coordinates agree.

Combining (1.7) and (3.4) proves (0.1)--(0.2).

## 4. Exact mass in a common-atom renewal model

Suppose first that the two transported scans have a common sequence of
renewal atoms \(\omega_1,\omega_2,\ldots\), and restrict to a subclass
on which both source conditions hold.  Let

\[
 h(\omega)=(h_t(\omega),h_u(\omega))
\]

be their two record depths, and put

\[
 K(a,b)=\sum_{h_t(\omega)\le a,\,h_u(\omega)\le b}w(\omega).
 \tag{4.1}
\]

After any number of atoms, the joint state is the coordinatewise maximum
of the feature vectors.  Möbius inversion on the product of the two
chains gives the exact-state Green series.  Summing over the full reset
rectangle telescopes to its top cumulative value:

\[
 \boxed{
 \sum_{a,b}G(a,b)
 =\frac1{1-K(A_t,A_u)}.}
 \tag{4.2}
\]

Every atom lies below the two physical strip depths, so

\[
 K(A_t,A_u)=\sum_{\omega}w(\omega)=\rho.
\]

Thus (4.2) is exactly (0.3).  At a central seam,

\[
 \rho(1/2)=1-\Theta(1/s),
 \qquad
 (1-\rho(1/2))^{-1}=\Theta(s).
 \tag{4.3}
\]

## 5. What interlacing can and cannot do

If the two phase atomizations interlace, the product-poset computation in
Section 4 is unavailable without enlarging the state to remember the
currently open atoms.  Equations (1.7) and (3.4) remain literal after
\(I_t\cap I_u\): every transported intermediate state produced by an
exact common-base word is then accepted at both terminal sinks.

Accordingly, interlacing can help through the joint source condition, or
earlier by making the set

\[
 \mathscr L_{t,u}
 =\{\hbox{phase-}t\hbox{ formal corridors which admit all transported
 phase-}u\hbox{ PBBS block identities}\}
 \tag{5.1}
\]

small inside the one-phase corridor language.  Once a word belongs to
\(\mathscr L_{t,u}\) and satisfies \(I_t\cap I_u\), applying both
terminal sink predicates removes nothing further.

Thus the exact remaining two-phase statement is either a joint
source-reset bound, or the coefficientwise transported-compatibility
bound

\[
 \boxed{
 [x^{2m}]\,\mathscr L_{t,u}(x)
 =o\bigl([x^{2m}]\,\mathscr L_t(x)\bigr)}
 \tag{5.2}
\]

on the critical Gaussian band, or an equivalent aggregate packing
version.  The free-monoid equations telescope the seam and terminal-sink
conditions, but neither relate \(p_t^{\rm in}\) to \(p_u^{\rm in}\) nor
prove (5.2).

No coefficient-one conclusion is claimed.
