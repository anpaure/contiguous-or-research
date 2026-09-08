# Canonical tensor-associator packets and their Hamming cycle factors

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome and exact scope

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\left\lfloor {m\over4}\right\rfloor.               \tag{0.1}
\]

Fix \(B\) labelled, pairwise disjoint eight-coordinate blocks among
\([n]\), leaving at most seven residual coordinates. In every block use
the same 24-state weight-four frame \(\mathcal V\) defined in Section 1.

Let

\[
 h=2^t\ge4,\qquad r={h\over2},\qquad
 1\le r\le B,\qquad r=o(m).                            \tag{0.2}
\]

There is a canonical partition of all middle sets having at least \(r\)
eligible blocks into packets isomorphic to \(\mathcal V^r\). The uncovered
fraction has the explicit bound

\[
 \boxed{
 {W-G\over W}
 \le 2(m+1)\exp\!\left(-{3B\over256}\right)}
                                                               \tag{0.3}
\]

whenever \(r\le3B/64\), where \(G\) is the number of covered middle sets.
In particular \(G=W-o(W)\).

Every packet has exactly \(24^r\) vertices. For every
\(\varepsilon\in\{0,1\}^r\), it has an exact decomposition into

\[
 6^r\quad\text{pairwise disjoint cells }Q_{2r}=Q_h.    \tag{0.4}
\]

Every cell has an explicit spanning \(2\)-factor into isometric
\(C_{2h}\)'s. Consequently every packet has an exact middle-vertex factor
containing

\[
 {24^r\over2h}                                         \tag{0.5}
\]

cycles, and all canonical packets together give a near-spanning
middle-vertex factor with

\[
 {G\over2h}                                            \tag{0.6}
\]

components.

The intended scale is available: one may choose \(h\) to be a power of
two with

\[
 \sqrt{m\log m}\ll h\ll m.                             \tag{0.7}
\]

Then (0.3) is exponentially small and

\[
 {G\over2h}
 =o\!\left({W\over\sqrt{m\log m}}\right).              \tag{0.8}
\]

This theorem proves exact middle ownership inside the retained packets.
It does **not** prove balanced shallow shadows, a literal exact wreath
factor, MWB, or coefficient one. In fact, Section 6 proves that the
uniform-order Hamming translate factor has only \(o(W)\) target support,
hence a \((1-o(1))W\) support deficit, at one logarithmic depth. The
surviving fine gate must use mixed direction orders within cells or must
fuse different cells.

## 1. The local 24-state frame

In one eight-block write the coordinates as

\[
 a,b,c,d,u,v,w,x.
\]

Let

\[
 \mathcal X=\binom{\{a,b,c,d\}}2,\qquad
 \mathcal Y=\{uw,ux,vw,vx\},                           \tag{1.1}
\]

and define

\[
 \boxed{\mathcal V=\{X\cup Y:X\in\mathcal X,\ Y\in\mathcal Y\}.}
                                                               \tag{1.2}
\]

Thus

\[
 |\mathcal V|=\binom42\,2^2=6\cdot4=24,                \tag{1.3}
\]

and every member has size four.

Use the following oriented squares:

\[
 \begin{aligned}
 Q_0&=(ac,bc,bd,ad),\\
 Q_1&=(ab,bc,cd,ad),\\
 Q_R&=(uw,vw,vx,ux).
 \end{aligned}                                         \tag{1.4}
\]

Every displayed square is a literal isometric \(Q_2\): its two directions
exchange endpoints in two disjoint coordinate pairs.

Define two six-cell decompositions of \(\mathcal V\):

\[
 \mathscr D_0=
 \{Q_0\cup Y:Y\in\mathcal Y\}
 \ \mathbin{\dot\cup}\
 \{ab\cup Q_R,\ cd\cup Q_R\},                          \tag{1.5}
\]

\[
 \mathscr D_1=
 \{Q_1\cup Y:Y\in\mathcal Y\}
 \ \mathbin{\dot\cup}\
 \{ac\cup Q_R,\ bd\cup Q_R\}.                          \tag{1.6}
\]

