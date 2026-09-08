# Dependent signed traces of tight promotion paths: exact external influence and a middle-safe counterexample

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web input
is used.

## 0. Outcome

Put

\[
 M=m+H,\qquad s=m-H,\qquad L=s-2H+1=m-3H+1,
\]

and assume

\[
 H=(1+o(1))\sqrt{m\log m},\qquad m>5H.
\tag{0.1}
\]

For every rank-\(M\) top choose one core-safe tight promotion path as in
`MATH_THEOREM_S_GLOBAL_COMMON_CORE_PROMOTION_ATLAS_20260726.md`.  This
note proves the following exact statements.

1. For two tops \(U,V\), and equal-length deletion intervals \(I\subset
   U\), \(J\subset V\),
   \[
      U\setminus I=V\setminus J
   \]
   if and only if
   \[
      I=(U\setminus V)\mathbin{\dot\cup}K,qquad
      J=(V\setminus U)\mathbin{\dot\cup}K
   \tag{0.2}
   \]
   for one \(K\subseteq U\cap V\).  In particular, a signed collision at
   deletion length \(\ell\) requires
   \(d_J(U,V)\le\ell\).

2. If two occurrences collide at upper depth \(q\), their middle owners
   are \(Z\setminus P_U,Z\setminus P_V\) for two \(q\)-subsets of the
   common upper target \(Z\).  If they collide at lower depth \(q\), their
   middle owners are \(Z\cup P_U,Z\cup P_V\).  In both cases
   \[
      d_J(X_U,X_V)=q-|P_U\cap P_V|,
   \tag{0.3}
   \]
   and the middle owners agree if and only if \(P_U=P_V\).  Thus signed
   equality does not force middle equality, and middle equality does not
   force signed equality.

3. For two distinct physical paths, the number of collisions at deletion
   length \(\ell\) is at most \(\ell\).  A sharper bound is the minimum
   of the two interval-span capacities in (4.3) below.  This is an exact
   external-influence bound for a compensated nibble.

4. Middle defect alone is insufficient.  There is a two-top reversed-tail
   gadget with exactly \(\ell\) cross-path collisions at every deletion
   length \(1\le\ell\le2H\).  It has only \(H\) middle collisions, but
   its upper signed ranks \(1\le q\le Q\) have
   \[
                       \sum_{q=1}^Q(H-q)
   \tag{0.4}
   \]
   collisions on nested phase sets.

5. Starting from any one-path-per-top selection having middle
   collision/leave \(o(W)\), replace only
   \[
                  K=\left\lfloor {cW\over H\sqrt m}\right\rfloor
   \tag{0.5}
   \]
   disjoint top pairs by these gadgets, for a sufficiently small fixed
   \(c>0\).  The middle occurrence vector changes in only
   \[
                      O(KL)=O(W/\sqrt{log m})=o(W)
   \tag{0.6}
   \]
   positions.  Nevertheless, with \(Q=\lfloor\varepsilon\sqrt m\rfloor\)
   and the displayed nested tag prescription, the aggregate upper signed
   collision potential is \(\Omega(W)\).  It becomes actual repeat excess
   under the explicit legal tag-compensation hypothesis stated in Section
   6; scalar class capacity alone does not prove that completion.

Consequently

\[
 \boxed{
   o(W)\text{ middle defect does not imply }
   o(W)\text{ aggregate signed-trace defect}.}
\tag{0.7}
\]

The additional quantity which a nibble or alteration must control is the
actual cross-path interval influence (4.5), or a valid upper envelope for
it.  Ordinary middle owner capacity does not contain that information.

## 1. Tight-path trace notation

Fix a top \(U\), a core \(Q_U\subset U\) of size \(2H\), and an ordered
tail

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

The phase-\(j\) deletion interval and target are

\[
 I^U_{j,\ell}
 =\{w^U_{j+2H-\ell},w^U_{j+2H-\ell+1},\ldots,
     w^U_{j+2H-1}\},
\tag{1.3}
\]

\[
                         T^U_{j,\ell}=U\setminus I^U_{j,\ell}.
\tag{1.4}
\]

The interval has length \(\ell\).  At the middle rank \(r=0\), one has
\(\ell=H\).  At upper depth \(q\), \(r=q\) and \(\ell=H-q\); at lower
depth \(q\), \(r=-q\) and \(\ell=H+q\).

As \(j\) varies, (1.3) ranges over all length-\(\ell\) intervals in the
tail whose starting position lies in

