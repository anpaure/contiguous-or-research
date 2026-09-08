# Two transported PBBS phases do not give a second record projection

Date: 2026-07-25  \
Method: pure mathematics only

## 0. Verdict

For the exact phase-transition identities, the factorization condition at
two phases is the **same condition transported through a bijective word
update**.  It is not two independent constraints.  The transported tail
equation is likewise an iterate of the one-step tail identities.

At the record-transfer level the same fact appears as a reset/sink
identity.  At each phase, the initial first-passage piece resets the record
to zero and the terminal first-passage piece accepts every intermediate
record.  The acceptance operator on the intermediate record coordinate is
therefore the identity.  Transporting it to a second phase and intersecting
the two accepted state sets still gives the identity, not a projection of
small mass.

Consequently the exact two-phase word equalities alone retain the scalar
Green mass \(\Theta(s)\).  Any genuine two-phase gain must use a new
canonical/geometric condition not implied by the phase updates (for
example, a non-aligned first-hit restriction proved from PBBS chronology).

## 1. Exact algebraic redundancy of phase factorizations

Suppose for \(t\le j<u\) that

\[
 Q_{j+1}=S_j1Q_j,\qquad
 V_j=V_{j+1}1\overline T_j,
\tag{1.1}
\]

and

\[
 S_j1P_j=P_{j+1}1\overline T_j.
\tag{1.2}
\]

Let

\[
 \mathcal E_j:=\{P_j=Q_jV_j\}.
\]

### Theorem 1.1 (phase transport)

\[
 \boxed{\mathcal E_t\Longleftrightarrow\mathcal E_u.}
\tag{1.3}
\]

In fact \(\mathcal E_j\Longleftrightarrow\mathcal E_{j+1}\) at every
step.

#### Proof

If \(P_j=Q_jV_j\), then (1.1)--(1.2) give

\[
 P_{j+1}1\overline T_j
 =S_j1Q_jV_j
 =Q_{j+1}V_{j+1}1\overline T_j.
\]

Right cancellation in the free monoid gives
\(P_{j+1}=Q_{j+1}V_{j+1}\).  Conversely, substitute the latter equality
in (1.2), use (1.1), and left-cancel \(S_j1\).  Iteration proves (1.3).
\(\square\)

Equivalently, if \(\mathcal T_{t,u}\) denotes the exact phase update on
the full word state and \(\Pi_j\) is the indicator of \(\mathcal E_j\),
then

\[
 \Pi_u\mathcal T_{t,u}=\mathcal T_{t,u}\Pi_t.
\tag{1.4}
\]

Thus on the exact phase fibre,

\[
 \Pi_t\mathcal T_{t,u}^{-1}\Pi_u
 \mathcal T_{t,u}\Pi_t=\Pi_t.
\tag{1.5}
\]

The second phase contributes no additional projection.

## 2. The transported tail equation is already an iterate

The one-step tail identity is

\[
 \overline T_j0R_j=R_{j+1}0S_{j+1}.
\tag{2.1}
\]

Multiplying (2.1) from \(j=t\) through \(u-1\) and cancelling the
intermediate tails yields

\[
 \boxed{
 \mathcal A_{t,u}R_t=R_u\mathcal C_{t,u},}
\tag{2.2}
\]

where

\[
 \mathcal A_{t,u}
 =(\overline T_{u-1}0)\cdots(\overline T_t0),
 \qquad
 \mathcal C_{t,u}
 =(0S_u)\cdots(0S_{t+1}).
\tag{2.3}
\]

Therefore (2.2) is not an independent event after the exact one-step
updates are imposed.  Treating (2.2) as a second statistically independent
carrier collision double-counts the same word equality.

This does not say that (2.2) is useless in a coarser relaxation.  It is a
compact way to retain all the intervening updates.  It says only that its
gain must come from a new geometric restriction on its solutions, not
from multiplying two phase-collision probabilities.

## 3. Record resets make the phase sink the identity

Fix a seam at height \(u\), put \(A=s-u\), \(b=u-1\), and write the
reversed corridor in the exact form

\[
 \operatorname{rev}F_b\,
 (0\operatorname{rev}U_k1\operatorname{rev}L_k)\cdots
 (0\operatorname{rev}U_11\operatorname{rev}L_1)\,
 0\operatorname{rev}F_A.
\tag{3.1}
\]

The first word resets every admissible incoming record \(p\le b\) to
zero.  The middle renewal pairs produce a running-maximum record
\(q\in\{0,\ldots,A+1\}\).  The last word has all prefix nets at least
\(-(A+1)\), has total net \(-(A+1)\), and hence resets every one of those
states to zero.  In particular, every intermediate \(q\) is accepted.

Let

\[
 \widehat\lambda_q=zC_bC_{q-1}\quad(q\ge1),
 \qquad \widehat\lambda_0=0.
\]

The exact Green entries are

\[
 \widehat G_{0,0}=1,\qquad
 \widehat G_{0,q}
 ={1\over1-\widehat\lambda_q}
  -{1\over1-\widehat\lambda_{q-1}}\quad(q\ge1).
\tag{3.2}
\]

Because the sink is the all-ones functional on the record states,

\[
 \boxed{
 \mathbf 1^{\!*}\widehat G e_0
 =\sum_{q=0}^{A+1}\widehat G_{0,q}
 ={1\over1-zC_bC_A}.}
\tag{3.3}
\]

At \(z=1/4\), for \(A,b\asymp s\), this is \(\Theta(s)\).

Now transport to any second exact phase.  Its reset/sink operator is again
the identity on every state which arises from the exact update.  In the
intertwining notation of (1.4), if \(\mathsf A_j=I\) is record acceptance
at phase \(j\), then

\[
 \mathsf A_t\mathcal T_{t,u}^{-1}\mathsf A_u
 \mathcal T_{t,u}\mathsf A_t=I.
\tag{3.4}
\]

Hence the intersection of the two accepted intermediate-state sets is the
entire transported state fibre.  It cannot have \(o(s)\) mass merely from
the two resets.

## 4. A direct critical-mass check

At the critical point, for \(q\ge1\),

\[
 \widehat G_{0,q}(1/4)
 ={(b+2)(b+1)\over(b+q+2)(b+q+1)}.
\tag{4.1}
\]

If \(A,b\asymp s\), choose any fixed
\(0<\alpha<\beta<\min\{A/s,1\}\).  For every
\(\alpha s\le q\le\beta s\), (4.1) is bounded above and below by positive
constants depending only on the centrality parameters.  There are
\(\Theta(s)\) such states.  Both phase reset/sink conditions accept all
of them.  Thus their common accepted record mass is already

\[
 \Omega(s).
\tag{4.2}
\]

The matching upper bound follows from (3.3).  Therefore the exact
reset-compatible two-phase record relaxation has mass

\[
 \boxed{\Theta(s),}
\tag{4.3}
\]

not \(o(s)\).

## 5. Exact scope of the obstruction

The theorem rules out the following proposed inference:

> impose the carrier equality at one phase, transport it to a second phase,
> and multiply the two record-state restrictions.

The two restrictions are conjugate copies of the same condition, and the
first-passage pieces accept all intermediate records.

The theorem does **not** rule out a genuinely new two-phase PBBS lemma.
Such a lemma would have to prove that simultaneous *canonical geometry*
at the two phases excludes almost all of the central records in (4.1), or
that quotient-edge-disjointness cannot pack the corresponding scalar
Green words.  Neither conclusion follows from (1.1)--(2.3) themselves.

