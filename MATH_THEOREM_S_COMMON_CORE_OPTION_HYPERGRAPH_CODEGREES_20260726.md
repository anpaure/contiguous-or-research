# Exact degrees, codegrees, and one-wave influence for the common-core promotion atlas

Date: 2026-07-26

Method: pure mathematics only. No finite search, computation, solver, or web
input is used.

## 0. Scope and conclusion

Let

\[
 M=m+H,\qquad s=m-H,\qquad n=s-H=m-2H,
 \qquad L=n-H+1=m-3H+1,
\tag{0.1}
\]

and assume throughout that \(H\ge2\) and \(m>4H\). Put

\[
 W=\binom{2m}{m},\qquad N_H=\binom{2m}{m-H},
 \qquad \Lambda=\frac{W}{N_H}
 =\frac{M!s!}{(m!)^2}.
\tag{0.2}
\]

This note audits the rooted middle-shadow hypergraph of the literal
common-core partial promotion paths. At the calibrated height below, its
exact largest pair codegree is the distance-one middle pair:

\[
 \frac{\Delta_2}{D_X}
 =\frac{2(L-1)}{Lm^2}.
\tag{0.3}
\]

At the calibrated height

\[
 H=(1+o(1))\sqrt{m\log m},\qquad \Lambda=m+O(H),
\tag{0.4}
\]

this is \((2+o(1))/m^2\). The uniformity is \(L+1\), so the crude
quantity \(L^2\Delta_2/D_X\) tends to \(2\), not to zero.
Nevertheless, linear tight-path geometry gives the sharper and
asymptotically exact link-influence bound

\[
 \max_{X\notin e}
 \frac{|\{f:X\in f,\ f\cap e\ne\varnothing\}|}{D_X}
 =\frac{6(L-1)}{Lm^2}+O(m^{-4}).
\tag{0.5}
\]

Thus the initial random-priority bite has the desired \(m^{-2}\) link
spread. This is a one-wave theorem only. It does not prove hereditary
regeneration of the residual option menus, a near-perfect rooted
matching, simultaneous lower/upper trace disjointness, or EP_A.

## 1. The decorated option hypergraph

Let

\[
 \mathcal U=\binom{[2m]}M,\qquad
 \mathcal X=\binom{[2m]}m.
\tag{1.1}
\]

A **decorated option** is a triple

\[
 (U,Q,w),
\tag{1.2}
\]

where

\[
 U\in\mathcal U,\qquad Q\in\binom U{2H},
\tag{1.3}
\]

and

\[
 w=(w_1,\ldots,w_n)
\tag{1.4}
\]

is an injective word in \(U\setminus Q\). For \(1\le i\le L\), define

\[
 B_i(w)=\{w_i,w_{i+1},\ldots,w_{i+H-1}\},
 \qquad X_i(U,w)=U\setminus B_i(w).
\tag{1.5}
\]

The rooted hyperedge is

\[
 e(U,Q,w)=\{U\}\cup\{X_i(U,w):1\le i\le L\}.
\tag{1.6}
\]

The \(X_i\)'s are distinct. The core \(Q\) is unordered, the word \(w\)
is oriented and ordered, and the \(H\) elements of \(U\setminus(Q\cup
\{w_1,\ldots,w_n\})\) are left unordered. All counts below use exactly
this convention unless explicitly stated otherwise.

## 2. Exact vertex degrees and root--middle codegrees

### Theorem 2.1 (degrees)

Every root \(U\) has degree

\[
 \boxed{
 D_U=\binom M{2H}(s)_n
     =\binom M{2H}\frac{s!}{H!}
     =\frac{M!}{(2H)!H!}.}
\tag{2.1}
\]

Every middle owner \(X\) has degree

\[
 \boxed{
 D_X=\binom mH\binom m{2H}Ln!
     =\frac{L(m!)^2}{(2H)!H!s!}.}
\tag{2.2}
\]

Consequently

\[
 \boxed{\frac{D_X}{D_U}=\frac L\Lambda.}
\tag{2.3}
\]

In particular, under (0.4), the rooted hypergraph is
\((1+O(H/m))\)-regular, with the root degree the larger degree.

#### Proof

For a fixed root, choose the unordered core and then an injection of
length \(n\) into the remaining \(s\) coordinates. This gives (2.1).