\[
                  2H-\ell+1,\ldots,s-\ell+1.
\tag{1.5}
\]

## 2. Exact two-top collision normal form

### Theorem 2.1 (top-complement interval criterion)

Let \(|U|=|V|=M\), let \(|I|=|J|=\ell\), with \(I\subseteq U\) and
\(J\subseteq V\).  Put

\[
 A=U\setminus V,qquad B=V\setminus U,qquad C=U\cap V,
\]

so \(|A|=|B|=\delta=d_J(U,V)\).  Then

\[
 U\setminus I=V\setminus J
\tag{2.1}
\]

if and only if there is a set \(K\subseteq C\), \(|K|=\ell-\delta\),
such that

\[
                         I=A\dot\cup K,qquad J=B\dot\cup K.
\tag{2.2}
\]

#### Proof

If (2.1) holds, every element of \(A\) must be deleted from \(U\), and
every element of \(B\) must be deleted from \(V\).  Hence \(A\subseteq I\)
and \(B\subseteq J\).  On the common top part \(C\), equality of the
remaining masks says exactly

\[
                         I\cap C=J\cap C=:K.
\]

Equal interval lengths give \(|K|=\ell-\delta\).  This proves necessity;
substitution proves sufficiency. \(\square\)

Immediate consequences are

\[
 \delta\le\ell,qquad I\triangle J=U\triangle V.
\tag{2.3}
\]

If an exclusive coordinate of \(U\) lies in its permanent core \(Q_U\),
then no core-safe deletion interval can contain it, so \(U\)'s path has no
collision with any path on \(V\).  Thus every colliding pair must obey

\[
                         Q_U\subseteq V,qquad Q_V\subseteq U.
\tag{2.4}
\]

## 3. Relation to the middle collision profile

Fix two phases, one in each path, and let their middle owners be
\(X_U,X_V\).

### Theorem 3.1 (upper and lower flag-distance law)

At upper depth \(q\), suppose their common trace is the
\((m+q)\)-set \(Z\).  Then there are \(q\)-sets \(P_U,P_V\subset Z\)
such that

\[
                         X_U=Z\setminus P_U,qquad
                         X_V=Z\setminus P_V.
\tag{3.1}
\]

At lower depth \(q\), suppose their common trace is the
\((m-q)\)-set \(Z\).  Then there are \(q\)-sets
\(P_U,P_V\subseteq[2m]\setminus Z\) such that

\[
                         X_U=Z\cup P_U,qquad
                         X_V=Z\cup P_V.
\tag{3.2}
\]

In either case,

\[
 \boxed{
 d_J(X_U,X_V)=q-|P_U\cap P_V|,qquad
 X_U=X_V\Longleftrightarrow P_U=P_V.}
\tag{3.3}
\]

#### Proof

For the upper trace, the middle deletion interval is obtained from the
shorter upper deletion interval by adjoining its \(q\) immediately
preceding tail coordinates.  Those coordinates lie in the common upper
mask \(Z\); deleting them from \(Z\) gives the middle owner, proving
(3.1).

For the lower trace, the longer lower deletion interval is obtained from
the middle interval by adjoining \(q\) preceding coordinates.  Those
coordinates belong to the middle owner but not to the common lower mask,
giving (3.2).  The two Johnson-distance identities follow by taking the
symmetric differences of equal-size sets. \(\square\)

Conversely, if two phases have a common middle owner \(X\), their upper
traces are \(X\cup P_U,X\cup P_V\), and their lower traces are
\(X\setminus P_U,X\setminus P_V\), for the corresponding ordered flag
blocks.  At either sign the traces agree if and only if those blocks agree.
Thus neither direction of a proposed automatic middle/signed implication
is valid.

## 4. A sharp external-influence bound

For a tail word \(w^U\) and a set \(A\subseteq U\setminus Q_U\), let
\(\operatorname{span}_U(A)\) be the length of the smallest linear tail
interval containing \(A\).  Put the span equal to \(+\infty\) if
\(A\not\subseteq U\setminus Q_U\).

Let \(c_{UV}(\ell)\) be the number of phase pairs whose length-\(\ell\)
targets agree.

### Theorem 4.1 (two-path interval influence)

For distinct tops \(U,V\), with \(A=U\setminus V\) and
\(B=V\setminus U\),

\[
 \boxed{
 c_{UV}(\ell)
 \le
 \min\left\{
  (\ell-\operatorname{span}_U(A)+1)_+,\,
  (\ell-\operatorname{span}_V(B)+1)_+
 \right\}
 \le\ell.}
\tag{4.1}
\]

