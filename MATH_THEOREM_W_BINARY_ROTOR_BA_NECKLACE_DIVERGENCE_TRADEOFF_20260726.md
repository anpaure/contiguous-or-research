# Binary-rotor \(BA\)-necklace rounding: exact divergence--boundary tradeoff

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external source is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom n m,\qquad
 H=\lceil \mathsf A\sqrt m\rceil,
\]

where the Gaussian cutoff constant \(\mathsf A>0\) is fixed.
Throughout, \(m\) is sufficiently large that \(H\le m-1\).

The exact half-\(A\), half-\(B\) uniform rotor point has one unit in every
owner fibre, perfectly uniform lower loads, zero upper--lower signed
divergence at every depth, and \(A\)-mass \(W/2\). For a singleton
long-cycle rethreading with \(o(W/m)\) components, the global
adjacent-swap inequality forces every integral output to have

\[
                         a\ge(1/2-o(1))W.
\]

Thus, among integral singleton rethreadings with this opening scale, the
fractional switch density is asymptotically sharp. The problem is
correlated rounding, not switch sparsification.

The most economical exact cancellation columns are protected nested-star
atoms. Let \(S\) be their set of \(A\)-source states and put

\[
 \Gamma=BA,\qquad
 \delta_\Gamma(S)
 ={1\over2}\left\|\mathbf1_S-\mathbf1_{\Gamma^{-1}S}\right\|_1.
\]

The quantity \(\delta_\Gamma(S)\) is the number of one-runs in the binary
necklaces cut out by \(S\) on the \(\Gamma\)-orbits. If the atom family is
owner-disjoint and covers \(G\) owners, then \(G=2|S|\).

The central new invariant is

\[
 \boxed{
 {1\over2}\|D_m(S)\|_1
 +(m+1)\delta_\Gamma(S)\ge |S|
 \qquad(m\ {\rm odd}),}
 \tag{0.1}
\]

where \(D_m(S)\) is the rank-\(m\) signed divergence of the switches in
\(S\). For even \(m\), owner disjointness alone gives

\[
 \boxed{\delta_\Gamma(S)\ge {|S|\over m+1}.}
 \tag{0.2}
\]

Every complete nested-star atom has \(D_q=0\) at every protected depth.
Consequently, for both parities,

\[
 \boxed{
 \delta_\Gamma(S)\ge {|S|\over m+1}
 ={G\over2(m+1)}.}
 \tag{0.3}
\]

Therefore:

1. no nonempty integral owner-disjoint nested-star family has exact
   \(BA\)-flow;
2. no correlated law can cover \(W-o(W)\) owners with cancelling atoms
   while having expected \(BA\)-boundary \(o(W/m)\); and
3. this obstruction stops at the sharp scale, because a boundary
   \(O(W/m)\) has crude Gaussian connector divergence
   \(O(HW/m)=O_{\mathsf A}(W/\sqrt m)=o(W)\).

There is an exact necklace completion normal form after prescribing the
maximal \(BA\)-runs. Keeping precisely the selected states
\(S\mathbin{\dot\cup}AS\), those prescribed runs close to a legal rotor
cycle cover if and only if

\[
                         \boxed{A^2T=R,}
 \tag{0.4}
\]

where \(T\) and \(R\) are their terminal and initial phases. It uses
exactly \(\delta_\Gamma(S)\) connector \(A\)-switches.

The natural translation-invariant construction at the critical scale is
also impossible. Partition the sources into \(BA\)-interval packets of
length \(m+1\) and put the forced \(A^2\)-connector at every packet end.
The induced start map is

\[
                         G=A^2\Gamma^m.
\]

For even \(m\), consecutive \(G\)-blocks repeat a source/successor owner.
For odd \(m\), the \(m\)-th \(G\)-block repeats the initial source owner.
Hence the single-length \(m+1\) necklace LP has a zero-leave uniform
fractional point but no nonzero integral owner-simple point.

What remains is sharply identified: a fixed or variable packet-length
law not concentrated at \(m+1\), or an exterior-moving connector which
changes the selected state set, must round the uniform point with
boundary \(\Theta(W/m)\), join the packets into \(o(W/m)\) cycles, and
make the lower floor-corrected factorial excess \(o(W)\). No such
rounding is proved here.

