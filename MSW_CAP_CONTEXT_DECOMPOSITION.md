# Capped MNW contexts without a wrap-fibre assumption

This note proves the context step needed in the boundary-connectivity
argument for the MSW path factor.  Its purpose is to avoid a false
statement: the owner of a capped vertex does **not** commute with the MNW
mirror-wrap operation vertex by vertex.  The correct proof uses a different
outer operation and moves the only mirror all the way down to the finite
base pattern.

Throughout, `bar` denotes bitwise complement, `rev` denotes literal reversal,
and

\[
                         \mu(x)=\overline{\operatorname{rev}(x)}
\]

is the Dyck-word mirror.  Let \(P(x)\) be the MSW path rooted at the Dyck
word \(x\), and let \(o(z)\) be the unique root whose path contains \(z\).

## 1. The capped incidence graph

For \(x\in\mathcal D_m\), put

\[
 \mathcal L(x)=\{h:\text{there is }z\in P(x)
                         \text{ with }10z\in P(h)\}.          \tag{1.1}
\]

Define a graph \(G_m\) on \(\mathcal D_m\) by

\[
                 x\sim y\quad\Longleftrightarrow\quad
                 \mathcal L(x)\cap\mathcal L(y)\ne\varnothing . \tag{1.2}
\]

This is exactly the common-hub graph for capped roots.  Indeed,

\[
 P(10x)=(10x,11x,01P(x)).                              \tag{1.3}
\]

Thus \(z\in P(x)\) gives the boundary-transposition incidence

\[
          01z\in P(10x),\qquad 10z\in P(h),             \tag{1.4}
\]

where \(h=o(10z)\).  Consequently, if a set is connected in \(G_m\), then
its capped roots lie in one component of
\(\Gamma_{m+1}^{\partial}\).

Two graph maps are immediate or already proved elsewhere:

* for Dyck \(V\), the map \(x\mapsto xV\) preserves every edge of \(G\),
  because \(P(xV)\) starts with \(P(x)V\) and a common hub \(h\) becomes
  \(hV\);
* for Dyck \(U\), the map \(x\mapsto Ux\) preserves every edge of \(G\).
  This is Corollary 3 of `MSW_PREFIX_CONTEXT_FUNCTOR.md`; a common hub
  \(h=1bR\) becomes
  \(11\theta_b(U)R\).

The third map is the key new simplification.

## 2. Literal reversal of an MSW path

### Lemma 1 (path reversal)

If

\[
                         P(x)=(x_0,x_1,\ldots,x_{2m}),
\]

then

\[
 P(\mu(x))=
 \bigl(\operatorname{rev}(x_{2m}),
       \operatorname{rev}(x_{2m-1}),\ldots,
       \operatorname{rev}(x_0)\bigr).                 \tag{2.1}
\]

In particular,

\[
 z\in P(x)\quad\Longleftrightarrow\quad
 \operatorname{rev}(z)\in P(\mu(x)).                  \tag{2.2}
\]

### Proof

If \(\rho(x)=(r_1,\ldots,r_{2m})\) is the MSW flip order, then a direct
induction in

\[
 \rho(1u0v)=
 (|u|+2,\ |u|+2-\rho(\mu(u)),\ 1,
                         |u|+2+\rho(v))
\]

gives

\[
 \rho(\mu(x))=
 (2m+1-r_{2m},\ldots,2m+1-r_1).                       \tag{2.3}
\]

The first word on the right side of (2.1) is
\(\operatorname{rev}(\bar x)=\mu(x)\), and (2.3) says that the successive
flips are exactly those of \(P(\mu(x))\).  This proves (2.1). \(\square\)

## 3. The outer primitive is a graph functor

Put

\[
                              J(x)=1x0.                 \tag{3.1}
\]

### Lemma 2 (outer-primitive functor)

The map \(J:G_m\to G_{m+1}\) preserves every edge.  More precisely, if
\(h\in\mathcal L(x)\cap\mathcal L(y)\), then

\[
                    J(h)\in\mathcal L(J(x))
                              \cap\mathcal L(J(y)).     \tag{3.2}
\]

### Proof

Choose \(z\in P(x)\) with \(10z\in P(h)\).  By Lemma 1,
\(\operatorname{rev}(z)\in P(\mu(x))\).  The primitive part of the MSW
recursion therefore puts

\[
            1\mu(\operatorname{rev}(z))1
             =1\bar z1
             \quad\hbox{in }P(1x0)=P(J(x)).            \tag{3.3}
\]

Apply the same statement to the vertex \(10z\in P(h)\).  Literal reversal
puts \(\operatorname{rev}(z)01\) in \(P(\mu(h))\), and the primitive
recursion for \(J(h)\) contains

\[
  1\mu(\operatorname{rev}(z)01)1
       =1(01\bar z)1
       =10(1\bar z1).                                  \tag{3.4}
\]

