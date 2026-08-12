# Lane Y16: zero-winding fixed-core completions and the sharp congestion boundary

Date: 2026-07-25

Pure mathematics only. No computation, finite search, solver, or web input is used.

## 0. Verdict

Write

$$
N=2r+1,\qquad W=\binom Nr,\qquad
B=\frac{W}{N}=\operatorname{Cat}_r.
$$

Let a genuine zero-winding PBBS return have step-two duration \(s\), and
put \(q=r-s\). The fixed-core theorem gives \((q!)^2\) ambient wreath
completions of its open owner segment.

The proposed equivariant-completion proof does not follow from that
multiplicity. The exact outcome is:

1. All \((q!)^2\) completions funnel through only \(q\) first-shell
   vertices. Each is used by \((q-1)!q!\) completions, and the minimum
   outside-open transversal of all completion tails is exactly \(q\).

2. At every Gaussian scale \(s\asymp\sqrt q\), there is a family of
   \(c_A\binom{2q}{q}\) pairwise vertex-disjoint integral fixed-core
   sectors such that both endpoint edges are genuine PBBS edges, both
   endpoint roots have exact height \(s\) and \(d=1\), yet every possible
   coordinated choice of one ambient completion per sector has a middle
   vertex of load \(\Omega_A(q)\).

3. Those sectors are recurrence-valid Kneser paths, but their intermediate
   edges are not asserted to be the canonical PBBS trajectory. Therefore
   they are an obstruction to an owner/endpoint completion theorem, not a
   counterexample to zero-winding \(CP_A\).

4. Full intermediate chronology kills the simplest contiguous-core
   realization by exactly the missing Catalan factor \(1/(q+1)\). A
   general genuine return can have an interlaced carrier overlap and a
   moving core cut, so that special argument does not prove \(CP_A\).

5. Two exact sufficient gates are isolated below: bounded aggregate load
   for the reciprocal-binomial completion kernel, or bounded congestion
   of the chronology-selected first core shells. Either implies

   $$
   \overline\nu_{H_A}^{\,0}=O_A(B/N),
   $$

   where the superscript denotes the zero-winding sector. Neither gate is
   proved here.

Thus the factorial and canonical-core-order shortcuts are closed. The
remaining issue is genuinely the complete nested \(\tau\)-chronology
across an interlaced overlap. No implication
\(d(D)=1\Rightarrow\) zero winding is used.

## 1. The local owner form has no counting rarity

Let \(A_0,A_1\) be an oriented edge of \(KG(N,r)\), omitting \(u\):

$$
A_0\cap A_1=\varnothing,\qquad
A_0\cup A_1=[N]\setminus\{u\}.
$$

Fix \(1\le s<r\). Choose ordered tuples of distinct elements

$$
(b_0,\ldots,b_{s-1})\subset A_0,\qquad
(a_1,\ldots,a_s)\subset A_1,
$$

put \(a_0=u\), and define

$$
K=A_0\setminus\{b_0,\ldots,b_{s-1}\},\qquad
K'=A_1\setminus\{a_1,\ldots,a_s\}.
$$