## 1. Exact signed-divergence rotor program

Let \(\mathcal E\) be the injective ordered \((n-1)\)-words. For

\[
 e=(x_1,\ldots,x_{n-1}),
\]

write \(x_n\) for its missing coordinate and identify \(e\) with the
permutation state \((x_1,\ldots,x_n)\). The two rotor maps are

\[
 A(x_1,\ldots,x_n)
  =(x_2,\ldots,x_{n-1},x_1,x_n),
\]

\[
 B(x_1,\ldots,x_n)
  =(x_2,\ldots,x_n,x_1).
\]

Their induced successors in \(\mathcal E\) are denoted \(S_Ae,S_Be\).
Put

\[
                         \kappa(e)=\{x_1,\ldots,x_m\}.
\]

With \(z_{e,A},z_{e,B}\ge0\) and \(y_e=z_{e,A}+z_{e,B}\), the exact owner
and state-flow equations are

\[
 \sum_{e:\kappa(e)=X}y_e=1
 \qquad\left(X\in\binom{[n]}m\right),
 \tag{1.1}
\]

\[
 y_f=\sum_{e,g:S_ge=f}z_{e,g}
 \qquad(f\in\mathcal E).
 \tag{1.2}
\]

For \(0\le q\le H\), put \(r_q=m-q\),

\[
 p_q(e)=\{x_1,\ldots,x_{r_q}\},
\qquad
 K_q(e)=\{x_{n-r_q+1},\ldots,x_{n-1}\}.
\]

The lower and complementary upper loads are

\[
 L_q(T)=\sum_{e:p_q(e)=T}y_e,
 \tag{1.3}
\]

and

\[
 R_q(T)=\sum_e y_e\,
 \mathbf1_{\{T=K_q(e)\cup\{x_n\}\}}.
\]

The signed upper--lower divergence is

\[
 D_q(T)=\sum_ez_{e,A}
 \left(
 \mathbf1_{T=K_q(e)\cup\{x_n\}}
 -\mathbf1_{T=K_q(e)\cup\{x_1\}}
 \right).
 \tag{1.4}
\]

State flow gives the exact targetwise identity

\[
                         R_q-L_q=D_q.
 \tag{1.5}
\]

An integral solution of (1.1)--(1.2) is an owner-transversal clustered
de Bruijn cycle cover, hence a literal singleton rethreading.

Put

\[
 N_q=\binom n{m-q},\qquad
 c_q=\left\lfloor{W\over N_q}\right\rfloor,
\]

and define the lower balanced factorial excess

\[
 \Delta_q^-
 =\sum_{T\in\binom{[n]}{m-q}}
 { (L_q(T)-c_q)(L_q(T)-c_q-1)\over2}.
 \tag{1.6}
\]

For integral loads every summand is nonnegative, and a hole costs
\(c_q(c_q+1)/2\). Also put

\[
 \mathfrak D_H={1\over2}\sum_{q=0}^{H}\|D_q\|_1.
 \tag{1.7}
\]

### Theorem 1.1 (integral wholesale sufficient criterion)

If an integral rotor factor has \(C_{\mathrm{out}}\) cycles and

\[
 (m+H)C_{\mathrm{out}}=o(W),
 \tag{1.8}
\]

\[
 \sum_{q=0}^{H}{\Delta_q^-\over c_q}=o(W),
 \qquad
 \mathfrak D_H=o(W),
 \tag{1.9}
\]

then it gives a literal word of length \(W+o(W)\) covering every paired
rank through depth \(H\).

#### Proof

Opening the singleton cycles costs \((m+H)C_{\mathrm{out}}=o(W)\). By
(1.6), the aggregate number of lower holes is at most

\[
 \sum_q{2\Delta_q^-\over c_q(c_q+1)}=o(W).
\]

At each depth, (1.5) implies that the number of upper holes is at most
the number of lower holes plus \(\|D_q\|_1/2\). Append every remaining
lower and upper target as one literal nonempty mask. Equations
(1.8)--(1.9) make the appended length \(o(W)\). \(\square\)

There are

\[
                         D_0=m!(m+1)!
\]

