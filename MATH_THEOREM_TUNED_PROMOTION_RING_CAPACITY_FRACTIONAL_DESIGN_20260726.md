# Tuned promotion rings: capacity, the exact fractional design, and the first vertical codegree

Date: 2026-07-26

Method: pure mathematics.  No computation, search, or external theorem is
used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 \lambda_q={W\over N_q}.
 \tag{0.1}
\]

Choose

\[
 q_0=\lceil m^{1/4}\rceil,\qquad
 H=\left\lfloor\sqrt{m\log m}\right\rfloor,\qquad
 M=m+H,
 \tag{0.2}
\]

where logarithms are natural.  The rank-(M) tops are counted by

\[
 \binom{2m}{M}=\binom{2m}{m-H}=N_H.
\]

For all sufficiently large \(m\), the following statements hold.

1.  The scalar capacity is on the covering side of the crossing:

    \[
    \boxed{M N_H\ge W>N_{q_0},\qquad
           0\le M N_H-N_{q_0}
              =O\!\left(W\sqrt{\frac{\log m}{m}}\right)=o(W).}
    \tag{0.3}
    \]

2.  The number of promotion rings is negligible even after an
    \(H\)-long linearization collar:

    \[
    \boxed{N_H=(1+o(1)){W\over m},\qquad
           N_H=o(W/H),\qquad HN_H=o(W).}
    \tag{0.4}
    \]

3.  On every top \(U\in\binom{[2m]}M\), average uniformly over its
    \((M-1)!\) oriented cyclic frames.  This gives an explicit feasible
    fractional point with exactly one frame per top.  Every signed target
    of depth \(q_0\le q<H\) has load

    \[
    \boxed{\theta_q={M N_H\over N_q}\ge1,}
    \tag{0.5}
    \]

    every lower target at depth \(H\) has load \(M\), and every upper
    depth-\(H\) target is its own top tag and has load exactly one.  The
    middle-owner load is

    \[
    \theta_0={M N_H\over W}=1+O\!\left(\sqrt{\frac{\log m}{m}}\right),
    \qquad W(\theta_0-1)=o(W).
    \tag{0.6}
    \]

    Thus there is no scalar or Farkas obstruction to the one-frame-per-top
    annulus covering relaxation.  The fractional point even pays only
    \(o(W)\) middle surplus.

4.  Same-rank target codegrees are exceptionally small.  Away from the
    single upper coatom row their maximum relative value is

    \[
    \boxed{{2\over r(2m-r)}=O(m^{-2}).}
    \tag{0.7}
    \]

    The first nontrivial dependence is vertical.  If \(S\subset T\),
    \(|S|=r\), \(|T|=r+1<M\), then

    \[
    \boxed{{\deg(S,T)\over D_{r+1}}={2\over r+1},\qquad
           {\deg(S,T)\over D_r}={2\over2m-r}.}
    \tag{0.8}
    \]

    Hence adjacent nested rows have relative codegree
    \(\Theta(m^{-1})\), a factor \(m\) larger than the horizontal
    codegree.  This is not a fractional obstruction; it is the first
    precise obstruction to treating the \(\Theta(H)\) rows as unrelated
    vertices in a black-box small-codegree matching theorem.

What is not proved is an integral choice of one frame on every top whose
interval targets cover the whole annulus with \(o(W)\) holes and whose
middle collisions are \(o(W)\).  The note isolates that as a purely
integral, vertically correlated rounding problem; all capacity and linear
feasibility assertions are settled exactly.

This is deliberately the **full-ring set-cover relaxation**.  It should
not be confused with the stronger truncated/SCD-compatible formulation in
which active starts have prescribed radius census
\(N_d-N_{d+1}\).  The full ring supplies \(M\) occurrences at every
non-top depth; it proves the coefficient-one capacity and cover LP, but
not that exact census.

## 1. Binomial-ratio estimates at the literal floor height

We first record an expansion with an error smaller than the top-capacity
increment (H/m).

### Lemma 1.1 (uniform ratio expansion)

If (q=o(m)), then

\[
 \log\lambda_q
 =\frac{q^2}{m}-\frac{q^2}{2m^2}
   +O\!\left(\frac{q^4}{m^3}+\frac{q^5}{m^4}\right).
 \tag{1.1}
\]

In particular, uniformly for (q\le H),

\[
 \log\lambda_q={q^2\over m}
 +O\!\left({q^2\over m^2}+{q^4\over m^3}\right).
 \tag{1.2}
\]

#### Proof

The exact product is