Equations (3.3)--(3.4) are precisely the capped incidence (1.4) from
\(J(x)\) to the hub \(J(h)\).  The same construction with the witness from
\(y\) proves (3.2). \(\square\)

Notice that Lemma 2 is not the false map \(x\mapsto1\mu(x)0\).  It is the
non-mirrored outer primitive \(x\mapsto1x0\); moving the mirror to the base
case is what makes the proof functorial.

## 4. Exact decomposition of an arbitrary MNW context

Let \(c=uv\) be a Dyck word, with the cut between \(u\) and \(v\), and let
\(d\) be the height of that cut.  There are unique Dyck words

\[
 A_0,\ldots,A_d,\qquad B_0,\ldots,B_d                 \tag{4.1}
\]

such that

\[
\begin{aligned}
 u&=A_0\,1A_1\,1\cdots1A_d,\\
 v&=B_d\,0B_{d-1}\,0\cdots B_1\,0B_0 .                \tag{4.2}
\end{aligned}
\]

This is the usual decomposition at the unmatched up-steps crossing the
cut: the \(A_i\)'s and \(B_i\)'s are the complete Dyck excursions between
successive crossing steps.  Since every \(A_i\) is balanced,

\[
                              |u|\equiv d\pmod2.        \tag{4.3}
\]

Let \(S\) be a set of Dyck roots.  Start with

\[
             S_d=A_d\,\mu^d(S)\,B_d                   \tag{4.4}
\]

and, for \(i=d-1,d-2,\ldots,0\), define

\[
             S_i=A_i\,J(S_{i+1})\,B_i .                \tag{4.5}
\]

Expanding (4.5) gives the exact identity

\[
                         S_0=u\,\mu^d(S)\,v.           \tag{4.6}
\]

By (4.3), this is exactly the support prescribed in MNW Lemma 7:
\(uSv\) for even \(|u|\), and \(u\mu(S)v\) for odd \(|u|\).

Every operation in (4.4)--(4.5), except for the single base mirror
\(S\mapsto\mu^d(S)\), is an edge-preserving map proved in Sections 1 and
3.  Therefore arbitrary contexts reduce to the following finite statement:

> each MNW base-pattern support \(S\), and its mirror \(\mu(S)\), is
> connected in the capped incidence graph.

No mirror-wrap owner identity is needed.

## 5. Base certificates

The base family is
\(\Phi=\{\alpha(w):w\in\mathcal D\}\cup\{\beta,\gamma,\delta\}\).
The following tables give common hubs in the sense of (1.1).  Thus a row
\(X,Y;H\) means

\[
                              H\in\mathcal L(X)\cap\mathcal L(Y). \tag{5.1}
\]

All identities below are literal consequences of the three-part MSW path
recursion; no search or existence assertion is used.

### 5.1 The parameterized pattern

The three roots of \(\alpha(w)\) have the common hub

\[
                        H_\alpha(w)=111w10000.          \tag{5.2}
\]

Explicit witnesses \(z\in P(X)\) for which \(10z\in P(H_\alpha(w))\)
are

\[
\begin{array}{c|c}
X&z\\ \hline
1w11000&1w01101\\
1w10100&1w10101\\
1w10010&0\bar w01111.
\end{array}                                             \tag{5.3}
\]

For a direct symbolic verification, put

\[
                         R_w=1110\mu(w)00.              \tag{5.4}
\]

Let \(N=|R_w|=|w|+6\), and write

\[
 R_w=1u0,\qquad u=110\mu(w)0.
\]

Then

\[
 \mu(u)=1w100=1(w10)0,\qquad \mu(w10)=10\mu(w).
\]

The concatenation rule gives

\[
 \rho(10\mu(w))=(2,1,2+\rho(\mu(w))).
\]

Applying the primitive-root recursion first to \(\mu(u)\), and then to
\(R_w\), shows that the first four flip positions of \(P(R_w)\) are

\[
                         |R_w|,\ 2,\ 4,\ 3.             \tag{5.5}
\]

Consequently \(P(R_w)\) contains

\[
 q_2=1010\mu(w)01\quad\text{after two flips},\qquad
 q_1=1001\mu(w)01\quad\text{after four flips},          \tag{5.6}
\]

and it ends at

\[
                         q_3=\bar R_w.                  \tag{5.7}
\]

The hub in (5.2) is

\[
                         H_\alpha(w)=1\mu(R_w)0.         \tag{5.8}
\]

The primitive middle-piece formula puts \(1\mu(q_i)1\) in
\(P(H_\alpha(w))\).  Written out, these are exactly `10` followed by the
three witnesses in (5.3).

It remains to locate the uncapped witnesses in their endpoint paths.  For
the first root, the primitive middle piece is controlled by
\(P(1100\mu(w))\).  Its initial copy \(P(1100)\mu(w)\) contains
\(1001\mu(w)\), and hence the middle piece contains