states in every owner fibre. For every \(0\le t\le1\),

\[
 z^t_{e,A}={t\over D_0},\qquad
 z^t_{e,B}={1-t\over D_0}
 \tag{1.10}
\]

satisfies (1.1)--(1.5), with

\[
 L_q(T)=R_q(T)=\lambda_q:={W\over N_q}.
 \tag{1.11}
\]

At \(t=1/2\), the total \(A\)-mass is \(W/2\). Thus (1.10) is the exact
fractional centre of the signed system.

There is an exact probabilistic formulation of the missing rounding
theorem. Write

\[
 \lambda_q=c_q+\vartheta_q,\qquad0\le\vartheta_q<1.
\]

If a law on integral rotor factors has
\(\mathbb E L_q(T)=\lambda_q\) for every \(q,T\), then

\[
 \boxed{
 \mathbb E\Delta_q^-
 ={1\over2}\sum_T
 \left(\operatorname {Var}L_q(T)
       -\vartheta_q(1-\vartheta_q)\right).}
 \tag{1.12}
\]

Indeed, (1.6) is quadratic, and the minimum variance of an
integer-valued variable of mean \(c_q+\vartheta_q\) is
\(\vartheta_q(1-\vartheta_q)\). A correlated rounding theorem would make
the weighted sum of the nonnegative remainders in (1.12), the expected
divergence (1.7), and the expected opening cost all \(o(W)\).

## 2. The adjacent-swap toll fixes the scalar switch density

Let \(a\) be the number of selected \(A\)-arcs, let
\(C_{\mathrm{out}}\) be the number of support cycles, and let \(c_1\) be
the number of non-pure cycles. Consecutive maximal \(B\)-runs are
supported on wreaths differing by one adjacent coordinate swap. Such a
swap introduces at most two new middle owners. Therefore

\[
 \boxed{W\le nC_{\mathrm{out}}+2a-2c_1.}
 \tag{2.1}
\]

In the singleton long-cycle regime (1.8),

\[
                         C_{\mathrm{out}}=o(W/m),
\]

and (2.1) gives

\[
                         a\ge(1/2-o(1))W.
 \tag{2.2}
\]

Thus (1.10) cannot be rounded by making \(A\)-switches rare: among
integral outputs satisfying \(C_{\mathrm{out}}=o(W/m)\), the
half--half point already has the asymptotically least possible
\(A\)-mass. This is neither a claim about other fractional faces nor a
claim in the weaker typed-opening regime.

The quantifier in (2.2) is essential. The weaker typed-erosion condition
\(C_{\mathrm{out}}=o(W/H)\) does not imply a linear switch toll. The
ordinary \(W/n\)-component wreath factor has no \(A\)-switches and
satisfies that weaker condition at Gaussian \(H\). Everything below
concerns the singleton wholesale rethreading (1.8).

## 3. Nested-star sources and their \(BA\)-necklaces

Every protected nested-star atom consists of three \(A\)-source states,
has six distinct source/successor middle owners, and has zero signed
divergence (1.4) at every protected depth. Let an owner-disjoint family
of such atoms have source set \(S\), and define

\[
                         X(e)=\kappa(e),\qquad Y(e)=\kappa(Ae).
\]

All owners in

\[
 \{X(e):e\in S\}\mathbin{\dot\cup}\{Y(e):e\in S\}
\]

are distinct. Hence, if \(G\) is the covered owner count,

\[
                         G=2|S|.
 \tag{3.1}
\]

Put \(\Gamma=BA\). Its pullback permutation on positions is

\[
 \gamma=(1,3,5,\ldots,2m-1)
        (2,4,6,\ldots,2m,2m+1),
 \tag{3.2}
\]

with cycle lengths \(m,m+1\). Define the necklace boundary

\[
 \delta_\Gamma(S)
 ={1\over2}|S\triangle\Gamma^{-1}S|.
 \tag{3.3}
\]

On every cyclic \(\Gamma\)-orbit, (3.3) is the number of one-runs of
\(\mathbf1_S\).

At rank \(m\), use the footprints

\[
 P_+=\{m+2,\ldots,2m+1\},\qquad
 P_-=\{1,m+2,\ldots,2m\},
\]

and define

