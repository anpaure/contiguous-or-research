# Common-core trace fusion: the sharp collision law, span influence, and a conditional reversed-tail obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web
input is used.

## 0. Scope and result

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},
\]

and

\[
 M=m+H,qquad s=m-H,qquad L=m-3H+1.
\tag{0.1}
\]

Assume throughout that

\[
 H=(1+o(1))\sqrt{m\log m},qquad m>5H,qquad
 N_H=(1+o(1)){W\over m}.
\tag{0.2}
\]

For each rank-\(M\) top, a **core-safe tight path** means the literal
\(L\)-phase path of Theorem 2.1 in
`MATH_THEOREM_S_GLOBAL_COMMON_CORE_PROMOTION_ATLAS_20260726.md`.

This report proves:

1. an exact necessary-and-sufficient criterion for two signed traces to
   coincide after complementing their deletion intervals inside different
   tops;
2. the exact relation between a signed collision and the Johnson distance
   of the two middle owners;
3. the sharp deterministic span bound on the number of collisions between
   two physical paths; and
4. a conditional perturbation theorem: **if** one middle-safe path per top
   has already been selected, replacing only
   \(K=\Theta(W/(H\sqrt m))\) top pairs preserves middle defect/leave
   \(o(W)\), while the explicitly constructed reversed-tail gadgets have
   \(\Omega(W)\) activatable upper-trace repeats.

The fourth statement is not an unconditional construction of the assumed
global middle-safe atlas.  Its tag conclusion is stated under the explicit
compensation hypothesis in Theorem 5.2.  What is unconditional is the
two-path collision profile and the \(o(W)\)-mass perturbation bound.

The principal conclusion, in the precise perturbative sense of Theorems
5.1--5.2, is

\[
 \boxed{
 \text{middle collision/leave }o(W)
 \text{ is not a perturbatively robust control of dependent signed traces}.}
\tag{0.3}
\]

Namely, whenever the base class is nonempty, it contains an
\(o(W)\)-mass perturbation with linear untagged signed-collision
potential; when the stated legal compensation reservoir exists, those
collisions can be activated with the chosen exact (or explicitly
\(o(W)\)-deficient) tag census.  Any positive
rounding theorem must therefore control the external-influence functional
in Section 3, or use an additional structural invariant that forbids this
perturbation.

## 1. Exact trace normal form

Fix a top \(U\), a \(2H\)-core \(Q_U\), and an ordered tail

\[
                         w^U=(w^U_1,\ldots,w^U_s)
\tag{1.1}
\]

on \(U\setminus Q_U\).  The retained phases are \(j=1,\ldots,L\).
At signed rank \(m+r\), put

\[
                         \ell=H-r,qquad0\le\ell\le2H.
\tag{1.2}
\]

The deletion interval and target of phase \(j\) are

\[
 I^U_{j,\ell}
 =\{w^U_{j+2H-\ell},\ldots,w^U_{j+2H-1}\},
\qquad
 T^U_{j,\ell}=U\setminus I^U_{j,\ell}.
\tag{1.3}
\]

Thus middle traces have \(\ell=H\), upper-depth-\(q\) traces have
\(\ell=H-q\), and lower-depth-\(q\) traces have \(\ell=H+q\).  As
\(j\) varies, the allowed length-\(\ell\) intervals start at

\[
                         2H-\ell+1,\ldots,s-\ell+1.
\tag{1.4}
\]

### Theorem 1.1 (top-complement collision criterion)

Let \(U,V\) be rank-\(M\) tops and let \(I\subseteq U,J\subseteq V\)
have the same size \(\ell\).  Put

\[
 A=U\setminus V,qquad B=V\setminus U,qquad C=U\cap V,
\]

so \(|A|=|B|=\delta=d_J(U,V)\).  Then

\[
 U\setminus I=V\setminus J
\tag{1.5}
\]

if and only if there is one \(K\subseteq C\), of size \(\ell-\delta\),
such that