### Lemma 1.1 (the two local \(Q_2\)-resolutions)

Each of \(\mathscr D_0,\mathscr D_1\) is a partition of \(\mathcal V\)
into six physical isometric copies of \(Q_2\).

#### Proof

In (1.5), the four cells \(Q_0\cup Y\) cover the special two-sets

\[
 ac,bc,bd,ad
\]

at every reservoir state \(Y\). The last two cells cover \(ab\) and
\(cd\), respectively, at all four reservoir states. These six special
two-sets exhaust \(\mathcal X\), and no two listed cells share one.

In (1.6), the four cells \(Q_1\cup Y\) cover

\[
 ab,bc,cd,ad,
\]

while the last two cells cover \(ac\) and \(bd\). Again the six special
two-sets exhaust \(\mathcal X\) disjointly. Every cell has four vertices,
so both decompositions contain \(6\cdot4=24\) vertices, as required.
\(\square\)

The two resolutions have identical support \(\mathcal V\). Replacing one
by the other is therefore an exact integral middle-support associator.

## 2. Canonical first-\(r\)-eligible packets

Let the eight-blocks be

\[
 B_1,\ldots,B_B,
\]

each carrying a labelled copy \(\mathcal V_i\) of (1.2). Let \(R_0\) be
the residual coordinate set, so

\[
 [n]=R_0\mathbin{\dot\cup}B_1\mathbin{\dot\cup}\cdots
       \mathbin{\dot\cup}B_B,\qquad
 |R_0|=2(m\bmod4)+1\in\{1,3,5,7\}.                    \tag{2.1}
\]

For \(S\in\binom{[n]}m\), call \(i\) eligible when

\[
 S\cap B_i\in\mathcal V_i,                             \tag{2.2}
\]

and put

\[
 Z(S)=|\{i:S\cap B_i\in\mathcal V_i\}|.                \tag{2.3}
\]

Suppose \(Z(S)\ge r\), and let

\[
 I(S)=\{i_1(S)<\cdots<i_r(S)\}                         \tag{2.4}
\]

be its first \(r\) eligible block indices. Freeze the exterior

\[
 C(S)=S\cap\left([n]\setminus\bigcup_{i\in I(S)}B_i\right). \tag{2.5}
\]

Define

\[
 \mathcal P(S)=
 \left\{
 C(S)\cup\bigcup_{i\in I(S)}V_i:
 V_i\in\mathcal V_i\text{ for every }i\in I(S)
 \right\}.                                             \tag{2.6}
\]

Every set in (2.6) has size

\[
 |C(S)|+4r=(m-4r)+4r=m.                                \tag{2.7}
\]

### Theorem 2.1 (canonical packet partition)

The distinct sets \(\mathcal P(S)\), as \(S\) ranges over
\(\{S:Z(S)\ge r\}\), form a partition of that family. Every packet is
canonically isomorphic to \(\mathcal V^r\) and has \(24^r\) vertices.

#### Proof

Let \(T\in\mathcal P(S)\). Every block in \(I(S)\) remains eligible,
because its new restriction is still in \(\mathcal V_i\). Every index
\(j<i_r(S)\) which is not in \(I(S)\) was ineligible for \(S\), and its
restriction is frozen by (2.5), so it remains ineligible for \(T\).
Therefore

\[
 I(T)=I(S).                                            \tag{2.8}
\]

The exterior is also unchanged, \(C(T)=C(S)\), and hence
\(\mathcal P(T)=\mathcal P(S)\).

Thus membership in one packet is an equivalence relation on
\(\{Z\ge r\}\). If two packets intersect, an intersection vertex has the
same first-\(r\) index set and the same exterior for both, so the packets
are equal. They therefore partition the good family. Finally, the \(r\)
selected block restrictions vary independently over 24 choices, giving
\(|\mathcal P(S)|=24^r\). \(\square\)

In particular, if \(\mathfrak P\) is the set of distinct packets, then