\[
 \lambda_q=\prod_{i=1}^q{m+i\over m-i+1}.
 \tag{1.3}
\]

For (q<m/2), Taylor expansion with a uniform remainder gives

\[
\begin{aligned}
 \log{m+i\over m-i+1}
 &=\log(1+i/m)-\log(1-(i-1)/m)\\
 &=\frac{2i-1}{m}-\frac{2i-1}{2m^2}
   +\frac{i^3+(i-1)^3}{3m^3}
   +O(i^4/m^4).
\end{aligned}
\]

Now

\[
 \sum_{i=1}^q(2i-1)=q^2,
 \qquad \sum_{i=1}^q i^3=O(q^4),
 \qquad \sum_{i=1}^q i^4=O(q^5),
\]

which proves (1.1), and (1.2) follows. \(\square\)

### Lemma 1.2 (the floor height lies on the covering side)

For all sufficiently large (m),

\[
 \lambda_H<M=m+H.
 \tag{1.4}
\]

Moreover

\[
 \lambda_H=m\exp(O(H/m)),
 \qquad
 1\le {M\over\lambda_H}=1+O(H/m).
 \tag{1.5}
\]

#### Proof

Let (x=\sqrt{m\log m}).  Since (x-1<H\le x),

\[
 \log m-2\sqrt{\frac{\log m}{m}}
 \le {H^2\over m}\le\log m.
 \tag{1.6}
\]

At (q=H), the error in (1.2) is

\[
 O\!\left({\log m\over m}+{(\log m)^2\over m}\right)
 =o(H/m).
 \tag{1.7}
\]

Consequently

\[
 \log(\lambda_H/m)=O(H/m)
 \tag{1.8}
\]

and, using the upper half of (1.6),

\[
 \log(\lambda_H/m)
 \le O((\log m)^2/m)=o(H/m).
 \tag{1.9}
\]

On the other hand

\[
 \log(M/m)=\log(1+H/m)
 ={H\over m}+O(H^2/m^2).
 \tag{1.10}
\]

Equations (1.9)--(1.10) prove (1.4).  Combining (1.8) and
(1.10) gives (1.5), with the lower bound following from (1.4).
\(\square\)

### Theorem 1.3 (capacity and surplus)

Equation (0.3) holds.  More explicitly,

\[
 M N_H-W=O(WH/m),
 \qquad
 W-N_{q_0}=Wm^{-1/2}+O(Wm^{-3/4}).
 \tag{1.11}
\]

#### Proof

Since (N_H=W/\lambda_H), Lemma 1.2 gives

\[
 M N_H=W{M\over\lambda_H}\ge W,
 \qquad
 M N_H-W=O(WH/m).
 \tag{1.12}
\]

At (q_0=\lceil m^{1/4}\rceil), Lemma 1.1 gives

\[
 \log\lambda_{q_0}
 =m^{-1/2}+O(m^{-3/4}).
 \tag{1.13}
\]

Therefore

\[
 {N_{q_0}\over W}
 =e^{-\log\lambda_{q_0}}
 =1-m^{-1/2}+O(m^{-3/4}),
 \tag{1.14}
\]

which proves (1.11).  Finally

\[
 M N_H-N_{q_0}=(M N_H-W)+(W-N_{q_0})
 =O\!\left(W\sqrt{\frac{\log m}{m}}\right)=o(W).
\]

This proves (0.3). \(\square\)

### Corollary 1.4 (ring and reset counts)

Equation (0.4) holds.

#### Proof

From (1.5),

\[
 N_H={W\over\lambda_H}=(1+O(H/m)){W\over m}.
\]

Thus

\[
 {N_H\over W/H}={H\over\lambda_H}
 =(1+o(1)){H\over m}\longrightarrow0.
\]

The assertion (HN_H=o(W)) is the same calculation. \(\square\)

### Proposition 1.5 (exact crossing-tuned variant)

If instead one defines

\[
 \widehat H=\max\{h:(m+h)N_h\ge W\},
 \qquad \widehat M=m+\widehat H,
 \tag{1.15}
\]

then \(\widehat H=(1+o(1))\sqrt{m\log m}\) and the surplus has the
exact one-step bound

\[
 \boxed{
 0\le \widehat M N_{\widehat H}-W
 <2\widehat H N_{\widehat H}.}
 \tag{1.16}
\]

Consequently every conclusion of Sections 2--4 remains true with hats,
and

\[
 0\le\widehat M N_{\widehat H}-N_{q_0}=o(W).
 \tag{1.17}
\]