\[
                         I=A\mathbin{\dot\cup}K,qquad
                         J=B\mathbin{\dot\cup}K.
\tag{1.6}
\]

#### Proof

Every coordinate in \(A\) must be deleted from the left top, and every
coordinate in \(B\) from the right top.  On \(C\), equality of the
remaining masks is exactly equality of the two deleted subsets.  This
gives (1.6), and equal interval sizes give \(|K|=\ell-\delta\).
The converse is immediate. \(\square\)

In particular,

\[
                         \delta\le\ell,qquad
                         I\triangle J=U\triangle V.
\tag{1.7}
\]

Because core-safe intervals avoid their cores, a collision also requires

\[
                         Q_U\subseteq V,qquad Q_V\subseteq U.
\tag{1.8}
\]

### Theorem 1.2 (signed collision versus middle distance)

Suppose two phases collide at upper depth \(q\), with common target
\(Z\in\binom{[2m]}{m+q}\).  There are \(q\)-sets \(P_U,P_V\subseteq Z\)
such that their middle owners are

\[
                         X_U=Z\setminus P_U,qquad
                         X_V=Z\setminus P_V.
\tag{1.9}
\]

If they collide at lower depth \(q\), with common target
\(Z\in\binom{[2m]}{m-q}\), there are \(q\)-sets outside \(Z\) such that

\[
                         X_U=Z\cup P_U,qquad
                         X_V=Z\cup P_V.
\tag{1.10}
\]

In either case,

\[
 \boxed{
 d_J(X_U,X_V)=q-|P_U\cap P_V|,qquad
 X_U=X_V\Longleftrightarrow P_U=P_V.}
\tag{1.11}
\]

#### Proof

For the upper trace, the middle deletion interval adds the \(q\)
coordinates immediately preceding the shorter upper interval.  Those
coordinates lie in \(Z\), and removing them gives (1.9).  For the lower
trace, the longer deletion interval removes \(q\) coordinates which are
present in the middle owner but absent from \(Z\), giving (1.10).
Taking symmetric differences proves (1.11). \(\square\)

Conversely, two equal middle owners have equal signed traces exactly when
their corresponding ordered \(q\)-blocks agree.  Hence neither middle
equality nor middle inequality determines the signed equality pattern.

## 2. Sharp two-path influence

For \(A\subseteq U\setminus Q_U\), define
\(\operatorname{span}_U(A)\) as the length of its smallest interval in
the linear tail word \(w^U\).  Put the span equal to \(+\infty\) if
\(A\not\subseteq U\setminus Q_U\).  Let \(c_{UV}(\ell)\) count equal
length-\(\ell\) targets between the two paths.

### Theorem 2.1 (sharp span bound)

For distinct tops, with \(A=U\setminus V\), \(B=V\setminus U\),

\[
 \boxed{
 c_{UV}(\ell)
 \le
 \min\left{
  (\ell-\operatorname{span}_U(A)+1)_+,\,
  (\ell-\operatorname{span}_V(B)+1)_+
 \right}
 \le\ell.}
\tag{2.1}
\]

Consequently

\[
                         \sum_{\ell=1}^{2H}c_{UV}(\ell)
                         \le H(2H+1).
\tag{2.2}
\]

#### Proof

Theorem 1.1 forces every colliding left interval to contain all of \(A\).
A set of span \(a\) lies in at most \((\ell-a+1)_+\) length-\(\ell\)
intervals.  For any fixed left interval, (1.6) determines the required
right interval set uniquely.  An injective linear word contains a fixed
set as an equal-length interval at most once.  Apply the same argument on
the right and sum \(1+\cdots+2H\). \(\square\)

The bound \(c_{UV}(\ell)\le\ell\) is sharp simultaneously at all
\(1\le\ell\le2H\), as Section 4 shows.

## 3. The compensated-nibble invariant

For one selected path per top, define

\[
                         \Xi
 =\sum_{\{U,V\}}\sum_{\ell=1}^{2H}c_{UV}(\ell).
\tag{3.1}
\]

At signed rank \(r\), let \(\mu_r(T)\) be target load, and put

