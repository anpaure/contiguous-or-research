# Promotion-ring positive cuts: fibre-dense cylinder no-go, literal short recourse, and the surviving global mesh

Date: 2026-07-26

Method: pure mathematics only.  Every column below is an actual cyclic
frame column.  No independent target table, signed column, or fractional
frame is substituted for a physical option.

## 0. Verdict

Let

\[
 n=2m,\qquad M=m+H,\qquad
 \mathcal U=\binom{[2m]}M,\qquad
 N=|\mathcal U|,\qquad R=(M-1)!.
\]

At the tuned covering-side height,

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 T:=MN=(1+o(1))W,\qquad W=\binom{2m}m.
\]

For every top \(U\), one chooses one oriented cyclic frame modulo
rotation.  Its middle row consists of its \(M\) cyclic \(m\)-windows; at
the entrance rank \(m-q_0\), its second row consists of its \(M\) cyclic
\((m-q_0)\)-windows.

The positive-cut/Gram attack has the following exact boundary.

1.  The two-row floor and one-top normal cone admit an exact identity.
    At a strong one-top local minimum, the floor-corrected pair energy is
    precisely the unsaturated part of the aggregate cyclic-score spread;
    the identity by itself gives only a \((1+o(1))W\) ceiling for the two
    rows, not \(o(W)\).

2.  A genuinely higher-order and fibre-dense adjacent-pair cylinder is
    nevertheless globally tiny.  For rank \(k=M-h\), its exact global
    degree is

    \[
       D_{k,2}={2D_k\over k(2m-k)},
    \]

    where \(D_k\) is the one-target degree.  At both the middle and
    entrance ranks this is

    \[
       D_{k,2}=(2+o(1)){R\over m^2}.
    \]

    In every compatible top it occupies a fraction

    \[
       q_k={2(h-1)!(k-1)!\over(M-1)!},
    \]

    and \(q_kN\to\infty\).  Thus it is fibre-dense in the surviving
    threshold \(q_kR\gg R/N\), but it is still \(m^{-2}\)-small globally.

3.  There is a literal short-recourse theorem.  Any

    \[
       t\le 1+\left\lfloor{(H-1)(m-1)-1\over M}\right\rfloor
       =(1-o(1))H
    \]

    pairwise vertex-disjoint adjacent middle-target pairs lift to \(t\)
    pairwise target-disjoint actual rooted cyclic columns.  Consequently
    every degree-two cylinder obstruction below this scale is covered by
    cleared target stars.  A non-star obstruction whose
    support-to-matching ratio is at least \((1-o(1))R\) needs at least

    \[
                         (1-o(1)){m^2H\over2}
    \]

    interlocked adjacent-pair atoms.

4.  The genuine middle--entrance nested cylinder is even smaller.  If
    \(S\subset X\), \(|X|=m\), and \(|S|=m-q\), then

    \[
       {D(X,S)\over D_m}={q+1\over\binom mq}.
    \]

    At \(q=q_0=\lceil m^{1/4}\rceil\), polynomially many such cylinders
    have \(o(R/m^A)\) total mass for every fixed \(A\), despite being
    fibre-dense inside each used top.

5.  Higher order plus fibre density therefore does not imply an
    \(\Omega(W)\) coercive inequality.  On one top the annihilator of all
    cyclic-deck differences is exactly the affine slice space, but a
    one-target spike already has nonzero higher-harmonic score spread only
    \(p_k=M/\binom Mk\), although its supporting column set is fibre-dense.

6.  There is also an actual integral obstruction to every fixed bounded
    **paired-orbit** transposition atlas.  For each fixed \(d\), a state
    exists which is simultaneously local against every compound cut
    formed from paired top-orbit switches for \(d\) prescribed disjoint
    transpositions and has floor energy \(\Omega_d(W)\).  The exact proof
    and its restricted move scope are in
    `MATH_OBSTRUCTION_PROMOTION_RING_DISJOINT_TRANSPOSITION_PRIVATE_ORBITS_20260726.md`.
    In the unrestricted one-frame-per-top fibre, however, a single top
    may be changed independently.  The paired-orbit invariant is not
    preserved by that legal move.  Hence it is not a local minimum for the
    full product fibre.