\[
 G=|\mathfrak P|\,24^r.                               \tag{2.9}
\]

## 3. The exceptional middle mass

The leave first has an exact coefficient formula. Put

\[
 A(x)=(1+x)^8-24x^4,\qquad \ell=|R_0|.                 \tag{3.1}
\]

Here \(24x^4\) records an eligible block, while \(A(x)\) records an
ineligible block. Hence

\[
 \boxed{
 W-G=
 \sum_{z=0}^{r-1}\binom Bz
 [x^m](24x^4)^zA(x)^{B-z}(1+x)^\ell.}                 \tag{3.2}
\]

### Proposition 3.1 (finite tail bound)

Let \(G=|\{S\in\binom{[n]}m:Z(S)\ge r\}|\). If

\[
 r\le {3B\over64},                                    \tag{3.3}
\]

then (0.3) holds.

#### Proof

Choose a random subset \(\mathbf S\subseteq[n]\) by taking every
coordinate independently with probability \(1/2\). For one eight-block,

\[
 \Pr(\mathbf S\cap B_i\in\mathcal V_i)
 ={24\over2^8}={3\over32}.                            \tag{3.4}
\]

The blocks are disjoint, so before conditioning

\[
 Z(\mathbf S)\sim\operatorname{Bin}\left(B,{3\over32}\right),
 \qquad
 \mu:=\mathbb EZ={3B\over32}.                          \tag{3.5}
\]

Condition (3.3) says \(r\le\mu/2\). The multiplicative Chernoff bound
therefore gives

\[
 \Pr\{Z(\mathbf S)<r\}
 \le\Pr\{Z(\mathbf S)<\mu/2\}
 \le e^{-\mu/8}
 =\exp\!\left(-{3B\over256}\right).                    \tag{3.6}
\]

Conditioning \(\mathbf S\) on \(|\mathbf S|=m\) gives the uniform law on
\(\binom{[n]}m\). Moreover,

\[
 \Pr\{|\mathbf S|=m\}={W\over2^{2m+1}}.                \tag{3.7}
\]

The elementary central-coefficient bound

\[
 \binom{2m}{m}\ge {4^m\over2m+1}
\]

and

\[
 W=\binom{2m+1}{m}
 ={2m+1\over m+1}\binom{2m}{m}
\]

give

\[
 \Pr\{|\mathbf S|=m\}\ge {1\over2(m+1)}.               \tag{3.8}
\]

Dividing (3.6) by (3.8) proves

\[
 {W-G\over W}
 =\Pr\{Z<r\mid|\mathbf S|=m\}
 \le2(m+1)e^{-3B/256}.
\]

This is (0.3). \(\square\)

If \(r=o(m)\), condition (3.3) holds for all sufficiently large \(m\),
and the right side of (0.3) is \(e^{-\Omega(m)}\). The power-of-two
condition is irrelevant to this mass estimate; it enters only in the
cycle factor.

## 4. Tensor product cells

Fix a canonical packet \(\mathcal P\), write its selected blocks in the
order \(i_1<\cdots<i_r\), and fix

\[
 \varepsilon=(\varepsilon_1,\ldots,\varepsilon_r)
 \in\{0,1\}^r.                                        \tag{4.1}
\]

In block \(i_j\), use the local six-cell decomposition
\(\mathscr D_{\varepsilon_j}\). For a tuple

\[
 (D_1,\ldots,D_r)\in
 \mathscr D_{\varepsilon_1}\times\cdots\times
 \mathscr D_{\varepsilon_r},                          \tag{4.2}
\]

let its product cell consist of all packet vertices whose restriction to
\(B_{i_j}\) lies in \(D_j\).

### Theorem 4.1 (exact tensor-cell decomposition)

For every \(\varepsilon\), the cells (4.2) partition \(\mathcal P\) into
exactly \(6^r\) pairwise disjoint isometric copies of

\[
 Q_2^{\square r}=Q_{2r}=Q_h.                           \tag{4.3}
\]

#### Proof