In particular,

\[
                         \sum_{\ell=1}^{2H}c_{UV}(\ell)
                         \le H(2H+1).
\tag{4.2}
\]

#### Proof

By Theorem 2.1, every colliding \(U\)-interval must contain all of \(A\).
The number of length-\(\ell\) intervals in a linear word containing a
fixed set of span \(a\) is at most \((\ell-a+1)_+\).  The same argument
applies in \(V\).

For a fixed \(U\)-interval \(I\), (2.2) determines the required
\(V\)-interval set uniquely.  A fixed set of distinct letters can occur as
an equal-length interval in an injective linear word at most once.
Therefore either span count bounds the number of collision pairs.  The
last inequality and (4.2) follow by summing \(1+2+\cdots+2H\).
\(\square\)

For a selected path family \(\mathcal P\), define its actual external
influence

\[
 \Xi(\mathcal P)
 =\sum_{\{U,V\}}\sum_{\ell=1}^{2H}c_{UV}(\ell).
\tag{4.3}
\]

Let \(e_r\) denote signed repeat excess and \(\Phi_r\) signed pair energy:

\[
 e_r=\sum_T(\mu_r(T)-1)_+,qquad
 \Phi_r=\sum_T\binom{\mu_r(T)}2.
\tag{4.4}
\]

Then

\[
 \boxed{
   \sum_{r=-H}^{H-1}e_r
   \le\sum_{r=-H}^{H-1}\Phi_r
   =\Xi(\mathcal P),}
\tag{4.5}
\]

for the untagged internal ranks; truncation only decreases the left and
middle quantities.  At \(r=H\), legal tagging permits at most one active
phase per top, and distinct tops have distinct top masks, so its collision
energy is zero.  Thus
\(\Xi=o(W)\) is a sufficient common-history invariant for aggregate
signed simplicity.  Equation (4.1) supplies a deterministic upper
envelope which can be charged during a compensated nibble.

There is also a middle-owner-only relaxation.  A signed collision at
depth \(q\) can occur only between middle owners at Johnson distance at
most \(q\).  Consequently

\[
 \sum_{q=1}^H\sum_{\sigma\in\{+,-\}}\Phi_q^\sigma
 \le
 2H\Phi_0+
 2\sum_{\substack{a<b\\X_a\ne X_b}}
   (H-d_J(X_a,X_b)+1)_+.
\tag{4.6}
\]

This is exact as a universal influence envelope but is generally far too
large: middle simplicity controls repeated owners, not the population of
distinct owners in small Johnson balls.

## 5. The reversed-tail gadget

Fix two coordinates \(a,b\), a set

\[
                         C\in\binom{[2m]\setminus\{a,b\}}{M-1},
\]

and paired tops

\[
                         U=C+\{a\},\qquad V=C+\{b\}.
\tag{5.1}
\]

Choose a common core \(Q\subset C\), \(|Q|=2H\), and let
\(\varphi:U\to V\) fix \(C\) and send \(a\) to \(b\).  Choose a tail
word

\[
                         w=(w_1,\ldots,w_s)
\tag{5.2}
\]

on \(U\setminus Q\), with

\[
                         w_{2H}=a.
\tag{5.3}
\]

Give \(V\) the reversed tail

\[
                         v_i=\varphi(w_{s+1-i}).
\tag{5.4}
\]

### Theorem 5.1 (exact reversed-tail collision profile)

For every \(1\le\ell\le2H\), the two core-safe paths in (5.1)--(5.4)
have exactly \(\ell\) common targets at deletion length \(\ell\).

#### Proof

The allowed length-\(\ell\) intervals in the \(U\)-tail start at the
positions in (1.5).  Those containing \(a=w_{2H}\) start at

\[
                         2H-\ell+1,\ldots,2H,
\tag{5.5}
\]

so there are exactly \(\ell\).  Since \(2H\le L\), reversal sends each
of these intervals to an allowed length-\(\ell\) interval in the
\(V\)-tail.  Its set is \(\varphi(I)\).  Because \(I\) contains \(a\),

\[
                         U\setminus I=V\setminus\varphi(I).
\tag{5.6}
\]

Conversely, Theorem 2.1 says a colliding interval must contain \(a\), and
reversal supplies its unique partner.  Hence (5.5) is the complete
collision list. \(\square\)