Thus the requested bounded/local higher-order sector cannot obstruct or
prove coefficient one.  The first surviving object is a diffuse,
owner-sensitive, cross-root mesh with at least \(\Omega(m^2H)\) comparable
degree-two atoms, or a comparably massive nested cross-row mesh, together
with a growing family of transpositions.  No all-transposition bad local
minimum and no \(o(W)\) positive-cut theorem is proved here.

## 1. Exact two-row floor and normal-cone identity

Index the controlled rows by \(a\).  Row \(a\) has target rank \(k_a\),
target count

\[
                         V_a=\binom{2m}{k_a},
\]

and complementary interval length

\[
                         h_a=M-k_a<M/2.
\]

Every selected frame contributes \(M\) occurrences to every row, so the
common row total is \(T=MN\).  Assume

\[
                         V_a\le T<2V_a,
\]

and put

\[
 s_a=T-V_a,\qquad \theta_a={T\over V_a},\qquad
 p_a={M\over\binom M{k_a}}={M\over\binom M{h_a}}.
\tag{1.1}
\]

For a physical selection \(F\), let \(\mu_z^a\) be the load of target
\(z\) in row \(a\), and define

\[
 P_a(F)=\sum_z\binom{\mu_z^a}{2},\qquad
 \Psi_a(F)=P_a(F)-s_a.
\tag{1.2}
\]

The exact integer-floor identity is

\[
 \boxed{
 \Psi_a(F)
 =|\{z:\mu_z^a=0\}|
  +\sum_{\mu_z^a\ge3}\binom{\mu_z^a-1}{2}.}
\tag{1.3}
\]

In particular \(\Psi_a\ge0\), and it controls the literal row holes.

For top \(U\), let \(c_{U,\pi}^a\) be the incidence vector of the row-\(a\)
deck of frame \(\pi\), and write

\[
 c_{U,\pi}=\bigoplus_a c_{U,\pi}^a.
\]

For the selected frame \(\pi_U\), put

\[
 r_U=\mu-c_{U,\pi_U}.
\tag{1.4}
\]

Thus \(r_U\) is the exact external load supplied by all other tops.  A
one-top replacement has the exact derivative

\[
 \boxed{
 \sum_a\Psi_a(F-\pi_U+\pi)-\sum_a\Psi_a(F)
 =\langle r_U,c_{U,\pi}-c_{U,\pi_U}\rangle.}
\tag{1.5}
\]

Indeed, adding one occurrence to an external load \(r\) increases
\(\binom r2\) by \(r\), and the floor constants do not change.

Let

\[
 m_U=\min_{\pi}\langle r_U,c_{U,\pi}\rangle,
\]

\[
 A_U=\mathbb E_\pi\langle r_U,c_{U,\pi}\rangle-m_U,
 \qquad
 D_U=\langle r_U,c_{U,\pi_U}\rangle-m_U.
\tag{1.6}
\]

The uniform frame barycentre has value \(p_a\) on every rank-\(k_a\)
target inside \(U\), and globally

\[
 \sum_U\mathbb E_\pi c_{U,\pi}^a=\theta_a\mathbf1.
\tag{1.7}
\]

Moreover

\[
 \sum_U\langle r_U,c_{U,\pi_U}\rangle=2\sum_aP_a(F).
\tag{1.8}
\]

The uniform-score sum is

\[
 \sum_U\mathbb E_\pi\langle r_U,c_{U,\pi}\rangle
 =\sum_a T(\theta_a-p_a).
\tag{1.9}
\]

Substituting (1.6) into (1.8), and subtracting twice the exact floors,
gives

\[
 \boxed{
 2\sum_a\Psi_a(F)
 =\sum_a B_a-\sum_UA_U+\sum_UD_U,}
\tag{1.10}
\]

where

\[
 \boxed{
 B_a=T(\theta_a-p_a)-2s_a
    =V_a+{s_a^2\over V_a}-p_aT.}
\tag{1.11}
\]

At a strong one-top local minimum, \(D_U=0\) for every \(U\), and hence

\[
 \boxed{
 2\sum_a\Psi_a(F)=\sum_aB_a-\sum_UA_U.}
\tag{1.12}
\]

