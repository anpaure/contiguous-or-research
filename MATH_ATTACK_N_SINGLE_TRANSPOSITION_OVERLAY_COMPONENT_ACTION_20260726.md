# Lane N: single-transposition overlays, bounded packets, and target action

Date: 2026-07-26

Method: pure mathematics only. No finite search or computation is used.

Throughout, \(C_j=\operatorname {Cat}_j\), \(D_j\) is the set of Dyck
words of semilength \(j\), and \(F_r\) is the canonical anchored
\(D_r\)-port MSW factor. Put

\[
                         s_i=(2i\ \ 2i+1),
                 \qquad 1\le i<r.                       \tag{0.1}
\]

## 0. Exact outcome

There are two corrections and three positive theorems.

1. The proposed **all-column permutation representation** of the full
   ownership components, using only generators

   \[
                         f_t=\kappa_t\kappa_0^{-1}       \tag{0.2}
   \]

   is false as a representation and proof: such a colour-column
   permutation need not exist. The formula is exact for the \(X\)-state
   suboverlay. A fixed
   adjacent-union colour column need not induce a permutation of row
   owners; an explicit \(r=3\) column has owner list \(1,1,3,4,5\).
   The full components are the connected components obtained after
   adjoining these generally noninjective colour-owner edges. The
   \(X\)-orbits only a priori refine the full partition; the counterexample
   to the representation does not by itself prove a strict merger.