At the middle rank, \(\ell=H\), so this gadget has exactly \(H\) middle
collisions.  At upper depth \(q\), \(\ell=H-q\), so it has exactly
\(H-q\) collisions.  On the \(U\)-path the relevant phase set is

\[
                         \{1,2,\ldots,H-q\},
\tag{5.7}
\]

and the corresponding phase sets in both paths are nested as \(q\)
increases.

## 6. Sparse insertion gives the global counterexample

The coordinate swap \(a\leftrightarrow b\) partitions all tops containing
exactly one of \(a,b\) into

\[
                         \binom{2m-2}{M-1}
\tag{6.1}
\]

disjoint pairs of the form (5.1).  Moreover,

\[
 {\binom{2m-2}{M-1}\over N_H}
 ={(m+H)(m-H)\over2m(2m-1)}
 ={1\over4}+o(1).
\tag{6.2}
\]

Thus (0.5) pairs are available, since

\[
 {K\over N_H}=O\left({m\over H\sqrt m}\right)
 =O(1/\sqrt{log m})=o(1).
\tag{6.3}
\]

Assume one core-safe path per top has already been selected with middle
collision and leave \(o(W)\).  Remove the old paths on these \(2K\) tops
and insert the reversed-tail paths.  Removing or adding one occurrence
changes middle overload plus leave by at most one.  Hence the total change
is at most

\[
                         4KL=O(W/\sqrt{log m})=o(W).
\tag{6.4}
\]

The modified selection still satisfies the assumed middle conclusion.

Choose

\[
                         Q_*=\lfloor\varepsilon\sqrt m\rfloor
\tag{6.5}
\]

for a sufficiently small fixed \(\varepsilon>0\).  In every gadget path,
make the phases in (5.7) active through upper depth \(q\), for every
\(1\le q\le Q_*\).  This is one nested threshold family: give the first
\(H-Q_*\) phases tag \(Q_*\), and give one successive phase each of the
tags \(Q_*-1,Q_*-2,\ldots,1\).  The reflected path receives the matching
nested tags.  A tag-\(H\) anchor, if required, can be placed elsewhere.

For every \(q<Q_*\), the gadget demand in tag class \(q\) is \(2K\),
which is \(o(W/m)\) and hence below \(\gamma_q\).  In tag class \(Q_*\),
the demand is at most

\[
                         2KH=2cW/\sqrt m+o(W/\sqrt m).
\tag{6.6}
\]

On the other hand,

\[
 \gamma_{Q_*}
 =\left(2\varepsilon e^{-\varepsilon^2}+o(1)\right){W\over\sqrt m}.
\tag{6.7}
\]

Taking \(c<\varepsilon e^{-\varepsilon^2}/2\) leaves positive scalar
census slack.  Assume, in addition, that the untouched phases and any
allowed compensation reservoir admit a legal assignment of all remaining
tags after this prescription.  This completion is an explicit hypothesis,
not a consequence of the scalar inequalities above.

At each upper depth \(q\), the collision pairs within distinct gadgets
use disjoint path occurrences.  Even if targets belonging to different
gadgets coincide, \(P\) disjoint duplicate pairs contribute repeat excess
at least \(P\).  Therefore Theorem 5.1 gives

\[
 \begin{aligned}
 \sum_{q=1}^{Q_*}e_q^+
 &\ge K\sum_{q=1}^{Q_*}(H-q)\\
 &\ge {1\over2}KHQ_*\\
 &=\Omega(W).
 \end{aligned}
\tag{6.8}
\]

Under the stated compensation hypothesis this proves the actual-repeat
form of (0.7).  Without it, the same calculation proves the untagged
collision-potential form.

## 7. Proved and unproved boundary

Proved:

1. the exact top-complement interval criterion;
2. the upper/lower flag-distance law relating signed and middle traces;
3. the sharp span-based two-path influence bound;
4. an exact reversed-tail collision profile saturating the coarse
   \(c_{UV}(\ell)\le\ell\) bound;
5. sparse insertion preserving \(o(W)\) middle collision/leave; and
6. a nested, census-compatible activation forcing \(\Omega(W)\) aggregate
   signed repeat excess.

Not proved:

1. a compensated nibble controlling \(\Xi\);
2. an integral one-path-per-top selection with \(\Xi=o(W)\);
3. completion to one SCD; or
4. the constant-one theorem.

The corrected selection gate is therefore strictly stronger than middle
owner packing: it must control dependent interval influence across all
signed ranks.