\[
 D_m(S)=\sum_{e\in S}
 \left(\mathbf e_{e(P_+)}-\mathbf e_{e(P_-)}\right).
 \tag{3.4}
\]

This is the depth-zero instance of (1.4) restricted to the
\(A\)-sources in \(S\).

### Theorem 3.1 (odd-\(m\) divergence--necklace inequality)

Suppose \(m=2r+1\), and put \(s=r+1=(m+1)/2\). For every source set \(S\)
whose \(X\)- and \(Y\)-owners are all distinct,

\[
 \boxed{
 {1\over2}\|D_m(S)\|_1
 +(m+1)\delta_\Gamma(S)\ge|S|.}
 \tag{3.5}
\]

#### Proof

Besides \(P_+,P_-\), put

\[
 P_0=\{1,\ldots,m\},\qquad P_1=\{2,\ldots,m+1\}.
\]

The source and successor owners read \(P_0,P_1\). On the odd position
cycle in (3.2), \(P_+\) is the translate of \(P_1\) by \(r\); on the
even-plus-last cycle it is the translate by \(r+1\). The Chinese
remainder theorem therefore gives

\[
                         P_+=\gamma^{-s}P_1.
\]

Similarly,

\[
                         P_-=\gamma^sP_0.
 \tag{3.6}
\]

With pushforward notation,

\[
 D_m(S)
 =Y_\#\mathbf1_{\Gamma^{-s}S}
  -X_\#\mathbf1_{\Gamma^sS}.
 \tag{3.7}
\]

Put

\[
                         V(S)=Y_\#\mathbf1_S-X_\#\mathbf1_S.
\]

Owner disjointness gives

\[
                         \|V(S)\|_1=2|S|.
 \tag{3.8}
\]

Pushforward by any map contracts \(\ell^1\). Telescoping around the
necklaces gives

\[
 |\Gamma^{\pm s}S\triangle S|
 \le s|\Gamma S\triangle S|
 =2s\delta_\Gamma(S).
 \tag{3.9}
\]

Thus

\[
 \|D_m(S)-V(S)\|_1\le4s\delta_\Gamma(S).
\]

The triangle inequality and \(2s=m+1\) prove (3.5). \(\square\)

### Theorem 3.2 (even-\(m\) necklace inequality)

If \(m\) is even and the \(X\)- and \(Y\)-owners of \(S\) are all
distinct, then

\[
                         \boxed{
 \delta_\Gamma(S)\ge{|S|\over m+1}.}
 \tag{3.10}
\]

#### Proof

The exact position identity for even \(m\) is

\[
                         Y(e)=X(\Gamma^{m+1}e).
 \tag{3.11}
\]

Owner disjointness therefore implies

\[
                         S\cap\Gamma^{m+1}S=\varnothing.
\]

On each cyclic \(\Gamma\)-orbit, no one-run has more than \(m+1\)
positions. The number of such runs is its contribution to
\(\delta_\Gamma(S)\). Summing run lengths proves (3.10). \(\square\)

### Corollary 3.3 (all-parity atom-flow obstruction)

For an owner-disjoint union of complete nested-star atoms,

\[
                         D_m(S)=0.
\]

Therefore Theorems 3.1--3.2 and (3.1) give, for every \(m\ge3\),

\[
 \boxed{
 \delta_\Gamma(S)\ge{|S|\over m+1}
 ={G\over2(m+1)}.}
 \tag{3.12}
\]

In particular, exact \(BA\)-flow \(S=\Gamma S\) forces
\(S=\varnothing\). For a random owner-disjoint atom packing, (3.12)
remains true after taking expectations. Hence

\[
 \mathbb EG=W-o(W)
 \quad\Longrightarrow\quad
 \mathbb E\delta_\Gamma(S)
 \ge(1/2-o(1)){W\over m}.
 \tag{3.13}
\]

No independence assumption occurs in this argument.

### Corollary 3.4 (correlated law-level boundary toll)

Let \(\boldsymbol S\) be any random source set such that, in every
realization, all \(X\)- and \(Y\)-owners are distinct, and put
\(\boldsymbol G=2|\boldsymbol S|\). If \(m\) is odd, then