Fix \(X\in\mathcal X\). An incident option has a unique occurrence of
\(X\), because distinct windows of an injective word are distinct. Choose

\[
 U\supset X \quad\text{in}\quad \binom mH\ \text{ways},
\tag{2.4}
\]

and write \(A=U\setminus X\). Choose

\[
 Q\in\binom X{2H}.
\tag{2.5}
\]

For a prescribed one of the \(L\) window positions, order the \(H\)
elements of \(A\) in \(H!\) ways. Fill the other \(n-H\) word positions
injectively from the \(n=s-H\) elements of \((U\setminus Q)\setminus A\).
The count is

\[
 H!(n)_{n-H}=H!\frac{n!}{H!}=n!.
\tag{2.6}
\]

This proves the first expression in (2.2). Direct cancellation gives the
second expression and (2.3). \(\square\)

### Theorem 2.2 (rooted pair codegrees)

Distinct root vertices have codegree zero. For a root \(U\) and a middle
owner \(X\),

\[
 \boxed{
 d(U,X)=
 \begin{cases}
 \displaystyle \binom m{2H}Ln!=\frac{Lm!}{(2H)!},&X\subset U,\\[1ex]
 0,&X\not\subset U.
 \end{cases}}
\tag{2.7}
\]

For an incident pair,

\[
 \frac{d(U,X)}{D_X}=\frac1{\binom mH},
 \qquad
 \frac{d(U,X)}{D_U}=\frac L{\binom MH}.
\tag{2.8}
\]

#### Proof

Once \(U\supset X\) is fixed, the argument in (2.4)--(2.6) remains, but
the choice of \(U\) disappears. This proves (2.7); (2.8) follows by
cancellation. A hyperedge contains exactly one root, proving the first
claim. \(\square\)

## 3. Exact two-window count

Let distinct \(X,Y\in\mathcal X\) have Johnson distance

\[
 d=d_J(X,Y)=|X\setminus Y|=m-|X\cap Y|.
\tag{3.1}
\]

### Lemma 3.1 (two prescribed windows in one tail)

Fix a common root \(U\supset X\cup Y\) and a core
\(Q\subset X\cap Y\) of size \(2H\). Put

\[
 A=U\setminus X,\qquad B=U\setminus Y.
\tag{3.2}
\]

Then \(|A|=|B|=H\) and \(|A\cap B|=H-d\). If \(1\le d<H\), the number
of injective tails in which both \(A\) and \(B\) occur as \(H\)-windows
is

\[
 \boxed{
 T_d=2(L-d)(d!)^2(H-d)!\frac{(n-d)!}{H!}.}
\tag{3.3}
\]

If \(d=H\), the number is

\[
 \boxed{
 T_H=(L-H)(L-H+1)H!(L-1)!.}
\tag{3.4}
\]

#### Proof

Suppose first that \(d<H\). Two length-\(H\) intervals in an injective
word have intersection size \(H-d\) exactly when their starts differ by
\(d\). There are two orientations and \(L-d\) placements. The positions
belonging only to \(A\), to \(A\cap B\), and only to \(B\) may be filled
in

\[
 d!(H-d)!d!
\tag{3.5}
\]

ways. The remaining \(n-H-d\) positions are filled from the
\(n-d\) letters outside \(A\cup B\), giving

\[
 (n-d)_{n-H-d}=\frac{(n-d)!}{H!}.
\tag{3.6}
\]

This proves (3.3). Notice that the denominator \(H!\) is forced by the
exactly \(H\) unused letters; omitting it is a genuine counting error.

When \(d=H\), the two prescribed windows are disjoint. Their starts may
have any separation \(g\ge H\). The number of ordered labelled start
pairs is

\[
 2\sum_{g=H}^{L-1}(L-g)=(L-H)(L-H+1).
\tag{3.7}
\]

The two blocks contribute \((H!)^2\), and the unfilled positions
contribute \((L-1)!/H!\). This gives (3.4). \(\square\)

## 4. Exact middle--middle and rooted triple codegrees

### Theorem 4.1 (complete pair sequence)

For distinct middle owners at Johnson distance \(d\), the codegree is
zero when \(d>H\). For \(1\le d<H\),

\[
 \boxed{
 \kappa_d
 =\frac{2(L-d)(m-d)!^2(d!)^2}{(2H)!H!s!}.}
\tag{4.1}
\]