\[
 e_r=\sum_T(\mu_r(T)-1)_+,qquad
 \Phi_r=\sum_T\binom{\mu_r(T)}2.
\tag{3.2}
\]

Because every individual path has distinct internal traces when
\(\ell>0\),

\[
 \boxed{
   \sum_{r=-H}^{H-1}e_r
   \le\sum_{r=-H}^{H-1}\Phi_r
   =\Xi.}
\tag{3.3}
\]

Legal tagging permits at most one tag-\(H\) phase per top, so rank
\(m+H\) adds no collision.  Tag truncation can only decrease (3.3).
Therefore

\[
                         \Xi=o(W)
\tag{3.4}
\]

is a sufficient deterministic condition for aggregate signed simplicity.

More precisely, let \(A_r=\sum_T\mu_r(T)\) be the number of active
occurrences at rank \(m+r\), let

\[
 B_r=\binom{2m}{m+r}=N_{|r|},\qquad
 h_r=\#\{T:\mu_r(T)=0\},
\]

and put

\[
 \Delta=\sum_{r=-H}^{H}(B_r-A_r)_+.
\tag{3.4a}
\]

At each rank the exact floor identity is

\[
                         A_r-B_r=e_r-h_r.
\tag{3.4b}
\]

Consequently

\[
 \boxed{
 \sum_{r=-H}^{H}(e_r+h_r)
 \le 2\Xi+\Delta.}
\tag{3.4c}
\]

Indeed, (3.4b) gives
\(e_r+h_r=2e_r+B_r-A_r\le2e_r+(B_r-A_r)_+\),
and rank \(m+H\) has \(e_H=0\).  Thus

\[
                         \Xi=o(W),\qquad\Delta=o(W)
\tag{3.4d}
\]

is a complete deterministic sufficient condition for aggregate signed
overload plus leave \(o(W)\).  It is this pair of estimates, rather than
middle defect alone, that a compensated path nibble would have to prove.

There is a weaker owner-only envelope.  If \(X_a\) denotes the middle
owner of occurrence \(a\), then Theorem 1.2 gives

\[
 \sum_{q=1}^H\sum_{\sigma\in\{+,-\}}\Phi_q^\sigma
 \le
 2H\Phi_0+2\sum_{\substack{a<b\\X_a\ne X_b}}
       (H-d_J(X_a,X_b)+1)_+.
\tag{3.5}
\]

This is valid but normally enormous: distinct middle owners may populate
small Johnson balls with no middle collision.  Thus a compensated nibble
must charge actual interval influence, or a substantially sharper
process-specific proxy, rather than middle overload alone.

## 4. The reversed-tail gadget

Fix coordinates \(a,b\) and

\[
 C\in\binom{[2m]\setminus\{a,b\}}{M-1},qquad
 U=C+\{a\},\quad V=C+\{b\}.
\tag{4.1}
\]

Choose a common core \(Q\subset C\), \(|Q|=2H\), and let
\(\varphi:U\to V\) fix \(C\) and send \(a\) to \(b\).  Order the
\(U\)-tail as

\[
                         w=(w_1,\ldots,w_s),qquad w_{2H}=a,
\tag{4.2}
\]

and the \(V\)-tail by

\[
                         v_i=\varphi(w_{s+1-i}).
\tag{4.3}
\]

### Theorem 4.1 (exact reversed-tail profile)

At every deletion length \(1\le\ell\le2H\), the two paths have exactly
\(\ell\) common targets.

#### Proof

The allowed length-\(\ell\) intervals containing \(w_{2H}=a\) start at

\[
                         2H-\ell+1,\ldots,2H,
\tag{4.4}
\]

giving \(\ell\) intervals.  Since \(2H\le L\), reversal sends each to an
allowed interval of the other path.  Its set is \(\varphi(I)\), and
\(U\setminus I=V\setminus\varphi(I)\).  By Theorem 1.1 no interval not
containing \(a\) can collide, and the reversed interval is unique.
\(\square\)