Lemma 1.1 partitions each local factor \(\mathcal V_{i_j}\) into six
disjoint squares. Taking Cartesian products preserves disjointness and
exhausts

\[
 \mathcal V_{i_1}\times\cdots\times\mathcal V_{i_r}.
\]

There are \(6^r\) tuples. Each product has

\[
 4^r=2^{2r}=2^h                                       \tag{4.4}
\]

vertices and \(2r=h\) independent binary directions.

Inside one local square the two directions exchange endpoints in two
disjoint coordinate pairs. Different blocks are coordinate-disjoint.
Thus all \(h\) directions in the product cell have disjoint physical
supports. The cell has a fixed physical core of size
\((m-4r)+2r=m-h\), together with one chosen endpoint from each of its
\(h\) active pairs. Thus Hamming distance in the product equals Johnson
distance between the corresponding middle sets, so the embedding in
\(J(n,m)\) is isometric. Finally,

\[
 6^r2^h=6^r4^r=24^r,                                  \tag{4.5}
\]

which agrees with the packet size. \(\square\)

Thus the \(2^r\) choices of \(\varepsilon\) give \(2^r\) exact alternative
cell decompositions of the same middle support. They are alternative
integral resolutions, not \(2^r\) simultaneously available copies of the
vertices.

## 5. The Hamming-syndrome \(C_{2h}\)-factor in every cell

### Theorem 5.1 (explicit cell factor)

Let \(h=2^t\ge2\). For each single prescribed ordering \(\sigma\) of the
\(h\) directions, every labelled \(Q_h\)-cell has a spanning
\(2\)-factor into

\[
 {2^h\over2h}                                         \tag{5.1}
\]

vertex-disjoint isometric cycles \(C_{2h}\), all having the common
direction word

\[
 \sigma\,\sigma                                       \tag{5.2}
\]

for any chosen ordering \(\sigma\) of the \(h\) cell directions.

#### Proof

Relabel the prescribed order as \(1,\ldots,h\), identify the cell with
\(\mathbb F_2^h\), and let \(e_1,\ldots,e_h\) be its direction basis.
Put

\[
 p_0=0,\qquad
 p_{j+1}=p_j+e_{1+(j\bmod h)}
 \quad(0\le j<2h).                                    \tag{5.3}
\]

The resulting closed walk

\[
 C=(p_0,p_1,\ldots,p_{2h-1})                          \tag{5.4}
\]

is a simple isometric \(C_{2h}\). Indeed, every cyclic arc of at most
\(h\) edges uses distinct directions, so its length equals the Hamming
distance of its endpoints.

Let \(g_0,\ldots,g_{h-1}\) be any listing of
\(\mathbb F_2^t\) with \(g_0=0\), and put

\[
 \Sigma=\mathbb F_2^t\oplus\mathbb F_2.
\]

Define a linear syndrome map

\[
 \phi:\mathbb F_2^h\longrightarrow\Sigma              \tag{5.5}
\]

by

\[
 \phi(e_j)=(g_j+g_{j-1},0)\quad(1\le j<h),\qquad
 \phi(e_h)=(g_{h-1},1).                                \tag{5.6}
\]

Telescoping gives

\[
 \phi(p_j)=(g_j,0),\qquad
 \phi(p_{h+j})=(g_j,1)
 \quad(0\le j<h).                                     \tag{5.7}
\]

Hence \(\phi\) maps the \(2h=2^{t+1}\) vertices of \(C\) bijectively onto
\(\Sigma\). Let

\[
 K=\ker\phi,\qquad |K|=2^{h-t-1}={2^h\over2h}.         \tag{5.8}
\]

The translates

\[
 \{C+k:k\in K\}                                       \tag{5.9}
\]

partition \(\mathbb F_2^h\). For if \(x\in\mathbb F_2^h\), there is a
unique \(p_j\in C\) with \(\phi(p_j)=\phi(x)\), and then
\(x=p_j+k\) for the unique \(k=x+p_j\in K\). Translation preserves
isometry and the direction word. \(\square\)