At the disjoint-window endpoint,

\[
 \boxed{
 \kappa_H
 =\frac{(L-H)(L-H+1)s!H!}{(2H)!}.}
\tag{4.2}
\]

Equivalently,

\[
 \boxed{
 \frac{\kappa_d}{D_X}
 =\frac{2(L-d)}{L\binom md^2}
 \quad(1\le d<H),}
\tag{4.3}
\]

and

\[
 \boxed{
 \frac{\kappa_H}{D_X}
 =\frac{(L-H)(L-H+1)}{L\binom mH^2}.}
\tag{4.4}
\]

#### Proof

A common root exists exactly when \(d\le H\). For such a pair the number
of common roots is

\[
 \binom{m-d}{H-d},
\tag{4.5}
\]

and, after fixing the root, the core must lie in \(X\cap Y\), giving

\[
 \binom{m-d}{2H}
\tag{4.6}
\]

choices. Multiply (4.5), (4.6), and Lemma 3.1. For \(d<H\), cancellation
gives (4.1); for \(d=H\), it gives (4.2). Dividing by (2.2) proves
(4.3)--(4.4). \(\square\)

### Corollary 4.2 (rooted triple sequence)

Fix \(U\supset X\cup Y\). For \(1\le d<H\),

\[
 d(U,X,Y)
 =\frac{2(L-d)(m-d)!(d!)^2(H-d)!}{(2H)!H!},
\tag{4.7}
\]

and hence

\[
 \boxed{
 \frac{d(U,X,Y)}{d(U,X)}
 =\frac{2(1-d/L)}{\binom md\binom Hd}.}
\tag{4.8}
\]

For \(d=H\), the root is necessarily \(U=X\cup Y\), and

\[
 d(U,X,Y)=\kappa_H,
 \qquad
 \frac{d(U,X,Y)}{d(U,X)}
 =\frac{(L-H)(L-H+1)}{L\binom mH}.
\tag{4.9}
\]

#### Proof

Delete the common-root factor (4.5) from the proof of Theorem 4.1 and
divide by (2.7). \(\square\)

### Corollary 4.3 (Johnson-shell audit identity)

A fixed \(X\) has \(\binom md^2\) middle owners at Johnson distance
\(d\). Conditional on a uniformly random option incident with \(X\), the
total expected number of its other owners in shell \(d\) is

\[
 \alpha_d=
 \begin{cases}
 \displaystyle \frac{2(L-d)}L,&1\le d<H,\\[1ex]
 \displaystyle \frac{(L-H)(L-H+1)}L,&d=H.
 \end{cases}
\tag{4.10}
\]

Exactly

\[
 \sum_{d=1}^H\alpha_d=L-1,
\tag{4.11}
\]

as required. Moreover,

\[
 \sum_{d=1}^H d\alpha_d
 =H(L-H)+\frac{H^3-H}{3L}.
\tag{4.12}
\]

Thus the small maximum codegree is compatible with a coherent total row
mass \(L-1\); it must not be interpreted as an expansion theorem.

### Corollary 4.4 (the exact maximum pair codegree)

For all sufficiently large \(m\) under the calibrated hypothesis (0.4),

\[
 \boxed{
 \Delta_2=\kappa_1,qquad
 \frac{\Delta_2}{D_X}=\frac{2(L-1)}{Lm^2},qquad
 \frac{\Delta_2}{D_U}=\frac{2(L-1)}{\Lambda m^2}.}
\tag{4.13}
\]

#### Proof

For \(1\le d<H-1\), put \(r_d=\kappa_d/D_X\). Then

\[
 \frac{r_{d+1}}{r_d}
 =\frac{L-d-1}{L-d}
  \left(\frac{d+1}{m-d}\right)^2<1.
\tag{4.14}
\]

The endpoint (4.4) can exceed \(r_{H-1}\), but it is still smaller than
\(r_1\): since \(H\ge2\) and \(H<m/2\),
\(\binom mH\ge\binom m2\), and (4.4) is \(O(m^{-3})\), whereas
\(r_1=(2+o(1))m^{-2}\). The root--middle ratio relative to \(D_X\) is
\(1/\binom mH=m^{-\omega(1)}\) under (0.4), so it is also smaller.
Distinct roots have zero codegree.
Equations (2.3) and (4.3) give the last formula. \(\square\)

