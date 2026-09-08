# Audit and sharpening of the two-phase PBBS chronology fork

Date: 2026-07-25  
Method: pure mathematics only; no computation or search

Audited report:
`MATH_ATTACK_OCR_TWO_TRANSPORTED_PHASE_CHRONOLOGY_FORK_20260725.md`.

## 0. Verdict

The free-monoid dichotomy, all staircase-length identities, the forbidden
window, and the nested forced-jump conclusion are correct.  One notation
repair is required in the definition of the outer-collar length:

\[
 \boxed{
 B_{t,u}
 =\sum_{0\le j<t}(|T_j|+1)
  +\sum_{u<j<s}(|S_j|+1).}                         \tag{0.1}
\]

The upper restriction (j<s) is essential: (S_s) is not part of this
ledger.  With (0.1), the number of summands is exactly

\[
 t+(s-u-1)=s-(u-t)-1=:S.                          \tag{0.2}
\]

The exact identity is

\[
 \boxed{\Delta=B_{t,u}-\Lambda,}                  \tag{0.3}
\]

and every compatible phase pair satisfies

\[
 \boxed{|B_{t,u}-\Lambda|\ge S.}                  \tag{0.4}
\]

For a nested scan which deletes one outer phase at each step, (B_r) is
strictly increasing and the branch can change at most once.  It starts in
the overlap branch and, if it changes between (r-1) and (r), the newly
added block has length at least (2r-1).

There is a useful strengthening.  At such a transition, among the first
(r) omitted collar blocks there is one of length at least

\[
 \boxed{
 \max\{r,\Lambda/r\}
 \ge\sqrt\Lambda.}                                \tag{0.5}
\]

Thus every transition in the large-overlap residual canonically exposes a
diverging block.  Under the critical law, a **prescribed** capped Dyck
block of bit length at least (L-1) has mass (O(L^{-1/2})).  The block in
(0.5) therefore carries a marked cost (O(\Lambda^{-1/4})).  This does not
yet give an unmarked coefficient bound: the large block may occupy any of
up to (s) staircase positions, and multiplying by that position count
can erase the gain.  A position-free injection or a joint rank
anti-concentration theorem is still needed.

If no transition occurs by the adjacent-phase interval, the report's
bound

\[
 \Lambda\ge2(s-2)                                  \tag{0.6}
\]

is exact.  Hence the remaining chronology fork is now:

1. a unique transition with a canonically exposed block of length at least
   (\sqrt\Lambda); or
2. persistent overlap through adjacent phases, forcing
   (\Lambda\ge2(s-2)) and a macroscopic positive-net bridge.

No coefficient-one conclusion follows.

## 1. Reset and phase-equivalence scope

The phase seam events satisfy

\[
 E_j:=\{P_j=Q_jV_j\}.
\]

From

\[
 Q_{j+1}=S_j1Q_j,
 \qquad
 V_j=V_{j+1}1\overline T_j,
 \qquad
 S_j1P_j=P_{j+1}1\overline T_j,
\]

left and right cancellation give

\[
 E_j\Longleftrightarrow E_{j+1}.                  \tag{1.1}
\]

Thus (E_t\) and (E_u) are the same literal constraint once the
intervening local identities are retained.  At either phase, the terminal
reset accepts every record state actually generated at that phase.
Consequently the two terminal sink indicators do not multiply.

The report's notation

\[
 \Theta_{t,u}^{-1}(Q_u^{\rm real})=Q_t^{\rm real}
\]

should be read as a statement about deterministic transport of **marked
words**, not as an assertion that the two unlabeled numerical record-value
sets are equal.  The indicator conclusion remains correct: conditional on
the two incoming-reset events, every word satisfying one phase's local
identities is accepted by both terminal resets.

No relation between the two incoming reset records is proved, and the
source intersection remains a genuine possible source of gain.

## 2. Free-monoid dichotomy

For (d=u-t), put

\[
 A=(\overline T_{u-1}0)\cdots(\overline T_t0),
 \qquad
 C=(0S_u)\cdots(0S_{t+1}).                        \tag{2.1}
\]

Then

\[
 \operatorname{net}(A)=\operatorname{net}(C)=-d,
 \qquad
 \operatorname{net}(R_t)=\operatorname{net}(R_u)=1-s.\tag{2.2}
\]

The transported equation is

\[
 AR_t=R_uC.                                        \tag{2.3}
\]

Length equality defines

\[
 \Delta=|R_u|-|A|=|R_t|-|C|.                     \tag{2.4}
\]

If \(\Delta\ge0\), prefix cancellation gives the unique word (Z) with

\[
 R_u=AZ,
 \qquad R_t=ZC,
 \qquad \operatorname{net}(Z)=-(s-d-1).          \tag{2.5}
\]

Under the explicit based-legality conditions on (A,C), (Z) is exactly
a corridor of height (S=s-d-1), with series

\[
 G_S(x)={x^S\over F_{S+1}(x^2)}.                 \tag{2.6}
\]

If \(\Delta=-r<0\), suffix/prefix overlap gives the unique (H) with

\[
 A=R_uH,
 \qquad C=HR_t,
 \qquad |H|=r,
 \qquad \operatorname{net}(H)=S.                 \tag{2.7}
\]

Therefore (r\ge S) and (r\equiv S\pmod2).  Every claim in the report's
Section 2 passes.

## 3. Staircase-length audit

Put

\[
 d_j=|S_j|+1,
 \qquad L_h=\sum_{j<h}d_j,
 \qquad M_h=\delta(D_h)-L_h,
 \qquad e_h=M_h-M_{h+1}=|T_h|+1.                 \tag{3.1}
\]

Zero winding gives