At the tuned middle and entrance rows, \(B_m=(1+o(1))W\) and
\(B_{m-q_0}=(1+o(1))W\).  Thus uniform one-top comparison gives only

\[
 \sum_a\Psi_a(F)\le(1+o(1))W.
\tag{1.13}
\]

The exact missing theorem is the saturation

\[
                         \sum_UA_U=\sum_aB_a-o(W).
\tag{1.14}
\]

Neither nonaffinity nor fibre density implies (1.14), as Sections 2--5
show.

### Remark 1.1 (the exact \(L^1\) coverage local minimum is also constant-scale)

For one row, abbreviate \(V=V_a\), \(p=p_a\), and
\(\theta=\theta_a\); let \(h\) be the number of holes and \(n_1\) the
number of load-one targets.  If the objective is literal coverage rather
than pair energy, remove top \(U\) and define the occupied-external
blocker score

\[
 B_U(\pi)=\sum_{z\in c_{U,\pi}}
                  \mathbf1_{\{r_U(z)>0\}}.
\tag{1.15}
\]

A strong one-top \(L^1\) local minimum chooses a frame minimizing
\(B_U\).  Exact double counting gives

\[
 \boxed{
 \sum_U\left(\mathbb E_\pi B_U(\pi)-\min_\pi B_U(\pi)\right)
 =(1-p)n_1-\theta h.}
\tag{1.16}
\]

Indeed a load-one target is externally occupied in all but its unique
owner fibre, whereas a load-at-least-two target is externally occupied
in every containing fibre.  Consequently

\[
 h\le{1-p\over\theta+1-p}\,V=(1/2+o(1))V.
\tag{1.17}
\]

If all loads are at most two, then
\(n_1=V-(T-V)-2h\), and (1.16) sharpens only to

\[
 h\le{(1-p)(V-(T-V))\over\theta+2(1-p)}
   =(1/3+o(1))V.
\tag{1.18}
\]

Thus the \(L^1\) blocker normal cone and the quadratic Gram normal cone
are different, but both one-top arguments stop at a positive constant
fraction.

## 2. Exact adjacent-pair cylinders

Fix one controlled rank \(k=M-h\), with \(2h<M\).  A top frame has \(M\)
cyclic rank-\(k\) windows, equivalently the complements of its \(M\)
cyclic \(h\)-windows.  There are \(R=(M-1)!\) frames on a fixed top, and a
fixed rank-\(k\) target contained in that top occurs in the fraction

\[
 p_k={M\over\binom Mk}={h!k!\over(M-1)!}.
\tag{2.1}
\]

Let \(X,Y\) be adjacent rank-\(k\) targets, so

\[
                         |X\setminus Y|=|Y\setminus X|=1.
\]

A compatible top contains \(X\cup Y\).  The complementary \(h\)-sets in
that top have an \((h-1)\)-set in common.  The two prescribed sets are
cyclic intervals in exactly

\[
                         2(h-1)!(k-1)!
\]

oriented cyclic frames modulo rotation.  Therefore the exact within-top
fraction is

\[
 \boxed{
 q_k={2(h-1)!(k-1)!\over(M-1)!}={2p_k\over hk}.}
\tag{2.2}
\]

There are

\[
                         \binom{2m-k-1}{h-1}
\]

compatible tops.  If

\[
 D_k=\binom{2m-k}{h}p_kR
\tag{2.3}
\]

is the one-target column degree, then the exact pair degree is

\[
\begin{aligned}
 D_{k,2}
 &=\binom{2m-k-1}{h-1}q_kR\\
 &=\boxed{{2\over k(2m-k)}D_k}.
\end{aligned}
\tag{2.4}
\]

At \(k=m\) and \(k=m-q_0\), exact regularity gives

\[
                         D_k=(1+o(1))R,
\]

and hence

\[
 \boxed{D_{k,2}=(2+o(1)){R\over m^2}.}
\tag{2.5}
\]

On the other hand,

\[
 \log(1/q_k)=O((h+q_0)\log m)=o(m),
 \qquad \log N=\Theta(m),
\]

so