At the calibrated height, both \(1/\binom mH\) and (4.4) are
superpolynomially smaller than \(m^{-2}\). More precisely,

\[
 \log\frac{\kappa_H}{D_X}
 =-2H\log(m/H)-2H+O(H^2/m+\log m).
\tag{4.15}
\]

## 5. Decorated versus simple physical paths

The preceding object is naturally a multihypergraph because different
decorations can have the same root and unordered owner family. The
multiplicity is uniform.

### Theorem 5.1 (exact projection multiplicity)

Every simple rooted path edge has exactly

\[
 \boxed{\mu_{\rm red}=2\binom{3H}{2H}}
\tag{5.1}
\]

preimages in the decorated catalogue (1.2). Therefore every degree and
codegree in Sections 2--4 is divided by the same factor (5.1) on passing
to the simple hypergraph, and every normalized formula is unchanged.

Here "simple edge" means the usual unordered hyperedge, so reversal of
the tail is identified. If the directed order of the physical path is
retained as part of the projected object, the reversal is not identified
and the corresponding multiplicity is only \(\binom{3H}{2H}\).

If one additionally orders the \(2H\) core letters and the \(H\) unused
noncore letters, every reduced option has \((2H)!H!\) full-order lifts.
The full-order catalogue has \(M!\) options per root, and its exact
unordered-simple-edge multiplicity is

\[
 \boxed{\mu_{\rm full}=2(3H)!.}
\tag{5.2}
\]

For an oriented physical path, the full-order multiplicity is instead
\((3H)!\).

#### Proof

From the owner family and its root \(U\), recover the deletion windows
\(B_i=U\setminus X_i\). Two of these windows have Johnson distance one
if and only if their starts are consecutive. Hence their distance-one
graph is a path, which recovers the window order up to reversal. The
successive one-letter differences recover the whole tail word. Here
\(L-1>H\), by \(m>4H\), so there is no unidentified interior segment.

The tail uses \(n=M-3H\) coordinates. Exactly \(3H\) coordinates of
\(U\) are absent from it, and any \(2H\)-subset of those coordinates may
be the core. Reversal supplies the factor two, proving (5.1). Restoring
the two hidden internal orders multiplies (5.1) by \((2H)!H!\), which is
\(2(3H)!\). \(\square\)

Thus \((3H)!\) is the directed-path multiplicity, while \(2(3H)!\) is
the unordered-hyperedge multiplicity. Uniformity makes this convention
harmless for all normalized codegrees and for uniform random-option laws,
but the factor two must be retained when raw simple-hypergraph degrees
are quoted.

## 6. Sharp external link influence

For a vertex \(v\notin e\), define

\[
 a_v(e)=|\{f:v\in f,\ f\cap e\ne\varnothing\}|.
\tag{6.1}
\]

This is the static external-link quantity used by a one-step
random-priority/RPRN audit.

### Lemma 6.1 (linear-path Johnson spheres)

Let \(E=\{X_1,\ldots,X_L\}\) be the middle path of one option. For any
middle owner \(X\) and any integer \(1\le d<H/2\),

\[
 |\{i:d_J(X,X_i)=d\}|\le2d+1.
\tag{6.2}
\]

For \(d=1\), the upper bound three is attainable with \(X\notin E\).

#### Proof

If \(X_i,X_j\) both have distance \(d\) from \(X\), then the triangle
inequality gives \(d_J(X_i,X_j)\le2d\). Along the tail path,

\[
 d_J(X_i,X_j)=\min\{|i-j|,H\}.
\tag{6.3}
\]

Because \(2d<H\), all qualifying indices have diameter at most \(2d\),
which proves (6.2).

For sharpness at \(d=1\), use three consecutive windows starting at
positions \(0,1,2\). Let \(A\) consist of the common \(H-2\) coordinates
in positions \(2,\ldots,H-1\), together with the coordinates in positions
\(0\) and \(H\). Then \(X=U\setminus A\) is distinct from all path
owners, but each of the three displayed windows differs from \(A\) in
one coordinate. \(\square\)

### Theorem 6.2 (asymptotically sharp middle-link influence)

Under (0.4), uniformly over all options \(e\) and all middle owners
\(X\notin e\),

\[
 \frac{a_X(e)}{D_X}
 \le \frac{6(L-1)}{Lm^2}+O(m^{-4}).
\tag{6.4}
\]