\[
 \boxed{
 \mathbb E\delta_\Gamma(\boldsymbol S)
 \ge
 {\mathbb E\boldsymbol G-\mathbb E\|D_m(\boldsymbol S)\|_1
  \over2(m+1)}.}
 \tag{3.14}
\]

If \(m\) is even, then

\[
 \boxed{
 \mathbb E\delta_\Gamma(\boldsymbol S)
 \ge{\mathbb E\boldsymbol G\over2(m+1)}.}
 \tag{3.15}
\]

Consequently, in either parity, a law with
\(\mathbb E\boldsymbol G=W-o(W)\) and, when \(m\) is odd,
\(\mathbb E\|D_m(\boldsymbol S)\|_1=o(W)\), must satisfy

\[
 \mathbb E\delta_\Gamma(\boldsymbol S)
 \ge(1/2-o(1)){W\over m}.
 \tag{3.16}
\]

#### Proof

Take expectations in (3.5) or (3.10), and use
\(|\boldsymbol S|=\boldsymbol G/2\). \(\square\)

This corrects the exact implication scope of the earlier \(BA\)-orbit
notes. On odd \(m\), a full \(BA\)-orbit can be owner-simple, but its top
signed divergence has one fixed sign on its two owner shores. Atomwise
zero divergence and exact orbit flow cannot coexist.

## 4. Exact open-necklace completion

Let \(S\) be the source set of an owner-disjoint union of complete
nested-star atoms. Retain the selected state set

\[
                         E=S\mathbin{\dot\cup}AS.
 \tag{4.1}
\]

Prescribe \(s\to As\) by an \(A\)-transition for every \(s\in S\).
Whenever \(s,\Gamma s\in S\), prescribe the interior transition

\[
                         As\longrightarrow\Gamma s
\]

by \(B\). Define terminals and starts by

\[
 T=S\setminus\Gamma^{-1}S
   =\{s\in S:\Gamma s\notin S\},
\]

\[
 R=S\setminus\Gamma S
   =\{s\in S:\Gamma^{-1}s\notin S\}.
 \tag{4.2}
\]

Then

\[
                         |T|=|R|=\delta_\Gamma(S).
 \tag{4.3}
\]

### Theorem 4.1 (forced endpoint closure)

Under the prescribed atom transitions and the prescribed \(B\)-edge at
every \(S\)-adjacency, \(E\) closes to a binary-rotor cycle cover without
adding states if and only if

\[
                         \boxed{A^2T=R.}
 \tag{4.4}
\]

It then uses exactly \(\delta_\Gamma(S)\) connector \(A\)-switches, and

\[
 \boxed{
 \mathfrak D_H^{\mathrm{conn}}
 \le(H+1)\delta_\Gamma(S).}
 \tag{4.5}
\]

The number of resulting rotor cycles is at most
\(\delta_\Gamma(S)\).

#### Proof

At \(As\) for a terminal \(s\in T\), the \(B\)-successor is
\(\Gamma s\notin S\). If \(\Gamma s\notin E\), that state is absent.
If \(\Gamma s\in AS\), it already has its prescribed incoming
atom-\(A\) edge, so the edge \(As\to\Gamma s\) would give it indegree
two. Thus the \(B\)-successor is unavailable in either case. The only
other rotor successor is \(A^2s\).
It cannot belong to \(AS\), because that would put \(As\) in \(S\),
contrary to (4.1). Hence it must be a source state. It must be a run
start; otherwise it already has the prescribed incoming \(B\)-edge from
the preceding interior phase. Thus closure implies
\(A^2T\subseteq R\), and (4.3) plus injectivity of \(A^2\) gives
equality.

Conversely, (4.4) gives every terminal successor one connector edge and
gives every start its missing incoming edge. All interior states already
have one incoming and one outgoing edge, so the selected graph is a
disjoint union of directed cycles.

The atom \(A\)-switches cancel at every depth. Each connector switch
contributes a signed Johnson edge of half-\(\ell^1\) norm one at each
protected depth, proving (4.5).

It remains to justify the component bound in the presence of complete
\(\Gamma\)-orbits. Let \(f\) be the number of such orbits contained in
\(S\). Since every \(\Gamma\)-orbit has length \(m(m+1)\), Corollary
3.3 gives

