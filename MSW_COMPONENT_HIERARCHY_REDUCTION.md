# Exact Catalan component hierarchy for the MSW factor

> **Status.**  Unconditional.  The boundary-connectivity input is proved for
> every dimension in `MSW_BOUNDARY_CONNECTIVITY.md`; the suffix-local induction
> below therefore gives the exact component law for every \(m\).

## 1. The theorem

Let $F_m$ be the MSW wreath factor on $2m+1$ coordinates, indexed by the
Dyck words $\mathcal D_m$, and let $\tau=(2\ 3)$.  Compare $F_m$ with
$\tau F_m$ in their middle-set interaction graph.

### Theorem

For $0\le j\le m-2$ and $R\in\mathcal D_{m-j-2}$, put

\[
 \mathcal A_j=
 \{1u0:u\in\mathcal D_{j+1}\}
 \;\dot\cup\;
 \{10\,1v0:v\in\mathcal D_j\},                     \tag{1.1}
\]

and

\[
                 \mathcal C_{j,R}=\{AR:A\in\mathcal A_j\}. \tag{1.2}
\]

The sets $\mathcal C_{j,R}$ are exactly the connected components of the
interaction graph (on either factor side).  Hence

\[
 \boxed{
 \#\{\text{components of size }
       \operatorname{Cat}_j+\operatorname{Cat}_{j+1}\}
   =\operatorname{Cat}_{m-j-2}
 }
 \qquad(0\le j\le m-2).                              \tag{1.3}
\]

The proof has two ingredients: the boundary-connectivity theorem proved in
MSW_BOUNDARY_CONNECTIVITY.md and the suffix-local induction below.

## 2. Concatenation is literal locality

The MSW flip permutation satisfies

\[
 \rho(1u0v)=
 (|u|+2,\ |u|+2-\rho(\operatorname{rev}u),\ 1,
                  |u|+2+\rho(v)).                  \tag{2.1}
\]

A direct induction on the first primitive component gives

\[
       \rho(PQ)=\rho(P)\mathbin\Vert(|P|+\rho(Q))    \tag{2.2}
\]

for all Dyck words $P,Q$.  Consequently, if
$P_p(P)=(P_0,\ldots,P_{2p})$ and
$P_q(Q)=(Q_0,\ldots,Q_{2q})$ are the MSW paths, then

\[
 P_{p+q}(PQ)=
 (P_0Q,P_1Q,\ldots,\overline P Q,
  \overline P Q_1,\ldots,\overline P\,\overline Q). \tag{2.3}
\]

Thus every coordinate in $P$ is flipped before any coordinate in $Q$.

## 3. Every Dyck word has one active atom

Let $x\in\mathcal D_m$, $m\ge2$, and decompose it into primitive Dyck
components.  If the first primitive has semilength at least two, call that
primitive $A$.  If the first primitive is $10$, let $A$ be the
concatenation of the first two primitives.  Let $R$ be the remaining
suffix.  Equivalently, $A$ is the shortest Dyck prefix of length at least
four.

This gives a unique factorization

\[
                         x=AR.                       \tag{3.1}
\]

If $A$ has semilength $j+2$, then either

\[
 A=1u0\quad(u\in\mathcal D_{j+1}),
 \qquad\text{or}\qquad
 A=10\,1v0\quad(v\in\mathcal D_j).                  \tag{3.2}
\]

Therefore the sets in (1.2) partition $\mathcal D_m$.

The endpoint family $\mathcal A_j$ is stable under swapping bits $2,3$.
Indeed, a word of the first type begins $11$.  It is fixed when its third
bit is $1$; otherwise

\[
               1(10v)0\ \stackrel\tau\longleftrightarrow\
               10(1v0).                              \tag{3.3}
\]

## 4. Suffix-lifting lemma

### Lemma

Suppose $X\subseteq\mathcal D_s$ has these two properties:

1. the union of the vertices of $P_s(x)$ over $x\in X$ is
   $\tau$-invariant;
2. $X$ is $\tau$-invariant at its Dyck endpoints.

Then, for every Dyck suffix $R$, the union of the paths $P(xR)$,
$x\in X$, is $\tau$-invariant.  Every local interaction edge in $X$ also
lifts after appending $R$.

### Proof

By (2.3), every vertex of $P(xR)$ has one of the two forms

\[
                         zR\quad(z\in P(x))           \tag{4.1}
\]

or

\[
                         \overline x\,w\quad(w\in P(R)). \tag{4.2}
\]

The family (4.1) is invariant by property 1.  For (4.2),

\[
          \tau(\overline x\,w)=\overline{\tau x}\,w,
\]

which remains in (4.2) by property 2.  Appending the common suffix $R$ to
a local witness proves the edge statement.  $\square$

## 5. Connectivity of the top atom

For a primitive word $x=1u0$, the recursive MSW formula says that its
middle piece is

\[
 \{1\mu(q)1:q\in P(\mu(u))\},                      \tag{5.1}
\]

where $\mu(w)=\overline{\operatorname{rev}(w)}$.  Literal path reversal gives

\[
 P(\mu(u))
   =\{\operatorname{rev}(z):z\in P(u)\}.             \tag{5.2}
\]

Consequently (5.1) is exactly

\[
                 \{1\overline z1:z\in P(u)\}.       \tag{5.3}
\]