Thus there are exactly \(H\) middle collisions.  At upper depth \(q\)
there are exactly \(H-q\), on the nested left-path phase sets

\[
                         \{1,\ldots,H-q\}.
\tag{4.5}
\]

The reflected right-path phase sets are nested as well.

## 5. Precisely scoped sparse replacement

The coordinate swap \(a\leftrightarrow b\) supplies

\[
 P_m=\binom{2m-2}{M-1}
\tag{5.1}
\]

disjoint top pairs, and

\[
 {P_m\over N_H}
 ={(m+H)(m-H)\over2m(2m-1)}={1\over4}+o(1).
\tag{5.2}
\]

Fix constants

\[
 0<\varepsilon<{1\over4},qquad
 0<c<{1\over4}\varepsilon e^{-\varepsilon^2},
\tag{5.3}
\]

and put

\[
 K=\left\lfloor {cW\over H\sqrt m}\right\rfloor,qquad
 Q_*=\lfloor\varepsilon\sqrt m\rfloor.
\tag{5.4}
\]

For sufficiently large \(m\), \(K<P_m\).

Indeed, (5.2), \(N_H=(1+o(1))W/m\), and (5.4) give

\[
 {K\over P_m}\le(4c+o(1)){\sqrt m\over H}
                =O((\log m)^{-1/2})=o(1).
\tag{5.4a}
\]

### Theorem 5.1 (unconditional perturbation given a base selection)

Assume a family \(\mathcal A\) containing one core-safe tight path for
every top has already been selected, and its middle overload plus leave is
\(D_m=o(W)\).  Remove the paths on any \(K\) pairs from (5.1), and insert
the corresponding reversed-tail gadgets.  The resulting family still has
one core-safe path per top and has middle overload plus leave at most

\[
                         D_m+4KL
 =D_m+O(W/\sqrt{\log m})=o(W).
\tag{5.5}
\]

Its untagged upper collision potential through depth \(Q_*\) is at least

\[
 K\sum_{q=1}^{Q_*}(H-q)
 \ge {1\over2}KHQ_*.
\tag{5.6}
\]

#### Proof

Each removed or inserted path changes exactly \(L\) middle occurrences.
Changing one occurrence changes overload plus leave by at most one, which
gives (5.5).  Theorem 4.1 gives (5.6), and the phase pairs in distinct
gadgets are occurrence-disjoint. \(\square\)

This theorem is conditional on the assumed base selection \(\mathcal A\).
It does not prove that such a globally middle-safe selection exists.

### Theorem 5.2 (activated obstruction under legal compensation)

In addition to Theorem 5.1, assume the tag layer may be reassigned on the
modified paths and on a legal compensation reservoir so that all unused
global tag counts can be placed after the following gadget tags are
prescribed.  The reservoir may contain auxiliary legal collar states not
belonging to the \(L\)-phase paths.  Alternatively, for a partial design,
assume a prescribed deficient census whose total deficit is \(o(W)\) can
be completed on the available states.  This is an explicit hypothesis:
the \(L N_H\) path phases alone are fewer than the \(W\) entries in the
full SCD census, so scalar capacity or arbitrary per-phase tagging does
not by itself supply an exact full-census completion.

On each gadget path, give its first \(H-Q_*\) collision phases tag
\(Q_*\), and give the successive phases one each of the tags
\(Q_*-1,\ldots,1\).  Give the reflected phases the same nested threshold
profile.  Then the exact prescribed demand is

\[
 2K\quad\text{in each tag class }1\le q<Q_*,
\tag{5.7}
\]

and exactly

\[
 2K(H-Q_*)\le 2KH
             \le(2c+o(1)){W\over\sqrt m}
\tag{5.8}
\]

in tag class \(Q_*\).  These demands fit inside the SCD census because

\[
 \gamma_{Q_*}
 =\left(2\varepsilon e^{-\varepsilon^2}+o(1)\right)
       {W\over\sqrt m},
\tag{5.9}
\]

and, uniformly for \(1\le q<Q_*\),