\[
 f m(m+1)\le |S|\le(m+1)\delta_\Gamma(S),
 \qquad f\le{\delta_\Gamma(S)\over m}.
\]

Every cycle assembled from open runs uses at least two runs. Indeed, a
one-run cycle of length \(1\le b<m(m+1)\) would fix an injective state
under \(A^2\Gamma^{b-1}\), forcing the pullback identity
\(\gamma^{b-1}a^2=1\). Since \(a^{-2}\) fixes position \(n\), this
would force \(m+1\mid b-1\), so \(\gamma^{b-1}\) fixes the entire
even-plus-\(n\) position cycle, whereas \(a^{-2}\) does not fix position
2, a contradiction. Hence the open-run cycles number at most
\(\delta_\Gamma(S)/2\), while each full orbit contributes one cycle.
For \(m\ge3\),

\[
 C_{\mathrm{out}}
 \le {\delta_\Gamma(S)\over2}+f
 \le {\delta_\Gamma(S)\over2}
     +{\delta_\Gamma(S)\over m}
 \le\delta_\Gamma(S).
\]

This proves the component bound. \(\square\)

If a construction attains the forced critical scale
\(\delta_\Gamma(S)=O(W/m)\), then (4.5) is only

\[
 O\left(H{W\over m}\right)
 =O_{\mathsf A}(W/\sqrt m)=o(W).
 \tag{4.6}
\]

Thus the signed-divergence ledger permits the critical-scale escape.
Owner-safe closure and lower-profile rounding are the remaining issues.

## 5. The critical equal-packet law has no integral lift

Suppose the selected sources are partitioned into state-disjoint directed
\(\Gamma\)-interval packets of common length

\[
                         b=m+1.
 \tag{5.1}
\]

At every packet end use the \(A^2\)-connector. The packets need not be
maximal as subsets of \(S\). If \(\pi\) is one packet start, its terminal
is \(\Gamma^m\pi\), and endpoint flow forces the next start to be

\[
                         G\pi=A^2\Gamma^m\pi.
 \tag{5.2}
\]

Let

\[
                         a=(1\ 2\ \cdots\ 2m),
\]

fixing \(n\), be the pullback position permutation of \(A\), and let
\(\gamma\) be (3.2). The pullback of \(G\) is

\[
                         g=\gamma^ma^2.
 \tag{5.3}
\]

### Lemma 5.1 (exact action of the critical start map)

The map \(g\)

1. rotates the odd-position \(m\)-cycle in (3.2) forward by one;
2. fixes \(2,4,\ldots,2m-2\); and
3. swaps \(2m\) and \(n\).

#### Proof

The map \(a^2\) advances by two on positions \(1,\ldots,2m\).
The power \(\gamma^m\) is the identity on the odd \(m\)-cycle and is a
one-step backward rotation on the even-plus-last \((m+1)\)-cycle.
Their product has exactly the displayed action. \(\square\)

### Theorem 5.2 (single-length integer-hull obstruction)

No nonempty owner-transversal completion satisfying (5.1)--(5.2) exists,
for either parity of \(m\).

#### Proof

Let

\[
 P_0=\{1,\ldots,m\},\qquad P_1=\{2,\ldots,m+1\}.
\]

If \(m\) is even, Lemma 5.1 gives

\[
                         gP_0=P_1.
\]

Hence the source owner of the next start equals the successor owner of
the present start:

\[
                         X(G\pi)=Y(\pi),
\]

contradicting owner capacity.

If \(m\) is odd, \(g\) has order \(2m\), and \(g^m\) is the identity on
the odd cycle and the transposition \((2m\ n)\) on the other cycle.
The footprint \(P_0\) avoids both transposed positions, so

\[
                         g^mP_0=P_0.
\]

Every \(G\)-orbit of starts has length \(2m\); its initial and \(m\)-th
starts therefore have the same source owner:

\[
                         X(G^m\pi)=X(\pi).
\]

Again owner capacity fails. \(\square\)

Thus the natural \(b=m+1\) equal-packet law at the critical boundary
scale is fractionally feasible but integrally empty. A different fixed
length, a variable packet-length law, or a connector which leaves the
state set \(S\dot\cup AS\) remains possible.