This is a syndrome construction; its kernel need not be the classical
perfect Hamming code. The theorem asserts one vertex factor. A resolution
of all cube edges is stronger and requires \(h/2\) such vertex factors.

Applying Theorem 5.1 independently in the \(6^r\) cells gives

\[
 6^r{2^h\over2h}
 ={6^r4^r\over2h}
 ={24^r\over2h}                                       \tag{5.10}
\]

cycles in one packet. Applying it in all canonical packets proves
(0.5)--(0.6).

For later window work, a useful deterministic order is the two-layer
block order. If the two directions in selected block \(i_j\) are
\(d_j^0,d_j^1\), take

\[
 \sigma=(d_1^0,\ldots,d_r^0,d_1^1,\ldots,d_r^1).       \tag{5.11}
\]

Then every cyclic window of at most \(r\) directions meets each selected
eight-block at most once. The theorem, however, allows any ordering.

## 6. Exact consecutive-window incidence and the remaining gate

Fix one of the packet factors from Sections 4--5 and orient every cycle.
For a cycle

\[
 C=(X_0,\ldots,X_{2h-1})
\]

and \(1\le q<h\), define the physical lower and upper decorations of the
window beginning at \(s\) by

\[
 L_q(C,s)=\bigcap_{j=0}^q X_{s+j},\qquad
 U_q(C,s)=\bigcup_{j=0}^q X_{s+j},                    \tag{6.1}
\]

with subscripts modulo \(2h\). Since the window uses \(q\) distinct
exchange directions,

\[
 |L_q(C,s)|=m-q,\qquad |U_q(C,s)|=m+q.                \tag{6.2}
\]

The \(q+1\) states span a unique affine \(q\)-face \(F(C,s,q)\) of the
host cell. Its free directions are the \(q\) directions used by the
window, and

\[
 L_q(C,s)=\bigcap_{X\in F(C,s,q)}X,\qquad
 U_q(C,s)=\bigcup_{X\in F(C,s,q)}X.                   \tag{6.3}
\]

### Lemma 6.1 (the exact order restriction)

Let the cell direction word be \(\sigma\sigma\). For \(1\le q<h\), a
specified \(q\)-set \(D\) of cell directions is used by a consecutive
window if and only if \(D\) is a cyclic \(q\)-interval of \(\sigma\).
If it is such an interval, its direction set occurs at exactly two starts
on each cycle; otherwise it occurs at none.

#### Proof

Every length-\(q\) subword of \(\sigma\sigma\) is a cyclic interval of
\(\sigma\), and the two halves give the same interval twice. Conversely,
all consecutive direction sets arise this way. For \(q<h\), distinct
cyclic starting positions in the first copy of \(\sigma\) give distinct
sets: their circular incidence words have different endpoints. \(\square\)

For a host cell \(Q\), an affine \(q\)-face \(F\subseteq Q\), and its
selected factor \(\mathscr H_Q\), define the exact integer

\[
 a_{Q,q}(F)=
 \#\{(C,s):C\in\mathscr H_Q,\ F(C,s,q)=F\}.            \tag{6.4}
\]

Then

\[
 \sum_{\substack{F\subseteq Q\\\dim F=q}}a_{Q,q}(F)=2^h, \tag{6.5}
\]

because the factor has one window start at each cell vertex. Lemma 6.1
implies

\[
 a_{Q,q}(F)=0
\quad\text{unless the direction set of }F
\text{ is a cyclic interval of }\sigma.               \tag{6.6}
\]

No assertion is made that the nonzero values in (6.4) equal one. Kernel
translations and antipodal phases can make their affine-face supports
correlated.

The correlation has the following exact algebraic form. Identify a cell
with \(\mathbb F_2^h\). For \(D\subseteq[h]\), put

\[
 E_D=\operatorname{span}\{e_i:i\in D\},
\qquad
 A(D,\theta)=\{x:x|_{D^c}=\theta\},                   \tag{6.6a}
\]

where \(\theta\in\mathbb F_2^{D^c}\). Allow a syndrome factor translated
by \(z\), so its cycles are