#### Proof

Put \(T_h=(m+h)N_h\).  The adjacent binomial ratio gives the exact
identity

\[
 {T_{h+1}\over T_h}
 ={m-h\over m+h}.
 \tag{1.18}
\]

Maximality gives \(T_{\widehat H+1}<W\le T_{\widehat H}\).  Hence

\[
\begin{aligned}
 0\le T_{\widehat H}-W
 &<T_{\widehat H}-T_{\widehat H+1}\\
 &={2\widehat H\over m+\widehat H}T_{\widehat H}
 =2\widehat HN_{\widehat H},
\end{aligned}
\]

proving (1.16).  Lemma 1.1 locates the crossing at
\((1+o(1))\sqrt{m\log m}\).  Therefore
\(\widehat HN_{\widehat H}=O(W\widehat H/m)=o(W)\), and (1.17)
follows from (1.14). \(\square\)

## 2. One physical promotion ring per top

For (U\in\binom{[2m]}M), let

\[
 \pi=(u_0,u_1,\ldots,u_{M-1})
\]

be an oriented cyclic frame, with indices modulo (M).  Put

\[
 X_j=I_\pi(j,m)=\{u_j,u_{j+1},\ldots,u_{j+m-1}\}.
 \tag{2.1}
\]

Then

\[
 X_{j+1}=X_j-\{u_j\}+\{u_{j+m}\},
 \tag{2.2}
\]

so the (M) owners form a literal cyclic Johnson walk.  For
(0\le q\le H),

\[
 \bigcap_{t=0}^{q}X_{j+t}=I_\pi(j+q,m-q),
 \qquad
 \bigcup_{t=0}^{q}X_{j+t}=I_\pi(j,m+q).
 \tag{2.3}
\]

Thus the lower and upper depth-(q) flags are precisely the cyclic
intervals of lengths (m-q) and (m+q) in the same frame.  At
(q=H), the upper flag is (U) itself.  Repeating the first (H)
owners when a ring is linearized exposes every rooted flag through depth
(H), at cost (H) per ring.  Corollary 1.4 shows that this total collar
cost is (o(W)).

## 3. The tag--target hypergraph and its fractional point

Let

\[
 \mathcal U=\binom{[2m]}M
\]

be the tag set.  For every (U\in\mathcal U), let
(\mathcal C(U)) be the ((M-1)!) oriented cyclic frames on (U),
modulo rotation.  A formal edge (e(U,\pi)) contains

* its tag (U);
* its (M) middle owners (I_\pi(j,m));
* for every (q_0\le q\le H), its (M) lower intervals of length
  (m-q);
* for every (q_0\le q<H), its (M) upper intervals of length (m+q).

The upper depth-\(H\) target is the tag \(U\) and is not duplicated as a
second set vertex.  This convention records set coverage.  Dynamically the
same top occurs at all \(M\) roots at depth \(H\), but those occurrences
represent one covered mask and one selected top tag.  Any
occurrence-balanced energy at that terminal row is a different
optimization problem.

For (1\le r<M), write (D_r) for the number of formal edges containing
a fixed rank-(r) target.

### Proposition 3.1 (exact degrees)

For every (1\le r<M),

\[
 \boxed{
 D_r=\binom{2m-r}{M-r}r!(M-r)!
 ={r!(2m-r)!\over(m-H)!}.}
 \tag{3.1}
\]

For a fixed incident tag--target pair (S\subset U), the codegree is

\[
 \boxed{\deg(U,S)=r!(M-r)!.}
 \tag{3.2}
\]

Its two useful normalizations are

\[
 \boxed{
 {\deg(U,S)\over(M-1)!}={M\over\binom Mr},
 \qquad
 {\deg(U,S)\over D_r}
 ={1\over\binom{2m-r}{M-r}}.}
 \tag{3.2a}
\]

#### Proof

Choose a top containing (S).  Within that top, contract (S) to one
cyclic block.  The block has (r!) internal orders, and the resulting
(M-r+1) cyclic objects have ((M-r)!) cyclic orders.  This proves
(3.1)--(3.2). \(\square\)

### Theorem 3.2 (uniform fractional tag--target design)

Assign

\[
 x_{U,\pi}={1\over(M-1)!}
 \tag{3.3}
\]

to every formal edge.  Then

\[
 \sum_{\pi\in\mathcal C(U)}x_{U,\pi}=1
 \qquad(U\in\mathcal U),
 \tag{3.4}
\]

and every rank-(r<M) target has load