## 6. Exact variable-run LP and Farkas dual

For a run packet

\[
 \rho=(\pi,b),\qquad1\le b<m(m+1),
\]

put

\[
 I_\rho=\{\pi,\Gamma\pi,\ldots,\Gamma^{b-1}\pi\},
 \qquad h_\rho=A^2\Gamma^{b-1}\pi.
 \tag{6.1}
\]

Let \(x_\alpha\) weight protected nested-star atoms, let \(y_\rho\)
weight run packets, and let \(r_X\) be owner leave. The exact fractional
necklace program with run budget \(K\) is

\[
 \begin{aligned}
 \min\quad&\sum_Xr_X\\
 \text{subject to}\quad
 &\sum_{\alpha:X\in\Omega(\alpha)}x_\alpha+r_X=1
       &&(X),\\
 &\sum_{\alpha:e\in I(\alpha)}x_\alpha
   =\sum_{\rho:e\in I_\rho}y_\rho
       &&(e),\\
 &\sum_{\rho:\pi_\rho=v}y_\rho
   =\sum_{\rho:h_\rho=v}y_\rho
       &&(v),\\
 &\sum_\rho y_\rho\le K,\\
 &x_\alpha,y_\rho,r_X\ge0.
 \end{aligned}
 \tag{6.2}
\]

At an integral point, owner capacity makes the selected run intervals
state-disjoint, the second row partitions the atom sources into packets,
and the third row closes the packet endpoints. This packetwise flow row
allows deliberate cuts at \(S\)-adjacencies and is therefore a genuine
generalization of the maximal-run condition (4.4).

### Theorem 6.1 (exact necklace Farkas dual)

The dual of (6.2) is

\[
 \begin{aligned}
 \max\quad&\sum_Xu_X-K\gamma\\
 \text{subject to}\quad
 &u_X\le1 &&(X),\\
 &\sum_{X\in\Omega(\alpha)}u_X
   +\sum_{e\in I(\alpha)}\phi_e\le0 &&(\alpha),\\
 &\sum_{e\in I_\rho}\phi_e
   +\psi_{h_\rho}-\psi_{\pi_\rho}+\gamma\ge0
       &&(\rho),\\
 &\gamma\ge0,
 \end{aligned}
 \tag{6.3}
\]

where \(u,\phi,\psi\) are free.

#### Proof

Give the owner, state-coupling, and endpoint-flow equalities the free
potentials \(u,\phi,\psi\), with signs chosen as in (6.3). Give the run
budget multiplier \(\gamma\ge0\). Nonnegativity of the coefficients of
\(r,x,y\) yields the three displayed dual inequalities; the constant
term is \(\sum_Xu_X-K\gamma\). Linear-programming duality proves the
statement. \(\square\)

The dual has no fractional obstruction at the critical scale. Let

\[
                         p={1\over2m!(m+1)!}.
\]

The exact uniform atom point gives source mass \(p\) at every state.
Choose constants \(\lambda_b\ge0\) with

\[
                         \sum_b b\lambda_b=p,
 \tag{6.4}
\]

and put \(y_{\pi,b}=\lambda_b\) for every start \(\pi\). Every state lies
in exactly \(b\) length-\(b\) packets, so the state-coupling row holds.
For each \(b\), the head map \(A^2\Gamma^{b-1}\) is a permutation, so
endpoint flow holds as well.

If

\[
 \bar b={\sum_b b\lambda_b\over\sum_b\lambda_b},
\]

then the total run mass is

\[
 \boxed{
 K^*=n!\sum_b\lambda_b={W\over2\bar b}.}
 \tag{6.5}
\]

This atom--run point is not the half--half point \(t=1/2\) of (1.10).
At every state, the uniform atom catalogue has source incidence \(p\)
and successor incidence \(p\), hence total selected mass
\(2p=1/[m!(m+1)!]\). The atom sources contribute \(A\)-mass \(p\);
uniform packet terminals contribute a further
\(\sum_b\lambda_b=p/\bar b\). Therefore the resulting full rotor point
is exactly (1.10) with

\[
 t={1+\bar b^{-1}\over2},\qquad
 1-t={1-\bar b^{-1}\over2},
\]