\[
 \boxed{q_kN\longrightarrow\infty.}
\tag{2.6}
\]

Thus an adjacent-pair cylinder uses \(q_kR\gg R/N\) actual columns in
every compatible fibre.  This verifies literal fibre density, while
(2.5) proves that its global mass is still negligible.

### 2.1 Odd triangles and weighted atoms

Let \(X_1,X_2,X_3\) be a Johnson triangle, and take the union of the
three pair cylinders.  Any two positive columns share at least one of
the three targets, so the packet matching number of this support is one.
Its total size is at most

\[
                         3D_{k,2}=(6+o(1)){R\over m^2}.
\tag{2.7}
\]

Hence even this literal, fibre-dense odd obstruction is

\[
                         o(R/\sqrt m).
\]

More generally, for nonnegative adjacent-pair atom weights \(z_P\), put

\[
                         y_e=\sum_Pz_P\mathbf1_{\{P\subset e\}}.
\tag{2.8}
\]

Then

\[
 \boxed{
 y(\mathcal E)=D_{k,2}\sum_Pz_P,\qquad
 \nu_y\ge\max_Pz_P.}
\tag{2.9}
\]

Here and below, an \(R\)-scale obstruction means a
support-to-packet-matching or weighted-dual ratio of order \(R\), the
degree of one top/root vertex.  Consequently such a weighted obstruction
requires

\[
 \boxed{
 {\sum_Pz_P\over\max_Pz_P}
 \ge(1-o(1)){m^2\over2}.}
\tag{2.10}
\]

Fibre density by itself is therefore too weak by a factor of order
\(m^2\).

### 2.2 Edge-transitivity collapses every weighted matching dual

Let \(\mathcal H_{\rm col}\) be the rooted column hypergraph whose edge
set is the \(NR\) actual columns \((U,\pi)\), and whose vertices are the
top/root \(U\) together with all controlled middle and entrance targets
in that column.  Let \(\nu\) be its ordinary maximum matching number.
The action of \(S_{2m}\) is transitive on the actual rooted columns.
Therefore

\[
 \boxed{
 \chi_f'(\mathcal H_{\rm col})
 =\sup_{y\ge0}{y(\mathcal E)\over\nu_y}
 ={NR\over\nu}.}
\tag{2.11}
\]

Indeed, \(y_e=1/\nu\) gives the lower bound.  Conversely, average one
maximum matching over its \(S_{2m}\)-orbit.  Every column then has
marginal \(\nu/(NR)\); scaling this distribution by \(NR/\nu\) is a
fractional edge-colouring of total mass \(NR/\nu\).

Thus an arbitrary nonnegative higher-order or fibre-dense matching-dual
weight is not a second gate: its optimum is exactly the unweighted
maximum-matching deficiency.  This statement does not compute \(\nu\),
and strict column matching is stronger than the floor-surplus selection
problem.  It rules out only the attempt to obtain a new obstruction by
choosing a special weighted dual sector.

## 3. Conditioned avoidance and literal short recourse

Condition a frame on a fixed top to contain adjacent targets \(X_0,X_1\).
Write their omitted \(h\)-sets as

\[
                         P+a,\qquad P+b,
 \qquad |P|=h-1.
\]

In either orientation every conditioned frame has the form

\[
 (a,p_1,\ldots,p_{h-1},b,r_1,\ldots,r_{k-1}),
\tag{3.1}
\]

where the orders of \(P\) and of the remaining \((k-1)\)-set are
independent and uniform.

Fix a third rank-\(k\) target \(Z\ne X_0,X_1\), and let \(J\) be its
omitted \(h\)-set.  Direct start-position counting gives the following
complete cases.

* If \(J\) contains both distinguished endpoints, its conditional
  probability is zero.
* If \(J\) lies in the \((k-1)\)-block, its probability is

  \[
                    {k-h\over\binom{k-1}h}.
  \]

* If \(J\) contains exactly one distinguished endpoint and uses \(u\)
  elements of the opposite random block, where \(1\le u\le h-1\), its
  probability is

  \[
                    {1\over\binom{k-1}u\binom{h-1}u}.
  \]

Therefore