\[
 L_s=\delta(D_s),
 \qquad M_0=\delta(D_0),
 \qquad M_s=0.                                    \tag{3.2}
\]

The canonical factorization has the exact length ledger

\[
 2m=\delta(D_h)+|R_h|+d_h
    =L_{h+1}+M_h+|R_h|,
\]

so

\[
 \boxed{|R_h|=2m-L_{h+1}-M_h.}                   \tag{3.3}
\]

The transported collars have lengths

\[
 |A|=\sum_{j=t}^{u-1}e_j=M_t-M_u,                \tag{3.4}
\]

\[
 |C|=\sum_{j=t+1}^{u}d_j=L_{u+1}-L_{t+1}.        \tag{3.5}
\]

Substitution into (2.4) yields

\[
 \Delta=2m-L_{u+1}-M_t.                           \tag{3.6}
\]

On the other hand,

\[
 \Lambda=M_0+L_s-2m,                              \tag{3.7}
\]

and the corrected outer ledger (0.1) is

\[
 B_{t,u}=(M_0-M_t)+(L_s-L_{u+1}).                 \tag{3.8}
\]

Subtracting (3.7) from (3.8) gives (3.6), proving (0.3) with every
endpoint index exact.

There are (S) terms in (0.1), each at least one, so

\[
 B_{t,u}\ge S.                                    \tag{3.9}
\]

If \(\Delta\ge0\), the common middle has length

\[
 |Z|=B_{t,u}-\Lambda\ge S.
\]

If \(\Delta<0\), the bridge has length

\[
 |H|=\Lambda-B_{t,u}\ge S,
\]

and hence \(\Lambda\ge B_{t,u}+S\ge2S\).  This proves the forbidden
window and overlap ledger.

## 4. Nested scan and the strengthened large-block certificate

Start at

\[
 [t_0,u_0]=[0,s-1].
\]

At step (r), delete one outer phase, so

\[
 S_r=t_r+(s-u_r-1)=r.                              \tag{4.1}
\]

Every step adds exactly one positive block length to (B_r): either

\[
 e_{t_{r-1}}=|T_{t_{r-1}}|+1
\]

or

\[
 d_{u_{r-1}}=|S_{u_{r-1}}|+1.
\]

Thus (B_0=0) and (B_r) is strictly increasing.  Since
\(\Lambda>0\), the initial branch is overlap.  Once

\[
 B_r\ge\Lambda+r,
\]

the next inequality

\[
 B_{r+1}\ge B_r+1\ge\Lambda+r+1
\]

shows that every later interval remains nonoverlap.  Hence there is at
most one transition.

If it occurs between (r-1) and (r), then

\[
 B_{r-1}\le\Lambda-(r-1),
 \qquad
 B_r\ge\Lambda+r,
\]

and therefore

\[
 \boxed{B_r-B_{r-1}\ge2r-1.}                     \tag{4.2}
\]

This verifies the report's forced-jump formula.

For the sharpening, let \(\ell_1,\ldots,\ell_r\) be the first (r)
added collar lengths.  Then

\[
 \max_{i\le r}\ell_i
 \ge\ell_r\ge2r-1\ge r                           \tag{4.3}
\]

and also

\[
 \max_{i\le r}\ell_i
 \ge{B_r\over r}
 \ge{\Lambda+r\over r}
 \ge{\Lambda\over r}.                            \tag{4.4}
\]

Equations (4.3)--(4.4) prove (0.5).

If no transition occurs through (r=s-2), then

\[
 B_{s-2}\le\Lambda-(s-2),
 \qquad B_{s-2}\ge s-2,
\]

which gives (0.6).

## 5. Marked critical tail of the forced block

Let (D) be any capped Dyck word under its normalized critical Boltzmann
law.  Since the cap only removes words and its partition function is at
least one,

\[
 \Pr(|D|\ge2n)
 \le\sum_{j\ge n}\operatorname{Cat}_j4^{-j}.      \tag{5.1}
\]

The standard Catalan bound

\[
 \operatorname{Cat}_j4^{-j}\le C(j+1)^{-3/2}
\]

gives

\[
 \boxed{\Pr(|D|\ge2n)\le {C\over\sqrt{n+1}}.}    \tag{5.2}
\]

By (0.5), a canonically marked large block has bit length at least
\(\sqrt\Lambda-1\).  Formula (5.2) gives critical mass

\[
 O(\Lambda^{-1/4}).                                \tag{5.3}
\]

This is a genuine vanishing factor in the large-overlap residual
\(\Lambda\to\infty\), but only for a prescribed/marked block.  Promoting
(5.3) to the required coefficientwise root bound must avoid a raw union
over the (s) possible staircase positions and must preserve the common
outer-carrier rank ledger.

That marked-to-unmarked step is the exact strengthened boundary.

## 6. Positive-net bridge penalty

The later bridge estimate in the attack report is also correct.  For a
fixed bridge length (r) and positive net height (S),

\[
 2^{-r}\#\{H:|H|=r,\ \operatorname{net}(H)=S\}
 =2^{-r}\binom r{(r+S)/2}
 \le e^{-S^2/(2r)}.
\]

The equality is the Rademacher endpoint probability, and the inequality
follows by bounding the atom by the upper tail and applying Hoeffding.
The two collar constraints can only reduce this mass.  Therefore
(r=o(S^2)) gives a uniform (o(1)) bridge factor.  In particular, if
(S\ge\varepsilon s) and (\Lambda=o(s^2)), then
(r=\Lambda-B_{t,u}\le\Lambda=o(S^2)).

This conclusion is only for the literal bridge piece, counted once.  A
full coefficient bound still needs a disjoint assembly with the collars
and external kernels; the attack report states this qualification
correctly.