Swapping global bits $2,3$ in (5.3) is therefore the left-boundary swap
on $z$, followed by bitwise complementation.  If $z\in P(u)$ and
$s_1z\in P(u')$, then (5.3) supplies the corresponding interaction edge
between the primitive roots $1u0$ and $1u'0$.  The boundary-connectivity
theorem therefore shows that

\[
                 \{1u0:u\in\mathcal D_{s-1}\}       \tag{5.4}
\]

is connected in the interaction graph for $\tau=(2\ 3)$.

Every word of the second type attaches by an endpoint edge:

\[
                    \tau(10\,1v0)=1(10v)0.           \tag{5.5}
\]

The right side belongs to (5.4).  Hence the whole top atom family
$\mathcal A_{s-2}$ is connected.

## 6. Induction and closure

We induct on $m$.  The case $m=2$ is the explicit two-wreath component
indexed by $1100,1010$.

Assume the theorem below dimension $m$.  Every class
$\mathcal C_{j,R}$ with nonempty $R$ is the suffix lift of the top class in
dimension $j+2<m$.  By induction and the suffix-lifting lemma it is closed
and connected.

The MSW paths partition the two middle levels, so the path-vertex unions of
these proper classes are disjoint.  Remove their $\tau$-invariant union.
Its complement is also $\tau$-invariant, and the unique active-atom
factorization says that this complement is precisely the top class
$\mathcal A_{m-2}$.  Section 5 says that the top class is connected.
It is therefore one component.  This completes the induction.

## 7. Enumeration

For fixed $j$,

\[
 |\mathcal A_j|=\operatorname{Cat}_{j+1}+\operatorname{Cat}_j, \tag{7.1}
\]

while the number of possible suffixes is
$\operatorname{Cat}_{m-j-2}$.  This proves (1.3).  The component sizes add
to the entire factor because

\[
 \sum_{j=0}^{m-2}
 \operatorname{Cat}_{m-j-2}
 (\operatorname{Cat}_j+operatorname{Cat}_{j+1})
 =\operatorname{Cat}_m.                              \tag{7.2}
\]

Equivalently, with $C(z)=\sum_{r\ge0}\operatorname{Cat}_rz^r$,

\[
 \sum_{j\ge0}(\operatorname{Cat}_j+operatorname{Cat}_{j+1})z^j
 =C(z)+C(z)^2,                                       \tag{7.3}
\]

and (7.2) follows from $C(z)=1+zC(z)^2$.

## 8. Shifted size-two subcomponents

Equation (2.2) also gives a useful nested family.  For
$P\in\mathcal D_s$ and $R\in\mathcal D_{m-s-2}$, the words

\[
                  P1100R,\qquad P1010R               \tag{8.1}
\]

form a legal two-for-two interaction component for the shifted
transposition

\[
                  (2s+2\ \ 2s+3).                   \tag{8.2}
\]

For fixed $s$ this supplies

\[
                  \operatorname{Cat}_s
                  \operatorname{Cat}_{m-s-2}         \tag{8.3}
\]

disjoint size-two components.  This is the nested Catalan self-similarity
behind the full hierarchy.

## 9. Global component spectrum

Let \(K_m\) be the total number of components.  Summing (1.3) gives the
exact formula

\[
 K_m=\sum_{j=0}^{m-2}\operatorname{Cat}_{m-j-2}
    =\sum_{r=0}^{m-2}\operatorname{Cat}_r.             \tag{9.1}
\]

Since

\[
 \frac{\operatorname{Cat}_{m-2}}{\operatorname{Cat}_m}
 =\frac{m(m+1)}{4(2m-1)(2m-3)}\longrightarrow\frac1{16}
\]

and

\[
 \frac{K_m}{\operatorname{Cat}_{m-2}}\longrightarrow
 \sum_{r\ge0}4^{-r}=\frac43,
\]

we obtain

\[
                     K_m\sim\frac1{12}\operatorname{Cat}_m. \tag{9.2}
\]

Thus this transposition exposes a linear-dimensional cube of independent
switches, not merely a subexponential exceptional family.

For every fixed \(j\), the proportion of all components having size
\(\operatorname{Cat}_j+\operatorname{Cat}_{j+1}\) tends to

\[
 \frac{\operatorname{Cat}_{m-j-2}}{K_m}
       \longrightarrow \frac{3}{4^{j+1}}.             \tag{9.3}
\]

In particular, asymptotically three quarters of all components are the
size-two switches at \(j=0\), three sixteenths have size three, and the
remaining components occur at successively larger Catalan scales.  The
hierarchy therefore supplies both many microscopic absorbers and a sparse
family of macroscopic corrections.

There is an exact two-ended split in vertex mass.  Components with fixed
small \(j\) account asymptotically for

\[
 \sum_{j\ge0}
   \frac{\operatorname{Cat}_j+\operatorname{Cat}_{j+1}}{4^{j+2}}
 =\frac38                                                   \tag{9.4}
\]

of all MSW roots.  If instead the suffix depth
\(r=m-j-2\) is fixed, the corresponding component family accounts for

\[
 \sum_{r\ge0}
   \frac{5\operatorname{Cat}_r}{4^{r+2}}
 =\frac58.                                                   \tag{9.5}
\]

The two limits add to one.  This makes the hierarchy genuinely multiscale:
the small components dominate by count, while the top Catalan components
carry most of the vertices.  Any global switching or absorption argument
can therefore be organized recursively by active-atom depth rather than by
dimension-specific search.