\[
 \boxed{
 \Pr(Z\text{ is a window}\mid X_0,X_1\text{ are windows})
 \le\beta_{h,k},}
\tag{3.2}
\]

with exact worst value

\[
 \boxed{
 \beta_{h,k}=\max\left\{
 {1\over(h-1)(k-1)},
 {k-h\over\binom{k-1}h}
 \right\}.}
\tag{3.3}
\]

At \(h=H,k=m\), with \(H\to\infty\) and \(H=o(m)\), the first term is
eventually the maximum:

\[
                         \beta_{H,m}={1\over(H-1)(m-1)}.
\tag{3.4}
\]

By the union bound, every forbidden target family \(\mathcal F\) disjoint
from \(X_0,X_1\) and satisfying

\[
                         |\mathcal F|\beta_{h,k}<1
\tag{3.5}
\]

is avoided by some actual conditioned frame.

### Theorem 3.1 (short-recourse lifting)

Let \(P_1,\ldots,P_t\) be pairwise vertex-disjoint adjacent middle-target
pairs.  If

\[
                         (t-1)M\beta_{H,m}<1,
\tag{3.6}
\]

and

\[
                         t\le\binom{m-1}{H-1},
\tag{3.6a}
\]

then there are \(t\) actual rooted cyclic-frame columns which contain
the respective pairs, use distinct tops, and are pairwise middle-target
disjoint.  Condition (3.6a) is automatic at the stated \(t=O(H)\) scale.

#### Proof

Choose the columns greedily.  At step \(i\), first choose an unused
compatible top; (3.2) is uniform in that top.  Then forbid every target
in the \(i-1\) earlier decks and both endpoints of every future pair.
The number of forbidden targets is at most

\[
                         (i-1)M+2(t-i)\le(t-1)M.
\]

Equation (3.5) supplies a conditioned frame avoiding them.  There are
\(\binom{m-1}{H-1}\) compatible tops for a prescribed adjacent pair;
this is much larger than \(t=O(H)\), so an unused top may be selected.
The future endpoints remain unused, and induction completes the lift.
\(\square\)

Using (3.4), one may take

\[
 \boxed{
 L=1+\left\lfloor{(H-1)(m-1)-1\over M}\right\rfloor
   =(1-o(1))H.}
\tag{3.7}
\]

Let a union of adjacent-pair cylinders have target-pair graph \(G\), and
write \(\tau(G)\) for its ordinary matching number and
\(\nu_{\rm cyl}\) for the middle-plus-root packet matching number of the
column union.
Theorem 3.1 gives

\[
 \boxed{\nu_{\rm cyl}\ge\min\{\tau(G),L\}.}
\tag{3.8}
\]

If \(\nu_{\rm cyl}<L\), then a maximum target-pair matching has at most
\(\nu_{\rm cyl}\) edges, and its endpoints cover every edge of \(G\).
Hence the entire cylinder union is contained in at most

\[
                         2\nu_{\rm cyl}
\]

ordinary target-star cylinders.  This is the already-cleared degree-one
sector.

If an unweighted union contains \(s\) complete adjacent-pair cylinders,
then

\[
 {y(\mathcal E)\over\nu_{\rm cyl}}
 \le {sD_{k,2}\over\min\{\tau(G),L\}}.
\]

Combining this with (2.5) proves the dichotomy:

* below \(L\), the support collapses to at most \(2\nu_{\rm cyl}\)
  target stars;
* outside that star sector, if the support-to-matching ratio is at least
  \(cR\), then

  \[
                         s\ge\left({c\over2}+o(1)\right)m^2H.
 \tag{3.9}
  \]

In particular, the normalized target ratio \((1-o(1))R\) forces
\((1-o(1))m^2H/2\) atoms.  The same conclusion extends to comparable
atom weights after normalization.  For arbitrary nonnegative weights
without comparability, Section 2.1 proves only the \(m^2\) effective-atom
bound (2.10).

No cross-row disjointness claim is made in Theorem 3.1.

## 4. Exact nested middle--entrance kernel

Fix a middle target \(X\) and an entrance target \(S\subset X\), with

\[
                         |X|=m,\qquad |S|=m-q.
\]