\[
 \boxed{
 \sum_{(U,\pi):\,S\in e(U,\pi)}x_{U,\pi}
 ={D_r\over(M-1)!}
 ={M N_H\over\binom{2m}{r}}.}
 \tag{3.5}
\]

Consequently all signed targets at depths (q_0\le q<H), and all lower
targets at depth (H), have load at least one.  Every upper depth-(H)
target has tag load one.  The total middle surplus is (M N_H-W=o(W)).

#### Proof

Equation (3.4) is immediate.  Equation (3.5) follows either from (3.1)
or by double counting: there are (N_H) units of top weight, and every
unit supplies (M) rank-(r) intervals.  Coordinate transitivity makes
their load constant, so it is (M N_H/\binom{2m}{r}).

For (r=m\pm q), the denominator is (N_q).  Since (N_q) decreases
with (q\ge0), Theorem 1.3 gives

\[
 {M N_H\over N_q}\ge {M N_H\over N_{q_0}}\ge1
 \qquad(q\ge q_0).
\]

The middle assertion is (1.12). \(\square\)

### Corollary 3.3 (no Farkas obstruction)

Consider the linear system

\[
 x_{U,\pi}\ge0,\qquad
 \sum_\pi x_{U,\pi}=1,
 \qquad
 \sum_{(U,\pi):S\in e(U,\pi)}x_{U,\pi}\ge1
 \tag{3.6}
\]

for every top tag and every annulus target described above.  This system
is feasible.  Hence no Farkas dual certificate exists against the tuned
promotion-ring relaxation.

If middle owners are also given unit upper capacities with nonnegative
slacks (z_X), the uniform point satisfies

\[
 \operatorname{load}(X)\le1+z_X,qquad
 z_X={M N_H-W\over W},qquad
 \sum_Xz_X=M N_H-W=o(W).
 \tag{3.7}
\]

Thus the complete fractional obstruction is absent even after the true
middle-collision budget is included.

There is one harmless exact dual obstruction worth recording.  If the
slacks in (3.7) are forbidden, summing the \(W\) unit owner capacities
gives total capacity \(W\), whereas the top equalities force total owner
mass \(M N_H>W\).  The all-ones owner dual therefore certifies
infeasibility of a collision-free full-ring packing.  Its deficiency is
**exactly**

\[
 M N_H-W=o(W),
\]

and (3.7) attains that lower bound.  Thus the only scalar Farkas
obstruction is precisely the already-budgeted \(o(W)\) owner surplus; no
annulus target obstruction remains.

## 4. Horizontal and vertical codegrees

The useful feature of the design is its horizontal sparsity; the useful
warning is that this sparsity does not persist vertically.

For two equal-sized targets (S,T), put

\[
 d=|S\setminus T|=|T\setminus S|,
 \qquad s_r=\min(r,M-r),
 \]

and define

\[
 a_{r,M}(d)=
 \begin{cases}
 2,&1\le d<s_r,\\
 M-2s_r+1,&d=s_r,\\
 0,&d>s_r.
 \end{cases}
 \tag{4.1}
\]

### Proposition 4.1 (exact same-rank codegree)

For distinct rank-(r) targets,

\[
 \boxed{
 {\deg(S,T)\over D_r}
 ={a_{r,M}(d)\over
   \binom rd\binom{2m-r}{d}}.}
 \tag{4.2}
\]

In particular, throughout the lower annulus and throughout the upper
annulus up to depth (H-2),

\[
 \max_{S\ne T}{\deg(S,T)\over D_r}
 ={2\over r(2m-r)}=(2+o(1))m^{-2}.
 \tag{4.3}
\]

At the upper coatom row (r=M-1),

\[
 \max_{S\ne T}{\deg(S,T)\over D_{M-1}}
 ={1\over m-H+1}=O(m^{-1}).
 \tag{4.4}
\]

This row has (N_{H-1}=O(W/m)=o(W/H)) targets.

#### Proof

Conditional on a frame in a fixed top containing (S) as an interval,
there are (a_{r,M}(d)) relative shifts whose interval is at distance
(d).  Symmetry among the

\[
 \binom rd\binom{M-r}{d}
\]

rank-(r) targets at that distance inside the top gives conditional
probability (a_{r,M}(d)) divided by this number.  Conditional on a
random top containing (S), the probability that it also contains
(T\setminus S) is

\[
 {\binom{2m-r-d}{M-r-d}\over\binom{2m-r}{M-r}}
 ={\binom{M-r}{d}\over\binom{2m-r}{d}}.
\]