and its total \(A\)-mass is

\[
 a_{\mathrm{frac}}={W\over2}+K^*.
 \tag{6.6}
\]

Thus the \(W/m\)-scale connector toll appears explicitly while the
adjacent-swap lower bound is met asymptotically.

Taking \(\bar b\asymp m\) gives the critical scale
\(K^*=\Theta(W/m)\). Taking only \(b=m+1\) gives a zero-leave
fractional point with

\[
                         K^*={W\over2(m+1)},
 \tag{6.7}
\]

while Theorem 5.2 says that the corresponding integral face contains
only the zero atom selection. This is an integer-hull obstruction, not a
fractional Farkas cut. Finally, \(K^*\) controls the packet count, not
the number of cycles in the endpoint circulation and not any factorial
load row; both are separate integral requirements.

## 7. Proved and open boundary

Proved:

1. The uniform half--half rotor point is fractionally exact at every
   Gaussian depth and matches the asymptotic scalar \(A\)-mass lower
   bound in the singleton long-cycle regime.
2. Singleton long-cycle rounding cannot sparsify the \(A\)-switches; it
   must correlate \(\Theta(W)\) signed flags.
3. The odd divergence--necklace inequality (3.5) and the even collision
   inequality (3.10) force the all-parity boundary (3.12).
4. Exact \(BA\)-flow and every \(o(W/m)\)-boundary correlated atom law
   are impossible on a near-perfect owner packing.
5. Prescribed maximal open necklaces close on the same selected state
   set exactly under \(A^2T=R\), with Gaussian divergence toll (4.5).
6. The translation-invariant critical packet length \(m+1\) is
   integrally owner-impossible for both parities, despite exact
   fractional feasibility.
7. The variable-run primal (6.2) and dual (6.3) are exact, and their
   uniform point has \(A\)-mass \(W/2+K^*\).

Not proved:

1. an integral variable-run point of (6.2) with owner leave \(o(W)\),
   run count \(O(W/m)\), and \(o(W/m)\) final cycles;
2. the lower floor-corrected variance/factorial bound (1.9);
3. a critical-scale exterior-moving connector if (4.4) cannot be met; or
4. coefficient one.

The shortest surviving route is not full \(BA\)-orbit rounding and not
the \(b=m+1\) equal-packet necklace. It is correlated fixed-or-variable
packet rounding away from that forbidden length, at the forced \(W/m\)
boundary scale, followed by a nonlocal owner-safe connector and the
lower factorial-variance estimate.

## 8. Audit and implication scope

The footprint identities in Theorem 3.1, the endpoint closure in Theorem
4.1, and the owner repetitions in Theorem 5.2 were independently
rederived. The constants \(m+1\), \(W/[2(m+1)]\), and
\((H+1)\delta_\Gamma\) are exact.

The global adjacent-swap toll is invoked only under the singleton opening
condition \(C_{\mathrm{out}}=o(W/m)\). It is not imported into the weaker
typed-erosion setting. The no-go is architecture-specific: it closes
exact/full \(BA\)-flow, subcritical \(BA\)-boundary, and the single
critical packet length. It does not close arbitrary mixed \(A/B\) rotor
circulations, a different fixed packet length, variable packet lengths,
or connectors which introduce additional states.

The inputs audited and combined here are:

* MATH_THEOREM_BINARY_ROTOR_DEBRUIJN_DIVERGENCE_AND_MINIMAL_SKELETON_20260726.md;
* MATH_THEOREM_BINARY_ROTOR_GLOBAL_ADJACENT_SWAP_TOLL_20260726.md;
* MATH_THEOREM_NESTED_STAR_ATOM_OWNER_NIBBLE_AND_FLOW_GATE_20260726.md;
* MATH_THEOREM_PHASE_VARYING_BA_ORBIT_FLAG_FACTOR_20260726.md;
* MATH_THEOREM_BA_ORBIT_MATCHING_CIRCULATION_PARITY_AND_ANNULUS_NOGO_20260726.md; and
* MATH_THEOREM_CLUSTERED_BINARY_ROTOR_FARKAS_AND_CANCELLATION_INTEGER_HULL_OBSTRUCTION_20260726.md.