Condition on a cyclic frame selecting \(X\).  The complement of \(X\) in
the top is then one fixed \(H\)-block, while the internal linear order of
the \(m\) elements of \(X\) is uniform.  Put

\[
                         Q=X\setminus S,\qquad |Q|=q.
\]

The set \(S\) is a cyclic \((m-q)\)-window exactly when \(Q\) occupies
\(t\) initial and \(q-t\) terminal positions of the \(X\)-block, for one
of

\[
                         t=0,1,\ldots,q.
\]

These \(q+1\) position sets are disjoint.  Therefore

\[
 \boxed{
 \Pr(S\text{ is selected}\mid X\text{ is selected})
 ={q+1\over\binom mq}.}
\tag{4.1}
\]

If \(D_m\) is the global middle-target degree, the exact two-row codegree
is

\[
 \boxed{D(X,S)=D_m{q+1\over\binom mq}.}
\tag{4.2}
\]

For \(q=q_0=\lceil m^{1/4}\rceil\),

\[
                         {q+1\over\binom mq}=o(m^{-A})
\]

for every fixed \(A\).  Yet the reciprocal of the corresponding
within-fibre support has logarithm

\[
 O(H\log(m/H)+q\log(m/q))=o(m),
\]

so multiplication by \(N=\exp(\Theta(m))\) still tends to infinity.
The nested cylinder is therefore fibre-dense but globally
superpolynomially negligible.  No bounded or polynomial family of such
cylinders can revive the cleared entrance LP obstruction.

## 5. No invariant and no fibre-density coercivity

Fix one \(M\)-top and one complementary interval length \(h<M/2\).  Let
\(w\) be a weight on its \(h\)-subsets, and suppose

\[
                         \sum_{J\in\mathcal D_h(\pi)}w(J)
\]

is independent of the cyclic frame \(\pi\).  Swap two adjacent labels
\(a,b\) in a cyclic order.  If \(P,Q\) are the two disjoint
\((h-1)\)-sets immediately outside the swapped pair, invariance gives

\[
 w(P+a)-w(P+b)=w(Q+a)-w(Q+b).
\tag{5.1}
\]

The Kneser graph \(KG(M-2,h-1)\) is connected because \(M>2h\).
Therefore the exchange difference in (5.1) is independent of the core.
Johnson four-cycles then integrate these differences, giving

\[
 \boxed{w(J)=c+\sum_{x\in J}\alpha_x.}
\tag{5.2}
\]

Conversely every affine weight has constant deck score.  Thus degree
zero and one are the complete annihilator; there is no hidden parity or
fixed higher-harmonic linear invariant on one top.

The conclusion also holds for the coupled middle--entrance column, and
more generally for any set of distinct controlled lengths.

### Lemma 5.1 (multi-length annihilator)

Let

\[
                  1\le h_1<\cdots<h_s=K,\qquad M\ge2K+1.
\]

For each \(j\), let \(w_j\) be a weight on the \(h_j\)-subsets of one
\(M\)-set.  If

\[
       \sum_{j=1}^s\sum_{J\in\mathcal D_{h_j}(\pi)}w_j(J)
\tag{5.3a}
\]

is independent of the cyclic frame \(\pi\), then every \(w_j\) is
affine on its own slice.

#### Proof

For adjacent labels \(a,b\), let \(P_j,Q_j\) be the nested left and
right \((h_j-1)\)-cores in the adjacent-swap identity, and write

\[
 \delta_{j,ab}(P)=w_j(P+a)-w_j(P+b).
\]

The swap identity is

\[
 \sum_j\bigl(\delta_{j,ab}(P_j)-\delta_{j,ab}(Q_j)\bigr)=0.
\tag{5.3b}
\]