Conversely, there are \(X,e\) for which

\[
 \frac{a_X(e)}{D_X}
 \ge \frac{6(L-1)}{Lm^2}-O(m^{-4}).
\tag{6.5}
\]

Hence (0.5) holds.

#### Proof

Let the root of \(e\) be \(U\), and let \(E\) be its middle path. By a
union bound over the vertices of \(e\),

\[
 a_X(e)
 \le \mathbf1_{X\subset U}d(U,X)
      +\sum_{Y\in E}\kappa_{d_J(X,Y)}.
\tag{6.6}
\]

The root term divided by \(D_X\) is at most \(1/\binom mH\). Lemma 6.1
and (4.3) give a distance-one contribution at most

\[
 3\frac{2(L-1)}{Lm^2}.
\tag{6.7}
\]

The shells \(2\le d<H/2\) contribute \(O(m^{-4})\): use (6.2), (4.3),
and the successive ratio in (4.14). For \(d\ge H/2\), the crude bound
of \(L\) path vertices times the largest remaining value in
(4.3)--(4.4) is superpolynomially small at (0.4). The root term is also
superpolynomially small. This proves (6.4).

For the construction in Lemma 6.1, call the three distance-one path
owners \(Y_0,Y_1,Y_2\). No option can contain \(X,Y_0,Y_1\), because
their three pairwise distances are all one, whereas the distance-one
graph of distinct windows is a path. The same applies to
\(X,Y_1,Y_2\). The only possible overlap between the three pair links is
bounded by \(\kappa_2=O(D_Xm^{-4})\), because
\(d_J(Y_0,Y_2)=2\). Inclusion--exclusion therefore gives

\[
 a_X(e)\ge3\kappa_1-\kappa_2,
\tag{6.8}
\]

which proves (6.5). \(\square\)

### Theorem 6.3 (external root influence)

Let \(e\) be rooted at \(U\), and let \(V\ne U\) be another root. Then

\[
 \boxed{
 \frac{a_V(e)}{D_U}\le\frac{HL}{\binom MH}.}
\tag{6.9}
\]

At (0.4), this is superpolynomially smaller than \(m^{-2}\). Thus the
maximum external vertex influence is the middle value in Theorem 6.2.

#### Proof

Put \(A=U\setminus V\), which is nonempty. A path owner
\(X_i=U\setminus B_i\) lies in \(V\) exactly when \(A\subset B_i\).
If the coordinates of \(A\) do not all occur in the tail, there are no
such owners. Otherwise, a length-\(H\) interval containing a fixed
nonempty set of positions has at most \(H\) possible starts. Hence at
most \(H\) owners of \(e\) lie below \(V\). Apply the union bound and
(2.8). \(\square\)

## 7. Whole-edge influence and one random-priority wave

The local bound (0.5) is the relevant variance input, but it is also
useful to compute the total number of other root proposals seen by one
fixed path.

Fix an option \(e\) rooted at \(U\). Every other root \(V\) chooses a
uniform option independently. Let \(p_V\) be the probability that this
option meets the middle path of \(e\), and put

\[
 T_e=\sum_{V\ne U}p_V.
\tag{7.1}
\]

### Theorem 7.1 (uniform total external proposal mass)

Define

\[
 F=L^2\left(\frac1\Lambda-\frac1{\binom MH}\right).
\tag{7.2}
\]

Then

\[
 F-S\le T_e\le F,
\tag{7.3}
\]

where

\[
 S=\frac2\Lambda\sum_{d=1}^{H-1}
       \frac{(L-d)^2}{\binom md^2}
   +\frac{((L-H)(L-H+1))^2}
          {2\Lambda\binom mH^2}.
\tag{7.4}
\]

At (0.4), uniformly in \(e\),

\[
 S=\frac{2+o(1)}m,
 \qquad
 T_e=\frac{L^2}{\Lambda}+O(1/m)=(1+o(1))m.
\tag{7.5}
\]

#### Proof

For one middle owner \(X\in e\), there are \(\binom mH-1\) other roots
above it, and a uniform option at each such root contains it with
probability \(L/\binom MH\). Summing this first incidence mass over the
\(L\) owners gives (7.2), because

\[
 \frac{\binom mH}{\binom MH}=\frac1\Lambda.
\tag{7.6}
\]