Then \(|K|=|K'|=q\).

### Theorem 1.1 (local universality)

Define

$$
A_{2j}
=K\cup\{a_0,\ldots,a_{j-1}\}
   \cup\{b_j,\ldots,b_{s-1}\},
\qquad 0\le j\le s,
\tag{1.1}
$$

$$
A_{2j+1}
=K'\cup\{b_0,\ldots,b_{j-1}\}
   \cup\{a_{j+1},\ldots,a_s\},
\qquad 0\le j\le s,
\tag{1.2}
$$

and

$$
A_{2s+2}=K\cup\{a_1,\ldots,a_s\}.
\tag{1.3}
$$

These states form a simple recurrence-valid Kneser return with omitted
word

$$
(a_0,b_0,a_1,b_1,\ldots,a_{s-1},b_{s-1},a_s,a_0).
\tag{1.4}
$$

Every oriented Kneser edge therefore supports exactly

$$
\boxed{(r)_s^2}
\tag{1.5}
$$

such ordered local sectors.

#### Proof

Direct substitution in (1.1)--(1.3) gives, for the corresponding entry
\(\lambda_t\) of (1.4),

$$
A_{t+1}=[N]\setminus(A_t\cup\{\lambda_t\}),
\tag{1.6}
$$

or equivalently

$$
A_{t+2}=A_t-\{\lambda_{t+1}\}+\{\lambda_t\}.
\tag{1.7}
$$

All labels before the returned endpoint are distinct. Thus every
consecutive pair is a legal Kneser edge and the return is simple. The two
ordered tuples are recovered from the omitted word, so the construction
is injective. There are \((r)_s\) choices of either tuple. \(\square\)

For a genuine zero-winding return, \(d(D_0)=1\) forces

$$
a_1=a_0-1\pmod N.
\tag{1.8}
$$

Even after imposing (1.8), every eligible edge has

$$
\boxed{(r)_s(r-1)_{s-1}}
\tag{1.9}
$$

recurrence-valid local sectors. These statements do not say that the
intermediate edges are PBBS edges. They show exactly why fixed-core
geometry, even with the \(d=1\) seam, contains no zero-winding rarity.

## 2. Exact completion tails

For one sector put

$$
U=\{b_0,\ldots,b_{s-1}\},\qquad
A^+=\{a_0,\ldots,a_s\},\qquad
R=K\mathbin{\dot\cup}K'.
\tag{2.1}
$$

Choose orders

$$
K=(k_1,\ldots,k_q),\qquad
K'=(k'_1,\ldots,k'_q).
$$

After the active omitted word, append

$$
k_1,k'_1,k_2,k'_2,\ldots,k_q,k'_q.
\tag{2.2}
$$

For \(0\le j\le q\), define

$$
R_j
=U\cup\{k_1,\ldots,k_j\}
 \cup\bigl(K'\setminus\{k'_1,\ldots,k'_j\}\bigr),
\tag{2.3}
$$

and, for \(1\le j\le q\),

$$
F_j
=A^+\cup\bigl(K\setminus\{k_1,\ldots,k_j\}\bigr)
 \cup\{k'_1,\ldots,k'_{j-1}\}.
\tag{2.4}
$$

Here \(R_0=K'\cup U\) is the last open owner and
\(R_q=K\cup U=A_0\) is the cyclicly repeated first owner. The new tail
vertices are

$$
F_1,R_1,F_2,R_2,\ldots,F_{q-1},R_{q-1},F_q,
\tag{2.5}
$$

so there are \(2q-1\) of them.

### Theorem 2.1 (tail closure and the completion funnel)

As both core orders vary,

$$
\{R_j\}
=\left\{U\cup L:L\in\binom Rq\right\}
\tag{2.6}
$$

when the two cyclic endpoints are included, while

$$
\{F_j\}
=\left\{A^+\cup L:L\in\binom R{q-1}\right\}.
\tag{2.7}
$$

Every one of the \((q!)^2\) completions first exits through one of

$$
\boxed{
F_k=A^+\cup(K\setminus\{k\}),\qquad k\in K.
}
\tag{2.8}
$$

Each \(F_k\) occurs in exactly

$$
\boxed{(q-1)!q!}
\tag{2.9}
$$

ordered completions.

#### Proof

Equations (2.3)--(2.5) follow from the Kneser recurrence along (2.2).
At an \(R_j\) layer the core contribution is an arbitrary \(q\)-subset
of \(R\); at an \(F_j\) layer it is an arbitrary \((q-1)\)-subset.
This proves (2.6)--(2.7).

The first new state is \(F_1\), which depends only on \(k_1\). Fixing
\(k_1=k\) leaves \((q-1)!\) orders of the rest of \(K\) and \(q!\)
orders of \(K'\). \(\square\)

### Theorem 2.2 (sharp robust capacity)

The minimum number of outside-open middle vertices meeting every
completion tail is exactly

$$
\boxed q.
\tag{2.10}
$$

#### Proof

The first shell (2.8) is a transversal of size \(q\).

For the reverse inequality, fix cyclic orders of \(K,K'\), and take the
\(q\) completions obtained by applying the same cyclic shift to both
orders. At each internal \(R_j\) layer, the selected and deleted core
sets are proper cyclic intervals of length \(j\); distinct shifts give
distinct states. Different \(j\)-layers are distinguished by their
intersection size with \(K\). The same holds on every \(F_j\) layer. An \(R\)-state
meets the active set in \(U\), whereas an \(F\)-state meets it in
\(A^+\), so opposite parities cannot coincide. The \(q\) tails are
internally vertex-disjoint, and every transversal has at least \(q\)
vertices. \(\square\)

Thus the factorial multiplicity has exact robust capacity \(q\), not
\((q!)^2\).

## 3. The reciprocal-binomial completion kernel

Choose the orders of \(K,K'\) independently and uniformly. For every
state in the indicated layer,

$$
\Pr(R_j=X)=\frac{1}{\binom qj^2},
\tag{3.1}
$$

and

$$
\Pr(F_j=X)
=\frac{1}{\binom qj\binom q{j-1}}.
\tag{3.2}
$$

The probability is zero unless \(X\) has the displayed active part and
the corresponding intersection sizes with \(K,K'\).

Let \(\mathcal P\) be a quotient-edge-disjoint family of genuine
zero-winding returns with \(s_I\le H\), on long quotient cycles. Lift all
\(N\) deck phases, and denote the resulting \(N|\mathcal P|\) physical
intervals by \(\widetilde{\mathcal P}\). The conditional load count below
does not require their open endpoints to be disjoint.

For a middle vertex \(X\), let

$$
\Lambda_X
=\sum_{I\in\widetilde{\mathcal P}}
 \Pr\{X\text{ is an outside-open vertex of the random completion of }I\}.
\tag{3.3}
$$

### Theorem 3.1 (conditional completion implication)

If

$$
\sup_X\Lambda_X\le C,
\tag{3.4}
$$

then

$$
\boxed{
|\mathcal P|
\le \frac{CB}{2(r-H)-1}
=\left(C+o_A(1)\right)\frac BN
}
\tag{3.5}
$$

whenever \(H\le A\sqrt r+1\) and \(A\) is fixed.

#### Proof

Every completion tail of \(I\) has \(2q_I-1\) vertices. Hence

$$
\sum_X\Lambda_X
=\sum_{I\in\widetilde{\mathcal P}}(2q_I-1)
\ge N|\mathcal P|\,[2(r-H)-1].
\tag{3.6}
$$

On the other hand, (3.4) gives

$$
\sum_X\Lambda_X\le CW=CNB.
$$

Cancel \(N\). Finally,

$$
\frac{N}{2(r-H)-1}=1+O_A(r^{-1/2}).
$$

\(\square\)

A deterministic choice of one completion per physical interval whose
whole completed wreaths have middle-vertex load at most \(C\) gives the
same conclusion by counting the \(N\) vertices of every completed wreath.

## 4. First-shell regularity and the exact selected-shell gate

Orient an arbitrary spanning \(2\)-factor of \(KG(N,r)\). For a state
\(G\), let \(H=\operatorname{pred}(G)\), and let \(u^-(G)\) be the
coordinate omitted by \(HG\). Define

$$
\mathscr S(G)=\{G-k+u^-(G):k\in G\}.
\tag{4.1}
$$

### Theorem 4.1 (exact full-shell regularity)

The incidence \(G\mapsto\mathscr S(G)\) is \(r\)-regular on both sides.

#### Proof

Every \(G\) has \(r\) displayed shell vertices. Fix a target \(F\). For
each \(k\notin F\), put

$$
H_k=[N]\setminus(F\cup\{k\}).
\tag{4.2}
$$

There are \(r+1\) choices. Exactly one is
\(\operatorname{pred}(F)\). For every other \(k\), write

$$
\operatorname{succ}(H_k)=G_k=F-u_k+k
$$

for the unique \(u_k\in F\). The edge \(H_kG_k\) omits \(u_k\), and

$$
F=G_k-k+u_k\in\mathscr S(G_k).
$$

These are \(r\) distinct preimages. The excluded predecessor of \(F\)
does not contribute \(F\) to its successor's shell. \(\square\)

For a genuine zero return only the inactive \(k\in K_I\) are retained:

$$
\Sigma_I=\{G_I-k+u_I:k\in K_I\},\qquad
|\Sigma_I|=q_I.
\tag{4.3}
$$

Over all physical lifts, set

$$
\Delta(\mathcal P)
=\max_F
 \#\{(I,k):F=G_I-k+u_I,\ k\in K_I\}.
\tag{4.4}
$$

Double counting gives

$$
\boxed{
|\mathcal P|
\le\frac{\Delta(\mathcal P)B}{r-H}
=\left(2+o_A(1)\right)\Delta(\mathcal P)\frac BN.
}
\tag{4.5}
$$

Indeed,

$$
N(r-H)|\mathcal P|
\le\sum_{I\in\widetilde{\mathcal P}}q_I
\le\Delta(\mathcal P)W.
$$

Thus \(\Delta=O_A(1)\) proves the required quotient bound. For an
edge-disjoint family, the terminal centres are distinct, so Theorem 4.1
shows that exactness alone gives only \(\Delta\le r\). The full shell
system attains \(r\) at every target.

There is a genuine zero-winding restriction on represented labels.

### Lemma 4.2 (the \(110\) seam)

If \(F\) is a selected shell target and \(u=a_0\) is the returned label,
then

$$
\boxed{
\bigl(\mathbf1_F(u-1),\mathbf1_F(u),\mathbf1_F(u+1)\bigr)
=(1,1,0).
}
\tag{4.6}
$$

#### Proof

Zero winding gives \(d_0=1\), hence \(a_1=u-1\). The terminal dual cap
is \(\operatorname{ht}(T_{s-1})\le0\), so
\(T_{s-1}=\varnothing\), \(e_{s-1}=1\), and
\(b_{s-1}=u+1\). Every \(a\)-label belongs to \(F\), while every
\(b\)-label is absent from \(F\). \(\square\)

Thus distinct returned labels at one \(F\) are endpoints of cyclic
\(1\)-runs of length at least two. This does not bound
\(\Delta(F)\): several inactive portals \(k\) may have the same \(u\).

There is an exact fixed-\((F,u)\) inversion. Let \(Q_{F,u}\) be the
length-\(2r\) word after \(u\), with bit \(1\) on \(F^c\) and bit \(0\)
on \(F\setminus\{u\}\). Its net height is \(2\). For \(k\in F^c\), put

$$
H_k=[N]\setminus(F\cup\{k\}).
$$

If \(S_j\) is the prefix-height process of \(Q_{F,u}\) and \(k\) occurs
at position \(t\), then \(H_k\) has PBBS unmatched zero \(u\) exactly
when flipping the \(k\)-bit from \(1\) to \(0\) gives a Dyck word, that
is,

$$
\boxed{
\min_{j<t}S_j\ge0,\qquad
\min_{j\ge t}S_j\ge2.
}
\tag{4.7}
$$

This follows because the flip subtracts \(2\) from all prefix heights at
and after \(t\). The word

$$
Q=11(10)^{r-1}
\tag{4.8}
$$

has \(r-1\) such flippable loop up-steps, and every resulting Dyck root
has height at most \(3\). Hence fixed returned label, endpoint PBBS
legality, and small height still allow linear facet multiplicity. Only
the full zero-winding history can bound the subset for which \(k\) stays
inactive.

## 5. An unavoidable \(\Omega(q)\) endpoint-level completion load

Fix \(q\ge1\), \(s\ge4\), \(r=q+s\), and put

$$
b=\lfloor s/2\rfloor.
$$

Partition the coordinates as

$$
\{a_0\}\mathbin{\dot\cup}U\mathbin{\dot\cup}V
\mathbin{\dot\cup}R,
\qquad |U|=|V|=s,\quad |R|=2q.
\tag{5.1}
$$

In the physical order after \(a_0\), place \(b\) elements of \(U\), then
all of \(R\), then the remaining \(s-b\) elements of \(U\), and finally
all of \(V\). Choose the active labels so that
\(b_{s-1}=a_0+1\) and \(a_1=a_0-1\); these are the two endpoint seams
necessary for a genuine zero return.

For \(K\in\binom Rq\), put \(K'=R\setminus K\), and let \(c_K\) be the
balanced word on the ordered set \(R\), with \(1\)'s at \(K\). Let
\(\mathcal K_{q,b}\) consist of those \(K\) for which every prefix sum of
\(c_K\) lies in

$$
[-b+1,b-1].
\tag{5.2}
$$

### Lemma 5.1 (positive strip density)

If \(M(q,b)=|\mathcal K_{q,b}|\), then

$$
\boxed{
M(q,b)\ge
\frac2b\left(2\cos\frac{\pi}{2b}\right)^{2q}.
}
\tag{5.3}
$$

Consequently, for fixed \(0<\alpha\le\beta<\infty\), if

$$
\alpha\sqrt q\le s\le\beta\sqrt q,
$$

then for all sufficiently large \(q\),

$$
\boxed{
M(q,b)\ge c_{\alpha,\beta}\binom{2q}{q}
}
\tag{5.4}
$$

for a positive constant \(c_{\alpha,\beta}\).

#### Proof

The admissible words are closed walks of length \(2q\), based at the
centre of the path graph on \(2b-1\) vertices. Its top and bottom
eigenvalues are

$$
\pm2\cos\frac{\pi}{2b},
$$

and the squared centre coordinate of either normalized eigenvector is
\(1/b\). Both contributions are nonnegative at the even power \(2q\),
which proves (5.3).

When \(b\asymp_{\alpha,\beta}\sqrt q\),

$$
\cos^{2q}\frac{\pi}{2b}\ge c'_{\alpha,\beta}>0.
$$

Wallis' inequalities give
\(\binom{2q}{q}\asymp4^q/\sqrt q\), and
\(b\asymp\sqrt q\). This proves (5.4). \(\square\)

For \(K\in\mathcal K_{q,b}\), the two endpoint words rooted at \(a_0\)
are

$$
D_K=1^b c_K1^{s-b}0^s,\qquad
D'_K=1^b\overline{c_K}1^{s-b}0^s.
\tag{5.5}
$$

Both are primitive Dyck words of exact height \(s\). During the core
bridge their height lies strictly between \(0\) and \(s\); the final
active \(1\)-block first reaches \(s\), and the last \(0\)-block first
returns to \(0\) at its final symbol. Thus both canonical endpoint
factorizations have empty suffix and

$$
d(D_K)=d(D'_K)=1.
\tag{5.6}
$$

The two endpoint edges are literally

$$
K\cup U\longrightarrow K'\cup V,\qquad
K'\cup U\longrightarrow K\cup V,
\tag{5.7}
$$

both omitting \(a_0\). Hence both are genuine PBBS edges. Between them,
use the integral fixed-core formulas (1.1)--(1.3). The resulting
intermediate path is recurrence-valid; no PBBS claim is made for it.

### Theorem 5.2 (high-multiplicity obstruction)

Choose one \(K\) from each complementary pair
\(\{K,R\setminus K\}\) in \(\mathcal K_{q,b}\). The resulting family has
at least

$$
\frac{c_{\alpha,\beta}}2\binom{2q}{q}
\tag{5.8}
$$

pairwise vertex-disjoint open owner paths. For every coordinated,
possibly adaptive and non-equivariant choice of one ambient completion
per path, some middle vertex belongs to at least

$$
\boxed{
\frac{c_{\alpha,\beta}}2(q+1)
}
\tag{5.9}
$$

chosen completion tails.

#### Proof

For the sector indexed by \(K\), every even owner intersects \(R\) in
\(K\), and every odd owner intersects \(R\) in \(K'\). Its active parts
are distinct cyclic \(s\)-windows. Thus two open paths can meet only when
their residual cores are equal or complementary. Keeping one member of
each complementary pair makes the paths vertex-disjoint.

Every chosen completion has \(q\) vertices of the form

$$
A^+\cup T,\qquad
T\in\binom R{q-1},\qquad
A^+=\{a_0\}\cup V.
\tag{5.10}
$$

All paths therefore send \(q\) incidences into the same shell of size
\(\binom{2q}{q-1}\). Pigeonhole and (5.4)--(5.8) give load at least

$$
\frac{q(c_{\alpha,\beta}/2)\binom{2q}{q}}
     {\binom{2q}{q-1}}
=\frac{c_{\alpha,\beta}}2(q+1).
$$

\(\square\)

This is a rigorous \(\Omega_A(r)\) obstruction to the proposed bounded
completion theorem at the owner/endpoint level. It is not an actual PBBS
zero-return family because the intermediate canonical chronology has not
been established.

## 6. What genuine chronology does to the contiguous carrier

The obstruction in Section 5 has one contiguous core carrier.

### Theorem 6.1 (no-overtaking)

Let

$$
D_0=1^b c1^{s-b}0^s
\tag{6.1}
$$

with \(c\) a balanced core word. If the first \(s-b\) step-two PBBS
iterates follow a fixed-core sector in which no core coordinate is
omitted, then

$$
\boxed{\maxpref(c)\le0.}
\tag{6.2}
$$

Consequently \(\overline c\) is Dyck, and there are at most

$$
\boxed{
\operatorname{Cat}_q
=\frac{1}{q+1}\binom{2q}{q}
}
\tag{6.3}
$$

possible core words.

#### Proof

While the first maximum remains in the trailing active \(1\)-block, the
exact block rotation

$$
\tau(P1R0S)=S1P0R
$$

gives

$$
\tau^jD_0=1^{b+j}c1^{s-b-j}0^s,
\qquad 0\le j\le s-b.
\tag{6.4}
$$

For \(j<s-b\), if a prefix of \(c\) reached the global height \(s\), the
canonical first maximum would be a core up-step. The corresponding PBBS
omitted coordinate would be a core label, contradicting the fixed-core
hypothesis. Hence

$$
b+j+\maxpref(c)<s
\qquad(0\le j<s-b).
\tag{6.5}
$$

Taking \(j=s-b-1\) and using integrality gives (6.2). Balanced
nonpositive-prefix words are complements of Dyck words. \(\square\)

The factor in (6.3) is exactly the one missing from the common-shell
pigeonhole obstruction:

$$
\frac{q\operatorname{Cat}_q}{\binom{2q}{q-1}}=1.
\tag{6.6}
$$

This only says that the forced lower bound on load is no longer growing;
it does not itself construct a bounded-load completion.

Theorem 6.1 is special to a contiguous carrier. A general deletion
assertion is false. The word

$$
D_0=1100111000
\tag{6.7}
$$

is a genuine \(r=5,s=3\) zero-winding root. Direct block rotation gives

$$
(d_0,d_1,d_2)=(1,1,5),\qquad
(\delta_0,\delta_1,\delta_2,\delta_3)=(7,3,3,7),
\tag{6.8}
$$

and \(1+1+5=7=\delta_3\). Rooting at \(u=0\), its active positions are

$$
\{a_0,a_1,a_2,a_3\}=\{0,10,9,4\},\qquad
\{b_0,b_1,b_2\}=\{7,2,1\}.
\tag{6.9}
$$

Deleting them leaves the rooted core word

$$
0110,
\tag{6.10}
$$

which is not Dyck in that inherited cut; only its cyclic rotation \(1100\)
is Dyck. Thus a genuine interlaced return can move the valid core cut.

## 7. The nested equations and the exact surviving theorem

For a genuine return write

$$
d_h=|S_h|+1,\qquad e_h=|T_h|+1,
$$

$$
C_h=\sum_{t<h}d_t,\qquad
M_h=\sum_{t=h}^{s-1}e_t.
$$

The active labels are the ordinary nonwrapping lifts

$$
a_h=u-C_h,\qquad b_h=u+M_h.
\tag{7.1}
$$

Moreover,

$$
d_0=e_{s-1}=1,\qquad
\operatorname{ht}(S_h)\le h,\qquad
\operatorname{ht}(T_h)\le s-1-h.
\tag{7.2}
$$

The increments \(d_h,e_h\) are positive odd integers, and

$$
\delta_h=C_h+M_h,\qquad
s\le \delta_h\le N-1-s.
\tag{7.3}
$$

Internal label simplicity also requires
\(C_p+M_\ell\ne N\) for every internal even/odd pair. These scalar tests
are still not enough. The complete chronology contains simultaneous
nested word equations

$$
L_hR_0=R_h\mathcal D_h,
\tag{7.4}
$$

where

$$
L_h=(\overline T_{h-1}0)\cdots(\overline T_00),
\qquad
\mathcal D_h=(0S_h)\cdots(0S_1).
\tag{7.5}
$$

There is a narrow common-bridge no-go. Put

$$
\mathcal C_{h+1}=(0S_{s-1})\cdots(0S_{h+1}),
\qquad 0\le h<s.
$$

In the ansatz
\(R_h=L_h\mathcal E\mathcal C_{h+1}\), where the same balanced word
\(\mathcal E\) is inserted intact at every nested level, the two extreme
canonical cuts force every prefix sum of \(\mathcal E\) to be both
nonpositive and nonnegative. Hence \(\mathcal E\) is empty. Long overlap
can therefore evade this ansatz only through literal interlacing across
the \(T\)- and \(S\)-block borders.

This interlacing has an exact scalar size. Let

$$
\Lambda=\delta_0+\delta_s-2r=2t\ge0,
\tag{7.6}
$$

and let \(O\) be the compulsory overlap between

$$
(\overline T_{s-1}0)\cdots(\overline T_00)
\quad\text{and}\quad
(0S_s)(0S_{s-1})\cdots(0S_1).
$$

Then

$$
|O|=\Lambda+|S_s|+1,
$$

and, literally,

$$
O=(0S_s)\mathcal B,
\tag{7.7}
$$

where \(\mathcal B\) is the next \(2t\) letters of
\((0S_{s-1})\cdots(0S_1)\). Since both \(O\) and \(0S_s\) have net
height \(-1\), the interlaced word \(\mathcal B\) is balanced. Thus
positive endpoint excess is exactly a balanced word embedded across
block borders, not a freely insertable carrier.

The remaining positive statement can now be made exactly.

> **PBBS cross-active completion congestion — UNPROVED.** For every fixed
> \(A>0\), every full deck lift of a quotient-edge-disjoint family of genuine
> zero-winding PBBS returns with
> \(s\le H_A=\lceil A\sqrt r\rceil\) satisfies either
>
> $$
> \sup_X\Lambda_X=O_A(1)
> \tag{7.8}
> $$
>
> for the reciprocal-binomial kernel, or at least
>
> $$
> \Delta(\mathcal P)=O_A(1)
> \tag{7.9}
> $$
>
> for the selected first shells.

Either (7.8) or (7.9) proves
\(\overline\nu_{H_A}^{\,0}=O_A(B/N)\) by Theorem 3.1 or (4.5).

The contiguous calculation suggests a sharper cut/cluster form. If the
interlaced overlap fixes one valid cut of the balanced core word, the
cycle lemma gives the Catalan factor \(1/(q+1)\). If the valid cut moves,
one must prove that the corresponding returns are nearby
\(\tau\)-shifts on one quotient cycle and hence cannot all survive an
edge-disjoint packing. This dichotomy remains unproved.

## 8. Independent audit and implication scope

The decisive steps were audited independently.

1. The tail formulas, reciprocal-binomial probabilities, first-shell
   multiplicity, and exact transversal \(q\) were separately rederived.

2. The shell incidence proof was checked in both directions. The one
   excluded predecessor gives exact degree \(r\), not \(r+1\).

3. The strip-walk eigenvalue factor \(2/b\), complementary-pair pruning,
   and load ratio (5.9) were checked independently.

4. Both endpoint roots in (5.5) are canonical primitive Dyck roots of
   exact height \(s\) with \(d=1\); the audit also confirmed that this
   does not establish intermediate PBBS chronology.

5. The no-overtaking proof was checked from the literal block-rotation
   formula. The genuine example (6.7)--(6.10) independently rules out
   extending its fixed-cut conclusion to all returns.

The proved/conditional boundary is

$$
\boxed{
\begin{array}{rcl}
\text{factorial completion gain}
 &:& \text{refuted; exact robust capacity }q,\\
\text{bounded load from owner and endpoints}
 &:& \text{refuted by an }\Omega_A(q)\text{ family},\\
\text{contiguous intermediate chronology}
 &:& \text{exact Catalan loss proved},\\
\text{interlaced genuine chronology}
 &:& \text{open},\\
\text{zero-winding }CP_A
 &:& \text{open},\\
\text{coefficient one}
 &:& \text{not claimed}.
\end{array}
}
$$