Take adjacent \((K-1)\)-sets \(P_s,P_s'\).  Their intersection has size
\(K-2\), so it contains nested cores for every smaller \(h_j\).  Since
\(M\ge2K+1\), there is a \((K-1)\)-set \(Q_s\) disjoint from
\(P_s\cup P_s'\cup\{a,b\}\).  Realize (5.3b) twice, with the same lower
cores and the same right cores but with \(P_s\) and \(P_s'\).  Subtraction
gives

\[
                         \delta_{s,ab}(P_s)
                         =\delta_{s,ab}(P_s').
\]

The Johnson graph on the \((K-1)\)-cores is connected, so
\(\delta_{s,ab}\) is core-independent.  Its two terms cancel from
(5.3b).  Descending induction isolates every length.  Core-independent
exchange differences integrate on Johnson four-cycles to
\(w_j(J)=c_j+\sum_{x\in J}\alpha_{j,x}\).  No division was used, so the
argument is valid over every field.  \(\square\)

For the global promotion fibre, a rank-\(k_j=M-h_j\) target \(X\subset U\)
corresponds to the local complement \(J=U\setminus X\).  Hence a global
weight orthogonal to every legal combined frame difference restricts,
by Lemma 5.1, to an affine function on the \(k_j\)-subsets of every top.
Every Johnson four-cycle of rank \(k_j\) lies in some \(M\)-top when
\(h_j\ge2\); its rectangle difference therefore vanishes.  Johnson
four-cycle integration makes the global weight affine on that entire
rank slice.

Consequently, for the middle and entrance rows together, the annihilator
of all legal combined frame differences is exactly the direct sum of the
two affine slice spaces.  Equivalently, over \(\mathbb R\) or any finite
field, the legal differences span all paired load directions having
separately zero total and zero point margins in each row.  There is no
cross-row linear or modular invariant hidden above degree one.

This does not give a positive quantitative gap.  Let \(w=\mathbf1_{J_0}\)
for one fixed \(h\)-set.  Some cyclic frame avoids \(J_0\), whereas the
uniform frame selects it with probability \(p_k\).  Hence

\[
 \boxed{
 \mathbb E_\pi\langle w,c_\pi\rangle
 -\min_\pi\langle w,c_\pi\rangle=p_k.}
 \tag{5.4}
\]

Subtracting the affine projection of \(w\) changes every deck score by
the same constant, so the genuine higher-harmonic quotient has the same
spread.  Meanwhile the supporting set of physical columns in one fibre
has size \(p_kR\), and

\[
                         p_kN\to\infty.
\]

At the critical middle scale,

\[
 p_m=\exp\left[-\left({1\over2}+o(1)\right)
          \sqrt m(\log m)^{3/2}\right].
 \tag{5.5}
\]

Thus an actual, nonaffine, fibre-dense direction may have exponentially
small cyclic-score spread.  Summing one such normalized direction per
top gives only

\[
                         Np_m=o(W).
\]

No theorem based solely on “higher harmonic plus fibre density” can
force the \(\Omega(W)\) spread in (1.14).

The same conclusion holds for state-independent PSD seminorms.  The
global span of legal frame differences contains every load direction
with zero total and zero point margins; equivalently, its annihilator is
the affine slice space.  Therefore a PSD seminorm which vanishes on every
legal difference also vanishes on the entire collision-deviation space.
The surviving Gram information must be statewise, owner-indexed, and
nonlinear.

### 5.2 The physical covariance lives at growing degree but has no PSD gap

There is an exact complementary harmonic statement.  For one middle
deck on an \(M=m+H\) top, let

\[
 c_\pi=\mathbf1_{\mathcal D_H(\pi)},\qquad
 z_\pi=c_\pi-p\mathbf1,\qquad p={M\over\binom MH},
\]

and let

\[
                         a_j=\|P_jz_\pi\|_2^2
\]

be its local Johnson degree-\(j\) mass.  The deck is an exact point
design, so \(a_1=0\), and direct transposition counting gives

\[
 \boxed{
 \sum_{j=2}^Hj(M-j+1)a_j=M(mH-2).}
\tag{5.6}
\]

Indeed each of the \(M\) deck windows has \(mH\) crossing
transpositions, exactly two of which send it to another deck window.
Using \(\sum_{j=2}^Ha_j=M(1-p)\) and subtracting (5.6) from the top
eigenvalue gives

\[
 \boxed{
 \sum_{j=2}^{H-1}(H-j)(m+1-j)a_j
 =M\bigl(H+2-pH(m+1)\bigr).}
\tag{5.7}
\]

Consequently

\[
 \boxed{
 a_H\ge M(1-p)-{M(H+2)\over m-H+2}=M-O(H).}
\tag{5.8}
\]

Thus a \(1-O(H/m)\) fraction of every physical column's centered norm is
in its *highest* local harmonic \(E_H(U)\); every fixed Johnson-degree
sector carries \(o(1)\) mass at the tuned height.

This does not yield coercivity.  The top-dependent spaces \(E_H(U)\)
overlap in the global middle layer.  The map

\[
 \bigoplus_U E_H(U)\longrightarrow\mathbb R^{\binom{[2m]}m},
 \qquad (g_U)_U\longmapsto\sum_U\widetilde g_U
\tag{5.9}
\]

has kernel dimension at least

\[
 W\left[
 \binom mH\left(1-{H\over m+1}\right)-1
 \right],
\tag{5.10}
\]

using
\[
 N\binom MH=W\binom mH,\qquad
 \dim E_H(U)=\binom MH\left(1-{H\over m+1}\right).
\]
Moreover the origin lies in the convex hull of each projected physical
orbit.  Hence the statewise diagonal \(W-o(W)\) high-harmonic mass can be
cancelled by cross-top inner products; the convexified bundle has no PSD
separation.  The complete covariance recursion is recorded in
MATH_THEOREM_L_PROMOTION_RING_HIGH_HARMONIC_COVARIANCE_AND_LOAD_ONLY_NOGO_20260726.md.

## 6. Paired-orbit obstruction and the sharp legality correction

The companion theorem

`MATH_OBSTRUCTION_PROMOTION_RING_DISJOINT_TRANSPOSITION_PRIVATE_ORBITS_20260726.md`

constructs, for every fixed \(d\ge1\), an actual physical state which is
local against every compound switch built from **paired top-orbit
replacements** for \(d\) prescribed disjoint transpositions and satisfies

\[
 \Psi_m\ge(2^d-1)2^{-d-1}e^{-2^d}W.
\tag{6.1}
\]

The proof uses full \((\mathbb Z/2)^d\)-orbits \(Q\) of middle targets.
For a suitable random base state, a positive-density family has total
load exactly one.  That total is preserved by every paired-orbit switch
for a generator, so every state in that restricted generated
component has \(2^d-1\) holes on each such orbit.  A minimum-energy state
in the finite restricted component has the linear floor (6.1).

This is **not** a local minimum in the literal one-frame-per-top product
fibre.  For two full selections \(F,G\), replacing the frame at a single
top \(U\) by \(G_U\) is already legal.  In particular, in the comparison
with \(\tau F\), one may replace \(F_U\) by
\((\tau F)_U=\tau F_{\tau U}\) without simultaneously changing
\(\tau U\).  Such a one-top move need not preserve the orbit total used
in (6.1).  Pairing \(U\) with \(\tau U\) is useful for the symmetric Gram
identity, but it is an extra restriction, not an integrality requirement.

The unrestricted product move graph is connected for the simpler reason
that every top frame may be replaced independently.  Equivalently, if
only coordinate-transposition alternatives are desired, then for every
top \(U\) and every \(a,b\in U\), the transposition \((a\ b)\) fixes
\(U\), and changing only that top sends its frame to the transposed
frame.  These moves generate every cyclic frame on \(U\).  Hence no
nonconstant exact state invariant survives the full legal product fibre.

The final boundary is therefore exact.

* Fixed bounded **paired-orbit** transposition atlases have actual
  \(\Omega(W)\) bad restricted local minima.
* This does not obstruct independent one-top replacements in the actual
  product fibre.
* Bounded or sub-\(H\) degree-two cylinder systems reduce to cleared
  stars or have \(o(R)\) dual mass.
* Bounded or polynomial nested middle--entrance systems have negligible
  reciprocal-binomial mass.
* No state-independent linear, modular, or PSD invariant remains after
  all legal frame differences are admitted.

The only surviving positive-cut theorem must couple a growing family of
transpositions and a diffuse owner-sensitive mesh of at least
\(\Omega(m^2H)\) comparable degree-two atoms, or an equally large
cross-row substitute.  Whether such a mesh forces a positive cut or
supports an all-transposition bad local minimum remains open.