The union bound gives \(T_e\le F\). Bonferroni subtracts at most the sum
of pair-occurrence probabilities. The path has \(L-d\) unordered pairs
at distance \(d<H\), and \((L-H)(L-H+1)/2\) unordered pairs at distance
\(H\). Divide (4.1)--(4.2) by \(D_U\) and sum these pair contributions;
this is exactly (7.4). Its \(d=1\) term is
\(2(L-1)^2/(\Lambda m^2)=(2+o(1))/m\); all remaining terms are smaller
by \(o(1/m)\). This proves (7.5). \(\square\)

There is also an exact top-distance first-moment decomposition. If
\(d_J(U,V)=t\), then two independent uniform options rooted at \(U,V\)
satisfy

\[
 \mathbb E|E_U\cap E_V|
 =\mathbf1_{t\le H}\binom{M-t}{H-t}
       \left(\frac L{\binom MH}\right)^2
 =\mathbf1_{t\le H}\frac{L^2}{\binom MH}
       \frac{(H)_t}{(M)_t}.
\tag{7.7}
\]

Summing over the \(\binom Mt\binom st\) roots at distance \(t\) recovers
(7.2) by Vandermonde.

### Corollary 7.2 (one random-priority wave)

Let every root propose an independent uniform option and attach an
independent uniform priority in \([0,1]\). Accept a proposal precisely
when it has strictly smaller priority than every intersecting proposal.
Then, uniformly in the proposed option \(e\),

\[
 \Pr(e\text{ is accepted}\mid e\text{ is proposed})
 =(1+o(1))\frac{1-e^{-T_e}}{T_e}
 =(1+o(1))\frac{\Lambda}{L^2}
 =(1+o(1))\frac1m.
\tag{7.8}
\]

Consequently one wave produces an integral owner-disjoint family of
literal common-core paths of expected size

\[
 (1+o(1))\frac{N_H}{m},
\tag{7.9}
\]

covering \((1+o(1))W/m\) middle owners.

#### Proof

Conditional on the priority \(y\) of \(e\), independence across the
other roots gives

\[
 \Pr(e\text{ accepted}\mid y,e)
 =\prod_{V\ne U}(1-yp_V).
\tag{7.10}
\]

Theorem 6.3 gives

\[
 \max_Vp_V\le\frac{HL}{\binom MH},
\tag{7.11}
\]

and hence

\[
 \sum_Vp_V^2\le(\max_Vp_V)T_e=o(1).
\tag{7.12}
\]

Uniformly for \(0\le y\le1\), the product in (7.10) is therefore
\(\exp(-yT_e+o(1))\). Integrating in \(y\) proves (7.8). Multiply by
the \(N_H\) roots to obtain (7.9), and then by \(L\) for the owner count.
\(\square\)

## 8. RPRN interpretation and exact boundary

The calculations prove all of the following for the initial common-core
catalogue.

1. The root and middle degrees are asymptotically equal.
2. The exact maximum normalized pair codegree is
   \((2+o(1))/m^2\).
3. Although \(L^2\Delta_2/D_X\to2\), the actual maximum external link
   influence is only \((6+o(1))/m^2\), because a linear tight path has at
   most three distance-one vertices around an external middle owner.
4. A one-wave random-priority packing is rigorous and uniform.

The usual link-variance calculation now has the correct scale. For
example, if decorated options are independently marked with probability

\[
 p=\frac{\gamma}{LD_U},
\tag{8.1}
\]

then Theorem 6.2 and the double count

\[
 \sum_e a_X(e)\le D_X(D_U+LD_X)
\tag{8.2}
\]

give

\[
 \operatorname{Var}\!\left(\sum_{e\not\ni X}a_X(e)\xi_e\right)
 \le\frac{(6+o(1))\gamma}{m^2}D_X^2.
\tag{8.3}
\]

Thus a Bernstein bound has exponent of order \(m^2\) in the first bite.

What is **not** proved is that (0.5), degree regularity, or the
linear-path sphere distribution returns after conditioning on many prior
accepted options. A near-perfect factor requires \(\Theta(L)\) dependent
waves, while residual menus can concentrate on exceptional path
segments. Nor does the middle projection enforce common phase tags or
simultaneous lower and upper mask disjointness. Therefore this report
closes the requested static degree/codegree and one-wave influence audit,
but leaves the positive physical fusion/RPRN regeneration gate open.