\[
                         2K=o(W/m)\le\gamma_q
\tag{5.10}
\]

for all sufficiently large \(m\).  A required tag-\(H\) anchor can be
placed outside the displayed collision phases.

After compensation, the actual upper signed repeat excess obeys

\[
 \boxed{
  \sum_{q=1}^{Q_*}e_q^+
  \ge K\sum_{q=1}^{Q_*}(H-q)
  \ge {c\varepsilon\over8}W}
\tag{5.11}
\]

for all sufficiently large \(m\).

Here the exact census identity used in (5.9)--(5.10) is

\[
 \gamma_q=N_q-N_{q+1}
          ={2q+1\over m+q+1}N_q.
\tag{5.10a}
\]

#### Proof

The phase sets (4.5) are nested, so the displayed tags activate every
gadget collision through depth \(Q_*\).  Identity (5.10a) follows from

\[
 {N_{q+1}\over N_q}={m-q\over m+q+1}.
\]

For \(q=Q_*\), the central-binomial local ratio gives (5.9).  Moreover,
explicitly,

\[
 {N_q\over W}
 =\prod_{i=1}^q{m-i+1\over m+i},
\qquad
 \log {N_q\over W}
 =-{q^2\over m}+O\!\left({q\over m}+{q^3\over m^2}\right).
\]

Thus \(N_{Q_*}/W=e^{-\varepsilon^2+o(1)}\), and (5.10a)
gives the displayed constant in (5.9).  Moreover,
\(\gamma_{q+1}\ge\gamma_q\) whenever

\[
                         2q^2+4q+1\le m.
\]

Since \(\varepsilon<1/4\), this holds throughout
\(1\le q<Q_*\) for all sufficiently large \(m\).  Also

\[
 \gamma_1={3m\over(m+1)(m+2)}W,
 \qquad
 2K=O\!\left({W\over m\sqrt{\log m}}\right)=o(W/m),
\]

which proves (5.10); (5.3), (5.8), and (5.9) give the remaining scalar
margin.  These inequalities certify capacity only.  The theorem's legal
completion follows from its explicit compensation hypothesis, not from
the inequalities alone.

At each depth, the activated occurrences split into disjoint equal-target
pairs.  If several pairs land on the same target, load \(2r\) contributes
at least \(r\) to repeat excess, so cross-gadget coincidences cannot lower
the bound.  Finally, for large \(m\), floors give

\[
 K\ge {cW\over2H\sqrt m},\qquad
 Q_*\ge{\varepsilon\sqrt m\over2},\qquad Q_*\le H/2,
\]

which yields (5.11). \(\square\)

The compensation assumption is stated explicitly because scalar capacity
does not itself construct a tag assignment inside an unrelated restricted
grammar, nor does the short \(L N_H\)-phase catalogue contain enough slots
for the full \(W\)-entry census.  Without it, Theorem 5.1 still gives the
exact untagged dependent collision potential and rules out any
perturbatively stable implication from middle defect alone.

## 6. Proved boundary

Proved unconditionally:

1. Theorems 1.1 and 1.2, including every signed rank and both signs;
2. the sharp span influence bound (2.1);
3. the exact reversed-tail collision profile; and
4. the conditional-on-base, but otherwise explicit, path replacement of
   Theorem 5.1.

Proved under the stated tag-compensation hypothesis:

1. exact scalar census compatibility of the prescribed gadget demands;
   legal completion itself is the stated hypothesis; and
2. the linear signed repeat lower bound (5.11).

Not proved:

1. existence of the assumed global middle-safe atlas;
2. existence of a compensation reservoir in every restricted tag grammar;
3. a nibble or alteration producing \(\Xi=o(W)\); or
4. the coefficient-one theorem.

The exact surviving positive target is a one-path-per-top selection which
controls the rankwise deficit \(\Delta\), the middle owner load, and the
nonlocal interval influence \(\Xi\).  Equations (3.4c)--(3.4d) then give
the required all-rank defect conclusion with no independence assumption.