\[
 z+k+(p_s)_{s\in\mathbb Z/(2h)},\qquad k\in K=\ker\phi. \tag{6.6b}
\]

### Lemma 6.2 (exact affine-face/phase criterion)

Fix a face \(A(D,\theta)\) and a phase \(s\), and let \(D_s\) be the
\(q\) consecutive directions beginning there. Let \(x_\theta\) equal
\(\theta\) on \(D^c\) and zero on \(D\). The phase-\(s\) windows span
\(A(D,\theta)\) if and only if

\[
 D=D_s
\quad\text{and}\quad
 \phi(x_\theta+z+p_s)\in\phi(E_D).                    \tag{6.6c}
\]

When this condition holds, the exact number of cycles whose phase-\(s\)
window spans the face is

\[
 |K\cap E_D|
 =2^{q-\operatorname{rank}(\phi|_{E_D})}.             \tag{6.6d}
\]

#### Proof

The direction condition is Lemma 6.1. A cycle indexed by \(k\in K\)
starts at \(z+k+p_s\), so its window spans \(A(D,\theta)=x_\theta+E_D\)
exactly when

\[
 (z+p_s+K)\cap(x_\theta+E_D)\ne\varnothing.
\]

Applying \(\phi\) gives (6.6c), and the implication reverses because a
preimage difference with zero syndrome lies in \(K\). If the intersection
is nonempty, its admissible \(k\)'s form a coset of \(K\cap E_D\). Rank
nullity gives (6.6d). \(\square\)

Summing over all cells and packets gives the literal fine loads

\[
 \mu_q^-(T)=
 \sum_{\substack{Q,F\subseteq Q\\\dim F=q,\ \cap F=T}}
 a_{Q,q}(F),                                          \tag{6.7}
\]

\[
 \mu_q^+(U)=
 \sum_{\substack{Q,F\subseteq Q\\\dim F=q,\ \cup F=U}}
 a_{Q,q}(F).                                          \tag{6.8}
\]

Their total occurrence masses are exactly

\[
 \sum_T\mu_q^-(T)=\sum_U\mu_q^+(U)=G.                 \tag{6.9}
\]

### The balanced fine-window target

For fixed \(A>0\), put

\[
 K_A=\lceil A\sqrt m\rceil.
\]

The desired loads must arise from one choice of physical cycles, common to
every \(q\le K_A\), rather than from separate depthwise factors. To state
the target exactly, put

\[
 N_q^-=\binom n{m-q},\qquad c_q^-=\left\lfloor{W\over N_q^-}\right\rfloor,
\]

\[
 N_q^+=\binom n{m+q},\qquad c_q^+=\left\lfloor{W\over N_q^+}\right\rfloor,
\]

let \(\mathcal B_q^\pm\) be the integer quota vectors on the corresponding
rank whose entries lie in \(\{c_q^\pm,c_q^\pm+1\}\) and whose sum is
\(W\). An additive exceptional completion means

\[
 \widehat\mu_q^\pm=\mu_q^\pm+\delta_q^\pm,\qquad
 \delta_q^\pm\ge0,\qquad
 \|\delta_q^\pm\|_1=W-G.                              \tag{6.9a}
\]

Thus it adds one occurrence per omitted middle start and does not rewire
the retained cell cycles. Define

\[
 O_q^\pm=
 \min_{b\in\mathcal B_q^\pm}
 \sum_T\bigl(\widehat\mu_q^\pm(T)-b(T)\bigr)_+.        \tag{6.10}
\]

The symmetric fine-window target is

\[
 \boxed{
 \sum_{q=1}^{K_A}
 \left({O_q^-\over c_q^-}+{O_q^+\over c_q^+}\right)=o(W).}
                                                               \tag{6.11}
\]

The essential word “consecutive” means that every retained contribution
is certified by (6.4), not merely by the existence of a candidate face in
the product cube.

### Theorem 6.3 (uniform-order Hamming factors fail the fine target)