2. For \(s_1=(2\ 3)\), the already proved full state-and-colour component
   hierarchy remains exact:

   \[
   \boxed{
   |K|=k_j:=C_j+C_{j+1},\qquad
   \#\{K:|K|=k_j\}=C_{r-j-2}}
             \quad(0\le j\le r-2).                      \tag{0.3}
   \]

   Every component has \(k_j\) rows on each shore and can be switched
   independently while preserving one exact anchored factor. Its maximum
   shore size is

   \[
   M_r=C_{r-2}+C_{r-1}
      =\left(\frac5{16}+O(r^{-1})\right)C_r.             \tag{0.4}
   \]

3. If \(K\) is an actual full component, its exact full local depth-\(q\)
   action is

   \[
   \boxed{
   \Delta_{q,K}=s_{i*}\mu_{q,\kappa_0^{-1}K}-\mu_{q,K}.} \tag{0.5}
   \]

   For the \(s_1\) hierarchy, \(\kappa_0K=K\), so this simplifies to the
   antisymmetric action

   \[
                         \Delta_{q,K}=s_{1*}\mu_{q,K}-\mu_{q,K}.          \tag{0.6}
   \]

4. Let \(p\to\infty\), and choose \(r\) minimally with

   \[
                         d:=C_r\ge4p.                   \tag{0.7}
   \]

   Then \(r=\Theta(\log p)\), \(4p\le d<16p\), and \(M_r>p\).
   Nevertheless every component layer \(j\le r-4\) has even its
   old-plus-new support \(2k_j<p\), for all sufficiently large \(p\).
   This uniform strict packet menu contains

   \[
   d-(C_{r-1}+2C_{r-2}+C_{r-3})
      =\left(\frac{39}{64}+o(1)\right)d                 \tag{0.8}
   \]

   direct \(F_r\)-rows.

5. The answer to “split or relocate?” depends on which plateau is meant.

   * A target common to **all** \(D_r\)-rows is split at owner level but
     remains in the two target bins \(S,s_1S\). If \(s_1S\ne S\), its
     exact optimal distinguished cap-\(p\) excess is \(d-2p\); if
     \(s_1S=S\), it is \(d-p\).
   * The aligned \(D_r\) child plateau inside \(F_{r+1}\) is genuinely
     multi-bin. Parent component \((j,R)\) has exact child action

     \[
     \boxed{
     \Delta^{\rm child}_{j,R}
       =C_j(e_{S_{2j+4}}-e_{S_2}).}                     \tag{0.9}
     \]

     Thus the layers expose \(S_4,S_6,\ldots,S_{2r+2}\), not one
     coordinate mate. The unique top component carries the indivisible
     chunk \(C_{r-1}>p\), so every choice still has distinguished excess
     at least

     \[
                              C_{r-1}-p.                 \tag{0.10}
     \]

     The uniform strict packet menu contains
     \((21/32+o(1))d\) child occurrences. Its remaining distinguished
     feasibility problem is an exact bounded integer capacity problem,
     stated in Section 7.

The decisive conclusion is therefore not a one-transposition no-go.
The direct common fibre is only a two-bin relocation, but the recursive
child is a genuine Catalan packet disperser. What remains open is whether
its multi-bin distinguished gain survives the full crossing-collar
histogram and composes across ambient contexts.

## 1. The exact owner graph

Write the canonical rooted trace as

\[
              X_0(u),X_1(u),\ldots,X_r(u),
                 \qquad u\in D_r,                       \tag{1.1}
\]

and put

\[
                         Y_a(u)=X_a(u)\cup X_{a+1}(u),
                         \qquad0\le a<r.                 \tag{1.2}
\]

The \(X\)-columns are Chung--Feller transversals. The flaw-preserving
swap \(s_i\) preserves each such layer and therefore defines involutions

\[
  s_iX_t(u)=X_t(\kappa_tu),\qquad
  \kappa_t\in\operatorname {Sym}(D_r),
                    \qquad0\le t\le r.                  \tag{1.3}
\]

At the rooted port,

\[
                         \kappa_0=s_i|_{D_r}.            \tag{1.4}
\]

Swapping steps \(2i,2i+1\) preserves Dyckness: immediately before this
pair the height is a positive odd integer, so either order of the two
steps stays nonnegative and has the same endpoint.

The raw transposed row \(s_iC_v\) has physical root \(\kappa_0v\).
After reindexing the transposed shore by its physical root \(u\), its row
is

\[
                         C_u^{(s)}=s_iC_{\kappa_0^{-1}u}.                \tag{1.5}
\]

Its phase-\(t\) \(X\)-state is

\[
 s_iX_t(\kappa_0^{-1}u)
   =X_t(\kappa_t\kappa_0^{-1}u)
   =X_t(f_tu),\qquad f_t=\kappa_t\kappa_0^{-1}.          \tag{1.6}
\]

In particular \(f_0=1\).

For a colour \(Y\), let \(\operatorname {own}_F(Y)\in D_r\) be the root
of its unique canonical owner row. Define

\[
 a_a(u)=\operatorname {own}_F
       \bigl(s_iY_a(\kappa_0^{-1}u)\bigr),
                    \qquad0\le a<r.                     \tag{1.7}
\]

These are owner maps \(D_r\to D_r\), but they need not be permutations.

### Theorem 1.1 (contracted full owner graph)

After contracting the phase-zero port matching, the full ownership
overlay of \(F_r\) and \(s_iF_r\) is the undirected graph \(\Gamma_i\)
on \(D_r\) with edges

\[
                         u\;--\;f_tu
                    \quad(0\le t\le r)                  \tag{1.8}
\]

and

\[
                         u\;--\;a_a(u)
                    \quad(0\le a<r).                    \tag{1.9}
\]

Its connected components are exactly the common physical-root blocks of
the independently switchable full ownership components. The orbits of

\[
                         G_i^X=\langle f_t:0\le t\le r\rangle           \tag{1.10}
\]

are the components of the \(X\)-state suboverlay and refine, but need not
equal, the full components.

#### Proof

The phase-zero state joins the two rows with physical root \(u\); contract
these edges. Formula (1.6) gives (1.8). Formula (1.7) is exactly the
canonical owner of the colour in the transposed row rooted at \(u\), so it
gives (1.9). The two ownership ledgers consist of all \(X\)-states and all
\(Y\)-colours, hence there are no other overlay edges. Omitting the colour
edges leaves the Schreier graph of the permutations \(f_t\), whose
components are the \(G_i^X\)-orbits. \(\square\)

For one \(X\)-column, an \(f_t\)-cycle of length \(\ell\) is an
alternating state-overlay cycle of length \(2\ell\) before the port edges
are contracted. Colour edges can merge several such cycles and several
\(G_i^X\)-orbits.

### Proposition 1.2 (the permutation-only model is false)

For \(r=3\) and \(s_1=(2\ 3)\), the canonical paths are

\[
\begin{array}{c|cccc}
1&123&136&146&456\\
2&124&126&156&356\\
3&125&145&345&346\\
4&135&235&245&246\\
5&134&234&236&256.
\end{array}                                             \tag{1.11}
\]

Their first colour column is

\[
                 1236,\quad1246,\quad1245,\quad1235,\quad1234.          \tag{1.12}
\]

Applying \(s_1\) gives

\[
                 1236,\quad1346,\quad1345,\quad1235,\quad1234.          \tag{1.13}
\]

The canonical owner rows of (1.13) are

\[
                              1,1,3,4,5.                \tag{1.14}
\]

Indeed \(1236,1346\) are the first two colours of row \(1\), \(1345\)
is the second colour of row \(3\), and the last two retain owners \(4,5\).
Thus this colour-owner map repeats row \(1\) and omits row \(2\); it is not
a permutation. Consequently the \(f_t\)-orbit theorem cannot be extended
to all ownership columns without replacing permutations by the relation
graph of Theorem 1.1. \(\square\)

## 2. Anchor involution and full target action

On the \(X\)-state suboverlay, every \(\kappa_t\) is an involution, so

\[
             \kappa_0f_t\kappa_0
                =\kappa_0\kappa_t=f_t^{-1}.             \tag{2.1}
\]

Thus \(\kappa_0\) normalizes \(G_i^X\). For the full owner graph, use the
uncontracted bipartite involution

\[
 \Xi(L_u)=R_{\kappa_0u},\qquad
 \Xi(R_u)=L_{\kappa_0u}.                                \tag{2.2}
\]

If a token \(Z\) witnesses \(L_a--R_u\), then \(s_iZ\) witnesses
\(L_{\kappa_0u}--R_{\kappa_0a}\). Hence \(\Xi\) is a graph automorphism,
and after contraction \(\kappa_0\) permutes the actual full component
blocks.

Let \(K\subseteq D_r\) be one actual full component block in physical-root
indexing. For any completely local coordinate-equivariant depth-\(q\)
statistic, let

\[
                         \mu_{q,K}(T)
   =\sum_{u\in K}v_q(C_u;T)                             \tag{2.3}
\]

be its complete canonical target histogram on \(K\).

### Theorem 2.1 (correct full component vector)

Switching \(K\) has exact signed action

\[
\boxed{
 \Delta_{q,K}(T)
   =\mu_{q,\kappa_0^{-1}K}(s_iT)-\mu_{q,K}(T).}         \tag{2.4}
\]

If \(\kappa_0K=K\), then

\[
\boxed{
 \Delta_{q,K}(T)=\mu_{q,K}(s_iT)-\mu_{q,K}(T).}         \tag{2.5}
\]

In that stable case,

\[
 \Delta_{q,K}(s_iT)=-\Delta_{q,K}(T),\qquad
 \Delta_{q,K}(T)=0\quad(s_iT=T),                        \tag{2.6}
\]

so every two-point \(s_i\)-target-orbit total is invariant componentwise.

#### Proof

By (1.5), the new shore over physical root block \(K\) is

\[
                         \{s_iC_v:v\in\kappa_0^{-1}K\}.                 \tag{2.7}
\]

Coordinate equivariance gives \(v_q(s_iC;T)=v_q(C;s_iT)\). Sum over
(2.7) and subtract the canonical rows rooted in \(K\). This proves (2.4).
Stability gives (2.5), and (2.6) follows from \(s_i^2=1\). \(\square\)

If \(K'=\kappa_0K\ne K\), then \(K'\) is another full component and

\[
 \Delta_{q,K}+\Delta_{q,K'}
  =s_{i*}(\mu_{q,K}+\mu_{q,K'})
     -(\mu_{q,K}+\mu_{q,K'}).                           \tag{2.8}
\]

Thus target-orbit totals are preserved by the paired switch, not
necessarily by either nonstable component alone.

For one actual consecutive \(X\)-phase interval \(I\), put

\[
                         T_I(u)=\bigcap_{t\in I}X_t(u).                  \tag{2.9}
\]

Then the exact occurrence vector is

\[
 \Delta_{K,I}
   =\sum_{u\in K}
      \left(e_{\,s_iT_I(\kappa_0^{-1}u)}
                    -e_{\,T_I(u)}\right).              \tag{2.10}
\]

The same formula holds for any coordinate-equivariant local union,
intersection, or ordered signature.

If \(T_I(u)=S\) for every \(u\in D_r\), then stability is unnecessary:

\[
                         \Delta^{\rm dist}_{K,I}
                              =|K|(e_{s_iS}-e_S).        \tag{2.11}
\]

## 3. Complete boundary hierarchy

Take \(i=1\). For \(0\le j\le r-2\), define

\[
 \mathcal A_j
 =\{1u0:u\in D_{j+1}\}
   \mathbin{\dot\cup}
   \{10\,1v0:v\in D_j\}.                                \tag{3.1}
\]

For \(R\in D_{r-j-2}\), put

\[
                         \mathcal C_{j,R}=\mathcal A_jR.                \tag{3.2}
\]

### Theorem 3.1 (full \(s_1\)-component law)

The sets \(\mathcal C_{j,R}\) are exactly the full state-and-colour
ownership component blocks. They are \(\kappa_0=s_1\)-stable, and

\[
 |\mathcal C_{j,R}|=k_j=C_j+C_{j+1},\qquad
 \#\{R\}=C_{r-j-2}.                                    \tag{3.3}
\]

#### Proof

Every Dyck word has a unique factorization \(AR\), where \(A\) is its
shortest Dyck prefix of length at least four. The possibilities for an
atom of semilength \(j+2\) are exactly (3.1). The MSW concatenation law is

\[
 P_r(AR)=P_{j+2}(A)R\ \Vert\
       \overline A\bigl(P_{r-j-2}(R)\setminus\{R\}\bigr).               \tag{3.4}
\]

The proved full-ownership suffix-lifting theorem says that every state and
colour-owner edge retains \(R\). Boundary connectivity makes the complete
ownership overlay connected on \(\mathcal A_j\). Thus (3.2) is one full
component, and the cells exhaust \(D_r\). The two families in (3.1) have
sizes \(C_{j+1},C_j\). Finally (3.1) is invariant under swapping bits two
and three, proving \(\kappa_0\)-stability. \(\square\)

The size check is

\[
 \sum_{j=0}^{r-2}C_{r-j-2}(C_j+C_{j+1})=C_r.           \tag{3.5}
\]

Since \(k_j\) increases with \(j\),

\[
                         M_r=C_{r-2}+C_{r-1}.            \tag{3.6}
\]

The exact Catalan ratios give

\[
\boxed{
 \frac{M_r}{C_r}
  =\frac{(r+1)(5r-6)}
          {4(2r-1)(2r-3)}.}                            \tag{3.7}
\]

This is \(5/16+O(1/r)\), is strictly larger than \(1/4\) for every
\(r\ge2\), and is at most \(1/2\) for every \(r\ge4\). The two inequalities
reduce respectively to

\[
                         r^2+7r-9>0,\qquad
                         3(r-1)(r-4)\ge0.               \tag{3.8}
\]

Coordinate reversal gives the identical spectrum for \(s_{r-1}\).

For every component \(\mathcal C_{j,R}\), the full depth-\(q\) action is
therefore exactly

\[
 \Delta_{q,j,R}(T)
      =\mu_{q,j,R}(s_1T)-\mu_{q,j,R}(T).                \tag{3.9}
\]

## 4. General \(i\): sealed full components and maximum bounds

The complete closed hierarchy is not known for an arbitrary interior
\(s_i\), but there is a uniform sealed library.

### Theorem 4.1 (shifted two-row component)

For

\[
 P\in D_{i-1},\qquad R\in D_{r-i-1},                    \tag{4.1}
\]

the two roots

\[
                         P1100R,\qquad P1010R            \tag{4.2}
\]

form one complete full ownership component. It has two rows per shore and
four rows in its old-plus-new trade support. For fixed \(i\), this gives

\[
                         C_{i-1}C_{r-i-1}                \tag{4.3}
\]

pairwise disjoint displayed components.

#### Proof

MSW concatenation makes the four-coordinate \(1100\leftrightarrow1010\)
rectangle literal after the complete prefix \(P\) and before the suffix
\(R\). Its internal \(X\)-matching interchanges the two owners; its four
adjacent-union colours are permuted within the same two-row ledger. Hence
no state or colour edge leaves the pair, and one state edge connects it.
Different \((P,R)\) give disjoint pairs. \(\square\)

These pairs are \(\kappa_0\)-stable, so their complete target action is
(3.9) with the appropriate \(s_i\).

There is a larger contextual hierarchy. Put

\[
                         a=i-1,\qquad b=r-i+1.           \tag{4.4}
\]

For every \(P\in D_a\), the sector \(PD_b\) is sealed, and its restricted
full overlay is the boundary \(s_1\)-overlay in dimension \(b\). Hence its
full components are

\[
                         P\mathcal A_jR,\qquad
 0\le j\le b-2,\quad R\in D_{b-j-2},                   \tag{4.5}
\]

with shore size \(k_j\). Over all prefixes, their multiplicity is

\[
                         C_{i-1}C_{r-i-j-1}.            \tag{4.6}
\]

Indeed,

\[
 P_r(PQ)=P_a(P)Q\ \Vert\
       \overline P\bigl(P_b(Q)\setminus\{Q\}\bigr).     \tag{4.7}
\]

During the prefix portion, \(Q\) is a common spectator in every state and
adjacent union, so physical-root reindexing gives identity owner edges on
the suffix label. The remaining transitions are the context lift of the
complete dimension-\(b\) \(s_1\)-overlay. This proves closure and the
component law. Every component in (4.5) is \(\kappa_0\)-stable.

These sectors cover \(C_{i-1}C_{r-i+1}\) roots and have maximum component
size \(M_{r-i+1}\). All unclassified components lie in the complement.
Therefore

\[
 M_{i,r}\le
 \max\left\{M_{r-i+1},
      C_r-C_{i-1}C_{r-i+1}\right\}.                    \tag{4.8}
\]

Reflection gives independently

\[
 M_{i,r}\le
 \max\left\{M_{i+1},
      C_r-C_{r-i-1}C_{i+1}\right\}.                    \tag{4.9}
\]

The minimum of the right sides of (4.8)--(4.9) is the strongest currently
proved general-\(i\) maximum bound. It need not be at most \(p\) at the
fatal scale.

## 5. Packet sizes at \(r=\Theta(\log p)\)

Let \(r=r(p)\) be minimal with \(d=C_r\ge4p\). Minimality and

\[
                         \frac{C_r}{C_{r-1}}
                           =4-\frac6{r+1}               \tag{5.1}
\]

give the exact bounds

\[
 4p\le d<
 \left(16-\frac{24}{r+1}\right)p<16p.                  \tag{5.2}
\]

Also \(r=\Theta(\log p)\).

### 5.1 The maximum is too large, but many packets fit

By (3.7),

\[
                         M_r>\frac d4\ge p.             \tag{5.3}
\]

Thus the false maximum-\(p\) claim is decisively ruled out at the fatal
scale. Still,

\[
                         M_r<(5+o(1))p,                 \tag{5.4}
\]

so every boundary component is \(O(p)\).

For every \(j\le r-4\),

\[
 k_j\le k_{r-4}
    =C_{r-4}+C_{r-3}
    =\left(\frac5{256}+o(1)\right)d.                   \tag{5.5}
\]

Since \(5/256<1/32\), (5.2) implies

\[
                             2k_j<p                    \tag{5.6}
\]

for all sufficiently large \(p\). This meets the stricter convention in
which packet size counts both deleted and inserted rows.

Only the layers \(j=r-3,r-2\) are omitted from this uniform menu. Their
one-shore root mass is

\[
                         C_{r-1}+2C_{r-2}+C_{r-3}.      \tag{5.7}
\]

Consequently the retained one-shore mass is exactly

\[
 d-(C_{r-1}+2C_{r-2}+C_{r-3})
    =\left(\frac{39}{64}+o(1)\right)d.                 \tag{5.8}
\]

This is the mass of the **chosen uniform menu**, not necessarily of all
\(p\)-components; an omitted layer can also fit for a favourable Catalan
overshoot.

The number of retained independent switches is

\[
                         \sum_{h=2}^{r-2}C_h
                           =\left(\frac1{12}+o(1)\right)d.              \tag{5.9}
\]

### 5.2 Interior sealed sectors

If \(i\ge3\), then \(b=r-i+1\le r-2\). Every component in every certified
prefix sector has

\[
 2|K|\le2M_b\le2M_{r-2}
    =\left(\frac{10}{256}+o(1)\right)d<p               \tag{5.10}
\]

for all sufficiently large \(p\). Thus all components in those sectors
are strict \(p\)-packets. They cover

\[
                         C_{i-1}C_{r-i+1}               \tag{5.11}
\]

roots. Reflection gives the corresponding suffix sectors for
\(i\le r-3\). Components crossing the context cut remain unclassified.

### 5.3 If all components must fit

Define

\[
 r_p^{\rm side}=\max\{r:M_r\le p\},\qquad
 r_p^{\rm supp}=\max\{r:2M_r\le p\}.                   \tag{5.12}
\]

Both are \(\Theta(\log p)\), and

\[
 C_{r_p^{\rm side}}=\Theta(p),\qquad
 C_{r_p^{\rm supp}}=\Theta(p).                         \tag{5.13}
\]

At these smaller scales every boundary component fits the corresponding
packet convention. Because successive Catalan numbers differ by a factor
tending to four, no single sharper leading constant holds for arbitrary
integer \(p\).

## 6. A direct common \(D_r\)-plateau is only two-bin

Suppose one distinguished occurrence in every canonical row of \(F_r\)
has the same target \(S\). For component \((j,R)\), (2.11) gives

\[
                         k_j(e_{s_1S}-e_S).             \tag{6.1}
\]

For a component selection, put

\[
 a=\sum_{j=0}^{r-2}\sum_{R\in D_{r-j-2}}
                      \varepsilon_{j,R}k_j,
             \qquad\varepsilon_{j,R}\in\{0,1\}.         \tag{6.2}
\]

If \(s_1S\ne S\), the exact distinguished loads are

\[
                         \mu(S)=d-a,\qquad
                         \mu(s_1S)=a,                   \tag{6.3}
\]

and no third target receives a token. This is genuine packet fragmentation
at owner scale—the \(C_{r-2}\) size-two components already give that many
independent choices—but all choices control only the scalar \(a\) at
target scale.

For every \(a\),

\[
                         (d-a-p)_++(a-p)_+\ge d-2p.     \tag{6.4}
\]

At \(d\ge4p\), (3.7) gives

\[
                         p\le M_r\le d/2\le d-p.        \tag{6.5}
\]

Switching the largest component alone therefore attains equality in
(6.4). Hence the exact direct distinguished optimum is

\[
\boxed{
 \min_{\varepsilon}
 \bigl[(\mu(S)-p)_++(\mu(s_1S)-p)_+\bigr]=d-2p.}        \tag{6.6}
\]

If \(s_1S=S\), every switch leaves all \(d\) tokens at \(S\), and the
excess is \(d-p\).

Thus the direct all-\(D_r\) plateau is split into owner packets but merely
relocated between two target bins. This statement must not be transferred
to a child subset which is not \(\kappa_0\)-stable.

## 7. The aligned child is genuinely multi-bin

To act on an aligned \(D_r\)-child fibre, use the parent \(F_{r+1}\). Its
components are

\[
 \mathcal C_{j,R}=\mathcal A_jR,\qquad
 0\le j\le r-1,\quad R\in D_{r-j-1},                   \tag{7.1}
\]

with shore size \(k_j\) and multiplicity \(C_{r-j-1}\).

The aligned right-child roots are \(10w\), \(w\in D_r\). Their intersection
with component \((j,R)\) is exactly

\[
                         u=10\,1v0\,R,\qquad v\in D_j,                  \tag{7.2}
\]

so it has \(C_j\) roots. Every old distinguished noninitial child window
has target

\[
                         S_2=O\cup\{2\}.                \tag{7.3}
\]

The new row over physical root \(u\) is \(s_1C_{s_1u}\), and

\[
                         s_1u=1(10v)0R.                 \tag{7.4}
\]

For \(P=1a0b\), the first MSW flip is

\[
                         \rho_1(P)=|a|+2.               \tag{7.5}
\]

Here \(a=10v\) has length \(2j+2\), so the first inserted coordinate is
\(2j+4\), which \(s_1\) fixes.

### Theorem 7.1 (exact child action)

Switching component \((j,R)\) has distinguished child vector

\[
\boxed{
 \Delta^{\rm child}_{j,R}
      =C_j(e_{S_{2j+4}}-e_{S_2}),
           \qquad S_h=O\cup\{h\}.}                     \tag{7.6}
\]

#### Proof

There are \(C_j\) roots in (7.2). Equations (7.3)--(7.5) show that each
old target is \(S_2\) and each new target is \(S_{2j+4}\), independently
of \(v,R\). Summing gives (7.6). \(\square\)

Whole-component stability does not contradict (7.6). The child subset is
not stable: (7.4) sends it into the primitive half of \(\mathcal A_j\).
Already in parent dimension three, the two child layers move from target
\(2\) to targets \(4\) and \(6\), not to target \(3\).

The Catalan convolution

\[
 \sum_{j=0}^{r-1}C_jC_{r-j-1}=C_r=d                    \tag{7.7}
\]

shows that these chunks partition the full child plateau. The \(j=0\)
layer consists of \(C_{r-1}\) independent two-row switches, each moving
one child occurrence from \(S_2\) to \(S_4\).

If \(n_j\) layer-\(j\) components are switched, then

\[
                         0\le n_j\le C_{r-j-1},         \tag{7.8}
\]

and the exact child loads are

\[
\boxed{
\begin{aligned}
 \mu(S_2)&=d-\sum_{j=0}^{r-1}C_jn_j,\\
 \mu(S_{2j+4})&=C_jn_j
                   \qquad(0\le j\le r-1).
\end{aligned}}                                         \tag{7.9}
\]

This is the requested componentwise distinguished action. It exposes
\(r\) different destination bins.

### 7.1 Exact packet-capacity criterion

Let

\[
 \mathcal J_p^{\rm side}=\{j:k_j\le p\},\qquad
 \mathcal J_p^{\rm supp}=\{j:2k_j\le p\}.               \tag{7.10}
\]

These respectively count one replacement shore or the full old-plus-new
support as packet size. Fix either allowed set \(\mathcal J\).
A distinguished cap-\(p\) assignment using only these packets exists
exactly when there are integers

\[
 0\le n_j\le
 \min\left\{C_{r-j-1},
            \left\lfloor\frac p{C_j}\right\rfloor\right\},
                 \qquad j\in\mathcal J,                \tag{7.11}
\]

such that

\[
                         \sum_{j\in\mathcal J}C_jn_j\ge d-p.            \tag{7.12}
\]

Equivalently, put

\[
 Q_p(\mathcal J)=
 \sum_{j\in\mathcal J}C_j
 \min\left\{C_{r-j-1},
            \left\lfloor\frac p{C_j}\right\rfloor\right\}.              \tag{7.13}
\]

Then feasibility is equivalent to

\[
                         Q_p(\mathcal J)\ge d-p.        \tag{7.14}
\]

Necessity is immediate from (7.9). For sufficiency, \(j=0\) belongs to
either allowed set for \(p\ge4\), its chunk size is one, and
\(C_{r-1}>p\), so it supplies \(p\) unit increments. Maximize the other
layers. If their total is at most \(d-p\), (7.14) says the unit layer fills
the deficit. If it exceeds \(d-p\), remove increments until the total
first falls below \(d-p\). Every removable increment has size at most
\(p\) by (7.11), so the remaining deficit is at most \(p\) and the unit
layer again fills it. This proves sufficiency.

### 7.2 The indivisible top obstruction

The unique top component \(j=r-1\) carries the child chunk

\[
 c=C_{r-1}
   =\frac{r+1}{2(2r-1)}d>\frac d4\ge p.                \tag{7.15}
\]

If it is unswitched, these \(c\) tokens remain at \(S_2\). If it is
switched, all \(c\) move together to \(S_{2r+2}\). Therefore every
component choice, even without a packet restriction, has distinguished
excess at least

\[
\boxed{
                         C_{r-1}-p.}                    \tag{7.16}
\]

Write \(\theta=d/p=4+\varepsilon_r\). Then

\[
 \frac{C_{r-1}-p}{p}
   =\frac{\varepsilon_r}{4}+\frac{3}{2r}
      +O\left(\frac{\varepsilon_r}{r}+\frac1{r^2}\right).              \tag{7.17}
\]

Thus the obstruction is \(O(p/r)\) when
\(\theta-4=O(1/r)\), and is
\((3/(2r)+o(r^{-1}))p\) under the sharper endpoint condition
\(\theta-4=o(1/r)\). Merely assuming \(d\sim4p\) is not enough for the
latter asymptotic. In general its exact value is

\[
                         \frac{r+1}{2(2r-1)}d-p.        \tag{7.18}
\]

The exact distinguished optimization is

\[
 \min_{(n_j)}
 \left[
  \left(d-\sum_jC_jn_j-p\right)_+
   +\sum_j(C_jn_j-p)_+
 \right],                                              \tag{7.19}
\]

with bounds (7.8), and with \(n_j=0\) outside the permitted packet set
when a packet restriction is imposed. Formula (7.16) is an unconditional
lower bound; equality in (7.19) is not asserted.

### 7.3 Uniform strict packet mass

For \(j\le r-4\), (5.6) gives \(2k_j<p\). The child mass outside this
uniform menu is

\[
 C_{r-1}+C_{r-2}+2C_{r-3}
    =\left(\frac{11}{32}+o(1)\right)d.                 \tag{7.20}
\]

Hence this menu contains

\[
                         \left(\frac{21}{32}+o(1)\right)d              \tag{7.21}
\]

child occurrences. This is not the exact mass of all strict packets:
the next layer can also fit for a favourable overshoot.

If every new destination is required to stay below \(p\), at most \(p\)
of the \(C_{r-1}\) unit chunks in layer zero may move. Thus this fixed
uniform menu can move at most

\[
                         p+\sum_{j=1}^{r-4}C_jC_{r-j-1}                 \tag{7.22}
\]

tokens without overloading a destination. It consequently leaves source
excess at least

\[
 \left(\frac{19}{32}+o(1)\right)d-2p
      \ge\left(\frac38+o(1)\right)p.                   \tag{7.23}
\]

This last obstruction is only for the fixed menu \(j\le r-4\), not for
the full overshoot-dependent set of \(p\)-packets.

## 8. Scope and proved boundary

1. The permutation-only all-phase theorem is disproved by Proposition 1.2.
   The exact general substitute is the owner relation graph in Theorem 1.1.
   The \(f_t\)-orbits remain an exact and useful refinement from the
   \(X\)-state ledger.

2. The complete spectrum, exact maximum, and Catalan packet constants are
   proved for \(s_1\) and, by reflection, \(s_{r-1}\). For interior \(i\),
   Sections 4--5 assert only the sealed contextual components and the
   displayed maximum bounds.

3. Formula (2.4) is exact for the direct local face and for a fully local
   statistic with a common exterior carrier. In a larger ambient context,
   a crossing collar can have an exterior carrier depending on the anchored
   root. Its full ambient action must be computed from (2.10) with that
   carrier retained; it need not be one global \(s_i\)-pushforward.

4. The direct common-\(D_r\) result (6.6) is genuinely two-bin. The aligned
   child result (7.6) is genuinely multi-bin. Confusing the whole stable
   component with its nonstable child subset gives the false destination
   \(S_3\).

5. In different affine parent contexts, the physical coordinate pairs
   representing \(s_1\) differ. Their target sets can overlap. Neither the
   local lower bound (7.16) nor the local multi-bin capacity can be summed
   globally without a separate overlap/matching theorem.

6. The lane is therefore closed at an exact new gate: choose the integers
   \(n_j\) through (7.9)--(7.14), then prove favorable drift for the full
   affected-window histograms (2.4), including all crossing collars, under
   simultaneous ambient component choices. The single-transposition face
   supplies literal integral \(p\)-packets and real multi-bin distinguished
   dispersion; it does not yet supply the full coefficient-one theorem.

## 9. Audit record

Three independent adversarial audits checked the component indexing,
Catalan constants, packet conventions, and target vectors. They found two
decisive corrections retained in this report:

* colour-owner columns need not be permutations, so \(f_t\)-orbits alone
  do not give full components;
* the aligned child destination of layer \(j\) is \(2j+4\), because its
  physical-root preimage lies in the primitive Catalan half.

The exact \(s_1\) hierarchy, its \(\kappa_0\)-stability, the ratios
\(5/16,39/64,21/32\), the generic full action (2.4), and the direct
two-bin calculation were independently rechecked after these corrections.