Multiplication proves (4.2).  The (d=1) value gives (4.3); the boundary
value is smaller when (s_r\ge2).  When (r=M-1), every coatom of a
top is an interval, and (4.2) reduces to (4.4).  Finally
(N_{H-1}=(1+o(1))W/m) follows from Lemma 1.1 exactly as in Corollary
1.4. \(\square\)

### Proposition 4.2 (exact nested cross-rank codegree)

Let \(S\subset T\), with \(|S|=r<|T|=s<M\).  Then

\[
 \boxed{
 \deg(S,T)=D_s\,{s-r+1\over\binom sr}.}
 \tag{4.5}
\]

For \(s=r+1\), this gives the two normalizations in (0.8).

#### Proof

Condition on a formal edge containing \(T\).  The interval \(T\) has a
uniform linear internal order.  A prescribed \(r\)-subset \(S\subset T\)
is an interval in that order exactly when it occupies one of the
\(s-r+1\) consecutive subblocks, out of the \(\binom sr\) possible
\(r\)-subsets.  This proves (4.5).

When \(s=r+1\), the ratio to \(D_s\) is \(2/(r+1)\).  Also

\[
 {D_{r+1}\over D_r}={r+1\over2m-r},
\]

which gives the ratio \(2/(2m-r)\) to \(D_r\). \(\square\)

### Remark 4.3 (the exact black-box warning)

One formal frame contains \(\Theta(MH)=\Theta(m^{3/2}\sqrt{\log m})\)
signed annulus incidences.  The largest genuine interior dependence is
the adjacent vertical value \(\Theta(1/m)\), not the horizontal
\(O(m^{-2})\) value.  Their product is \(\Theta(H)\), which diverges.
Therefore a theorem that flattens all target ranks into one ordinary
uniform hypergraph and tests only ``edge size times maximum relative
codegree'' does not close this instance.  A successful integral theorem
must exploit the fact that the vertical incidences form nested interval
columns of one cyclic frame.

This is a limitation of current generic rounding, not a Farkas or
capacity obstruction: Theorem 3.2 is an explicit feasible fractional
point.

### Proposition 4.4 (independent frame rounding fails at the entrance)

Choose the frame on each top independently and uniformly.  For a fixed
rank-\((m-q_0)\) entrance target \(S\), let

\[
 R=\binom{m+q_0}{H+q_0}
 \tag{4.6}
\]

be the number of tops containing it.  In each eligible top, the
probability that \(S\) is a cyclic interval is

\[
 p={M\over\binom{M}{m-q_0}}
   ={M\over\binom{M}{H+q_0}}.
 \tag{4.7}
\]

Then

\[
 Rp={M N_H\over N_{q_0}}=1+o(1),\qquad p=o(1),
 \tag{4.8}
\]

and hence

\[
 \boxed{\Pr(S\text{ is missed})=(1-p)^R=e^{-1}+o(1).}
 \tag{4.9}
\]

Consequently independent rounding has
\((e^{-1}+o(1))N_{q_0}=\Theta(W)\) expected entrance holes.

#### Proof

The count \(R\) is immediate.  The local interval probability is the
first ratio in (3.2a), proving (4.7), while (4.8) is the degree identity
(3.5).  Both \(H+q_0\) and its complement in \(M\) tend to infinity, so
\(p=o(1)\).  Therefore

\[
 R\log(1-p)=-Rp+O(Rp^2)=-1+o(1),
\]

because \(Rp^2=(Rp)p=o(1)\).  This proves (4.9). \(\square\)

Thus the open theorem is genuinely a correlated resolution theorem:
neither the fractional point nor independent randomized rounding supplies
the needed near-cover at mean one.

## 5. The remaining integral statement

The tuned promotion-ring lane is now equivalent to the following
rounding problem.

> **Tuned vertical frame theorem (open).**  Choose one oriented cyclic
> frame \(\pi_U\) for every \(U\in\binom{[2m]}{m+H}\) such that
> 
> \[
> \sum_X(\operatorname{load}_m(X)-1)_+=o(W)
> \]
> 
> and the aggregate number of uncovered signed targets at depths
> \(q_0\le q\le H\) is \(o(W)\).

If this theorem holds, concatenating the \(N_H\) promotion rings with an
\(H\)-collar costs

\[
 M N_H+O(HN_H)=W+o(W).
\]

The scalar capacity, number of components, physical chronology, exact
fractional design, and horizontal codegrees are no longer open.  The sole
gate is integral rounding under the adjacent vertical correlation
(0.8).