\[
 1\mu(1001\mu(w))1=1w01101.
\]

For the second root, the controlling path starts at \(1010\mu(w)\), so its
middle piece contains \(1w10101\).  Finally, write

\[
 1w10010=(1(w10)0)10.
\]

The concatenation formula contains

\[
 \overline{1(w10)0}\,11=0\bar w01111,
\]

because \(11\in P(10)\).  These are exactly the three endpoint witnesses
in (5.3), proving all six required memberships uniformly in \(w\).

For the mirrored family put \(t=\mu(w)\).  Its three roots are

\[
 A=10110t0,\qquad B=11010t0,\qquad C=11100t0.          \tag{5.9}
\]

We use the terminal-insertion lemma from
`MSW_PREFIX_CONTEXT_FUNCTOR.md`: if \(q\in P(r)\) ends in `1`, then

\[
 q^-\operatorname{rev}(w)1
   \in P\bigl(r^-\mu(w)0\bigr).                       \tag{5.10}
\]

For \(w=\epsilon\), the center \(C=111000\) has two capped common-hub
edges:

\[
\begin{array}{c|c|c}
\text{edge}&\text{hub}&\text{endpoint witnesses}\\ \hline
C,B&11110000&101101,110101\\
C,A&11101000&111001,011101.
\end{array}                                             \tag{5.11}
\]

Every displayed witness ends in `1`.  Apply (5.10) simultaneously to the
two endpoint paths and to their common hub path.  It sends every root
\(r\) to \(r^-t0\), so the three base roots become exactly the roots in
(5.9), and each common hub remains common.  Hence \(C\) is adjacent to
both \(A\) and \(B\) for every Dyck parameter \(w\).  This proves
connectivity of \(\mu(\operatorname{supp}\alpha(w))\) without a
mirror-wrap assumption.

### 5.2 The constant patterns

For the unmirrored patterns, connected spanning certificates are

\[
\begin{array}{c|c|c|c}
\text{pattern}&X,Y&\text{hub}&z_X,z_Y\\ \hline
\beta&101010,101100&11101000&010111,011101\\
      &101100,111000&11101000&011101,111001\\
\gamma&11001100,11011000&1111001000&00111101,11011001\\
      &11011000,11101000&1111001000&11011001,10111001\\
\delta&101010,101100&11101000&010111,011101\\
      &101100,111000&11101000&011101,111001\\
      &101100,110100&11100100&011011,110011.
\end{array}                                             \tag{5.13}
\]

For their mirrors, connected spanning certificates are

\[
\begin{array}{c|c|c|c}
\text{pattern}&X,Y&\text{hub}&z_X,z_Y\\ \hline
\mu(\beta)&101010,110010&11100010&011110,110110\\
           &110010,111000&11110000&001111,101101\\
\mu(\gamma)&11001100,11100100&1111000100&00111011,10110011\\
            &11001100,11101000&1111001000&00111101,10111001\\
\mu(\delta)&101010,110010&11100010&011110,110110\\
            &110010,110100&11110000&001111,110101\\
            &110100,111000&11110000&110101,101101.
\end{array}                                             \tag{5.14}
\]

In these tables \(z_X\in P(X)\), \(z_Y\in P(Y)\), and both `10`-prefixed
words belong to the displayed hub path.  Thus (5.13)--(5.14) are literal
finite path certificates.  Each membership follows at once by writing the
flip order from the displayed root using the defining recursion.

It follows from (5.2)--(5.14) that both orientations of every base pattern
are connected in \(G\).

## 6. Cap theorem for the full MNW family

### Theorem 3

For every flippable tuple \(\psi\) in the MNW family \(\Psi_m\), the capped
roots

\[
                         \{10x:x\in\operatorname{supp}\psi\}
\]

lie in one component of \(\Gamma_{m+1}^{\partial}\).

### Proof

By the definition of \(\Psi\), there are a base pattern \(\phi\in\Phi\)
and a Dyck word \(uv\) such that the support is

\[
 u\operatorname{supp}(\phi)v
 \quad(|u|\text{ even}),
 \qquad
 u\mu(\operatorname{supp}(\phi))v
 \quad(|u|\text{ odd}).                               \tag{6.1}
\]

Use the cut decomposition (4.2).  Equations (4.4)--(4.6) construct the
support from the appropriate orientation of the base support using only
Dyck-prefix maps, Dyck-suffix maps, and \(J\).  Sections 1 and 3 prove that
all three maps preserve connectedness in \(G\), while Section 5 proves
connectedness of both base orientations.  Hence the support in (6.1) is
connected in \(G_m\).  The incidence interpretation (1.3)--(1.4) gives the
claimed capped connectivity. \(\square\)

Combining Theorem 3 with the MNW spanning-tree theorem gives connectivity
of all roots beginning in `10`.  The standard last-middle-vertex argument
then attaches every remaining Dyck root, yielding boundary connectivity.