Suppose every product cell is resolved by a translate factor from
Theorem 5.1. Allow the shore vector, direction order, and syndrome factor
to vary arbitrarily from cell to cell. Suppose also that the exceptional
completion leaves these retained cycles unchanged and contributes one
additional depth-\(q\) start for each of the \(W-G\) omitted owners. Let

\[
 q_*=\left\lceil2\log_2h\right\rceil.                 \tag{6.12}
\]

If \(h\to\infty\) and \(h=o(m)\), then \(q_*<h\) and

\[
 \left|\operatorname{supp}\widehat\mu_{q_*}^-\right|
 \le {G\over h}+(W-G)=o(W).                           \tag{6.13}
\]

Moreover,

\[
 N_{q_*}^-=(1-o(1))W,\qquad c_{q_*}^-=1,              \tag{6.14}
\]

and therefore every additive completed load (6.9a) satisfies

\[
 \boxed{O_{q_*}^-\ge(1-o(1))W.}                       \tag{6.15}
\]

In particular, the choices listed in Sections 4--5 cannot satisfy
(6.11), even at this single logarithmic depth. Moreover
\(q_*\le K_A\) for every fixed \(A>0\) and all sufficiently large \(m\).

#### Proof

Fix one \(Q_h\)-cell. Its cycles all have one common cyclic direction
order. At depth \(q<h\), Lemma 6.1 permits only \(h\) direction sets.
For a fixed \(q\)-set of directions, \(Q_h\) has exactly
\(2^{h-q}\) affine faces, one for every assignment of the other
\(h-q\) coordinates. Hence the lower-decoration support contributed by
one cell is at most

\[
 h2^{h-q}.                                             \tag{6.16}
\]

There are exactly \(G/2^h\) selected product cells globally. Summing
(6.16), and allowing collisions only to reduce support, gives

\[
 |\operatorname{supp}\mu_q^-|
 \le {G\over2^h}h2^{h-q}
 ={Gh\over2^q}.                                        \tag{6.17}
\]

Since \(2^{q_*}\ge h^2\), the retained support is at most \(G/h\).
Adding one depth-\(q_*\) occurrence for each of the \(W-G\) exceptional
starts enlarges support by at most \(W-G\), proving (6.13).

Because \(q_*=O(\log m)=o(\sqrt m)\),

\[
 {N_{q_*}^-\over W}
 =\prod_{j=0}^{q_*-1}{m-j\over m+j+2}
 =1-o(1).                                              \tag{6.18}
\]

Thus \(1<W/N_{q_*}^-<2\) eventually, proving \(c_{q_*}^-=1\).
Every balanced quota \(b\in\mathcal B_{q_*}^-\) is at least one on every
one of the \(N_{q_*}^-\) targets. Outside the load support its deficit is
therefore at least one. Since both the completed load and \(b\) have total
mass \(W\), total positive excess equals total deficit. Consequently

\[
 O_{q_*}^-
 \ge N_{q_*}^-
      -|\operatorname{supp}\widehat\mu_{q_*}^-|
 =(1-o(1))W,
\]

which is (6.15). \(\square\)

The exponential packet leave is not the issue: \(W-G=e^{-\Omega(m)}W\).
The obstruction comes from using one direction order on every cycle of a
cell. The same conclusion survives any recoding of only \(o(W)\) retained
start occurrences, since such a recoding enlarges support by at most
\(o(W)\). It does not survive unrestricted fusion that rewires a positive
density of retained starts.

### A surviving sufficient fine gate \(\mathrm{MFCW}_A\) (unproved)

Replace the uniform-order translate factor in each cell by a
middle-vertex factor whose component orders may vary, or permit
middle-owner-preserving fusions between cells. Choose these factors,
packet shores, phases, and the exceptional completion once for all
depths so that the actual consecutive-window incidences (6.4) satisfy
(6.11), together with the corresponding literal wreath compilation.

There is an exact necessary order-richness condition even before load
balance. Let \(R_Q\) be the number of distinct cyclic \(\sigma\sigma\)
order catalogues used by cycles retained in cell \(Q\), where rotations
of one cyclic order count as the same catalogue. Each catalogue exposes
at most \(h\) depth-\(q\) direction sets, so

\[
 |\operatorname{supp}\mu_q^-|
 \le h2^{h-q}\sum_Q R_Q.                              \tag{6.19}
\]

Since the number of cells is \(G/2^h\), support
\((1-o(1))W\) requires

\[
 {2^h\over G}\sum_QR_Q
 \ge(1-o(1)){2^q\over h}.                             \tag{6.20}
\]

At \(q=q_*\), the average cell therefore needs at least
\((1-o(1))h\) distinct cyclic orders. This is only a necessary support
condition. The surviving theorem must additionally control affine phases,
collisions of identical labelled targets across cells and packets, the
coupled lower and upper decorations, and the common all-depth choice.

Equation (6.11) is a symmetric sufficient packet target, not the logically
minimal compiler ledger. Two distinct surviving interfaces must be kept
separate.

For the direct finite-cycle compiler, take

\[
 {H\over\sqrt m}\longrightarrow\infty,\qquad
 H=o(m^{2/3}),\qquad {H\over h}\longrightarrow0,
\]

and define its exact physical-hole ledger

\[
 D_H=
 \sum_{q=1}^{H}
 \left[
 N_q^- -|\operatorname{supp}\mu_q^-|
 +N_q^+ -|\operatorname{supp}\mu_q^+|
 \right].                                             \tag{6.21}
\]

The required gate for that compiler is \(D_H=o(W)\), together with its
already separate collar and outer-tail hypotheses. Theorem 6.3 refutes
this gate for the uniform-order factors, because its single
depth-\(q_*\) lower-hole term is \((1-o(1))W\).

For the MWB route, the exact interface is instead:

1. compile the selected packet construction into one literal exact
   odd-wreath factor; and
2. with \(O_q^-\) computed from the **final literal wreath histogram**,
   prove

   \[
   \sum_{q\le K_A}{O_q^-\over c_q^-}=o_A(W).           \tag{6.22}
   \]

The independent upper term in (6.11) is stronger than MWB requires.
Conversely, merely having \(\Theta(W)\)-sized support in each rank does
not imply either the \(o(W)\) aggregate hole ledger or MWB.

## 7. Adversarial scope audit

1. **Middle packets, not wreaths.** A \(C_{2h}\) in \(J(n,m)\) is a
   physical exchange cycle, but it is not automatically the length-\(n\)
   cyclic-window orbit of a coordinate order.

2. **Alternative shores, not multiplied ownership.** The \(2^r\) vectors
   \(\varepsilon\) give alternative exact decompositions of one packet.
   Selecting several would repeat every middle owner.

3. **A vertex factor, not an edge resolution.** The factor in one
   \(Q_h\)-cell uses \(2^h\) of its \(h2^{h-1}\) edges. The full resolvable
   edge theorem is stronger and is not needed for (0.5).

4. **Coarse eligibility is insufficient.** A target may admit many
   completions into first-\(r\) packets while none of their prescribed
   direction sets is consecutive in a chosen \(\sigma\).

5. **No face-simplicity claim.** Equation (6.5) counts starts with
   multiplicity. It does not say that \(2^h\) distinct affine faces occur.

6. **No independent-depth selection.** Choosing a different shore,
   order, or factor at each \(q\) would not define one physical
   construction and is excluded from \(\mathrm{MFCW}_A\).

7. **The native fine gate is refuted, not merely open.** Theorem 6.3
   applies even when shores, orders, syndrome maps, and shifts vary by
   cell. It fails only if one allows different component orders inside a
   cell or abandons the cell boundary.

The unconditional positive theorem ends at the packet and cycle factors
(0.3)--(0.6). The same note proves the uniform-order no-go (6.15). The
displayed surviving sufficient hypothesis is the mixed-order or cross-cell
incidence theorem \(\mathrm{MFCW}_A\), followed by literal wreath
compilation.
