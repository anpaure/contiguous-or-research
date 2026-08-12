# Unseeded ordinary frames: higher-codegree geometry, the finite pair-column cutoff, and the exact residual wall

Date: 2026-07-27

Scope: the ordinary promotion-frame owner-resolution hypergraph.  All
arguments are purely combinatorial.

## 0. Audited conclusion

Put

\[
 n=2m,\qquad M=m+H,\qquad r=M+1,
 \qquad H=(1+o(1))\sqrt{m\log m},
\]

and let an edge be one rank-\(M\) top together with the \(M\) cyclic
rank-\(m\) windows of an order on that top.  Let

\[
 D={m!^2\over(m-H)!},\qquad R=(M-1)!
\]

be the owner and top degrees.  At the calibrated scale
\(D/R=1-o(1)\).

The following boundary is rigorous.

1.  For \(2\le s\le L=o(H)\), every \(s\)-owner codegree satisfies

    \[
    {\Delta_s\over D}
    \le
    \left({C(s-1)^2\over m^2}\right)^{s-1}.                 \tag{0.1}
    \]

    The exponent is optimal: a monotone consecutive chain of \(s\)
    owners has relative codegree

    \[
                         {2\over(m)_{s-1}^2}.               \tag{0.2}
    \]

2.  The full cyclic geometry is stronger than the maximum pair
    codegree.  For two fully equality-resolved frame arms, after their
    already common resources have been removed from the union deficit,
    the number of new catalogue frames meeting both arms is

    \[
                              O(D/m).                       \tag{0.3}
    \]

    Since a free event column has mass \((1+o(1))rD\), the time-zero
    common-event clock mass is \(O(m^{-2})\), not merely the
    \(O(m^{-1})\) obtained from \(r\Delta_2/D\).

3.  A corrected ordered pair-column tower needs no infinite initializer.
    If it is initialized through

    \[
                              B=C_0(\log m)^2               \tag{0.4}
    \]

    and every current equality-resolved arm pair has common-event clock
    mass

    \[
             {(\log m)^{O(1)}\over m^2u(t)^2},
    \]

    its finite backward potential loses only

    \[
       \exp[-\Theta((\log m)^3)].                           \tag{0.5}
    \]

    The exact static range required for a base excess \(s\) is

    \[
                              2(s+B)\le L_{\rm pm}.          \tag{0.6}
    \]

4.  The pointwise current bound in item 3 is not hereditary under
    arbitrary edge deletion.  There is a literal ordinary-frame
    subhypergraph of maximum degree two containing two arms and
    \(cm\) pairwise disjoint further frames, every one of which meets
    both arms.  Its normalized common-event mass is bounded below by a
    positive absolute constant.

5.  This last construction is **not** a near-factor or Hall obstruction.
    Its \(cm\) common frames themselves form a matching and cover all
    but \(O(m)\) of the \(\Theta(m^2)\) vertices in the displayed
    residual.  The residual is also obtained by arbitrary edge deletion,
    not proved to be a vertex-induced state of the random greedy
    trajectory.  Thus the ordinary near-resolution remains open.

Consequently the finite-cutoff algebra passes, while the proposed
static-to-dynamic inference fails.  The exact surviving statement is an
incidence-weighted, trajectory-specific whole-arm common-event estimate
(HCE/ADLE), with an \(o(W)\) quarantine allowance.  The later
``additive one-child'' note does not bypass this statement: its stopped
current one-row path-mesh bound is the same missing dynamic input.

## 1. Exact higher codegrees

Fix an owner \(X\).  A frame through \(X\) has the unique rooted form

\[
 (A;x_1,\ldots,x_m;a_1,\ldots,a_H),
 \qquad A\in\binom{[2m]\setminus X}{H},                    \tag{1.1}
\]

with cyclic order
\(x_1\cdots x_m a_1\cdots a_H\).  This gives the degree \(D\).
For an owner \(Y\) with \(d_J(X,Y)=d<H\), membership in the deck means
that its leaving and entering sets are respectively the first \(d\)
positions of the two displayed orders, or respectively the last \(d\)
positions.

For \(t=s-1\) prescribed owners, choose their two shores and collect the
positive successive gap sizes on both shores.  If their total is \(k\),
the exact fraction of rooted descriptions for one admissible shore
assignment is

\[
 \left({(m-k)!\prod_j g_j!\over m!}\right)^2.              \tag{1.2}
\]

For \(k\ge t\),

\[
 { (m-k)!\prod_jg_j!\over m!}
 \le {k!\over(m)_k}
 ={1\over\binom mk}
 \le\left({2t\over m}\right)^t.                          \tag{1.3}
\]

There are at most \(2^t\) shore assignments.  If opposite boundary
pieces cover the entire \(H\)-set, or an owner has distance \(H\), the
top extension is forced; this costs at most
\(2^tM/\binom mH\), which is smaller than the right side below because
\(t=o(H)\).  Hence

\[
 {d(X,Y_1,\ldots,Y_t)\over D}
 \le\left({Ct^2\over m^2}\right)^t,                       \tag{1.4}
\]

which is (0.1).  Taking nested one-step prefix sets on one shore gives
\(((m-t)!/m!)^2=(m)_t^{-2}\); the two shores are disjoint, proving
(0.2).

The same proof with a compatible top fixed replaces the second \(m\)-order
by an \(H\)-order and gives

\[
 {d(U;X,Y_1,\ldots,Y_t)\over m!H!}
 \le\left({Ct^2\over mH}\right)^t.                        \tag{1.5}
\]

These are genuine all-fixed-order estimates through any prescribed
\(L=o(H)\); they do not assert heredity after endogenous restriction.

## 2. The sharp time-zero common-event bound

We first record a useful elementary fact.

### Lemma 2.1 (distinct-top deck intersection)

If two frames have distinct tops, their owner decks have at most \(H\)
common vertices.

#### Proof

Let the tops be \(U\ne V\), and choose \(a\in U\setminus V\).  Every
owner common to the two decks is contained in \(V\), hence omits \(a\).
In a cyclic order on \(U\), exactly \(H=M-m\) of the \(M\) length-\(m\)
windows omit a prescribed coordinate.  \(\square\)

For the common-event count one needs a stronger weighted statement.
Fix an owner \(X\) and a frame \(G=F(V,\pi)\).  Put
\(a=|X\setminus V|\).  If an owner \(Y\) in the deck of \(G\) has
\(d_J(X,Y)=d<H\), write \(Y=V\setminus B\), where \(B\) is a cyclic
\(H\)-interval.  Comparing any two valid intervals shows that their
starts differ by at most \(2d-a\).  Therefore

\[
 \#\{Y\in\mathcal O(G):d_J(X,Y)=d\}\le4d-2a+1\le4d+1.    \tag{2.1}
\]

Using the exact pair-codegree table,

\[
 {d(X,Y)\over D}=
 \begin{cases}
 2\binom md^{-2},&1\le d<H,\\
 (m-H+1)\binom mH^{-2},&d=H,
 \end{cases}                                             \tag{2.2}
\]

we obtain, uniformly in \(X,G\),

\[
 \sum_{Y\in\mathcal O(G),\,Y\ne X}d(X,Y)
 \le {CD\over m^2}.                                      \tag{2.3}
\]

Now let \(F,G\) be two physical arms.  First quotient every owner and
top already shared by the arms; those resources occur once in the
physical union reference and produce no positive pair correction.
Sum (2.3) over the at most \(M\) remaining owners of \(F\).  The two
top--owner orientations contribute at most

\[
 2Mm!H!={2MD\over\binom mH}=o(D/m),                       \tag{2.4}
\]

and two distinct tops have codegree zero.  Thus the number of genuinely
new edge events hitting both quotient arms is \(O(D/m)\), proving
(0.3).  This proof applies whether the original arms were disjoint or
shared a protected center; equality resolution is the relevant
hypothesis.

## 3. Exact finite-cutoff accounting

Let \(F_0,\ldots,F_B\) be the transported tower observables and suppose

\[
 (\partial_t+\mathcal L_t)F_j\le\kappa(t)F_{j+1}
 \quad(0\le j<B),                                        \tag{3.1}
\]

while the cutoff state satisfies

\[
 (\partial_t+\mathcal L_t)F_B\le q(t)F_B.                \tag{3.2}
\]

Put \(A(t)=\int_t^{t_1}\kappa\), \(Q=\int_{t_0}^{t_1}q\).  Backward
variation of constants gives a nonnegative supermartingale whose initial
expectation is at most

\[
 C\alpha^s\left[
  \sum_{j<B}{(A\alpha)^j\over j!}
  +e^Q{(A\alpha)^B\over B!}
 \right],                                                \tag{3.3}
\]

provided \(\mathbb EF_j(t_0)\le C\alpha^{s+j}\) for \(j\le B\).

At level \(B\), core compression leaves
\(p=O(s+B)=O((\log m)^2)\) nonprivate marginal arms.  If every pair has
current common-event clock mass \(\beta_m\), the exact union-deficit
bound

\[
                         (t-1)_+\le\binom t2              \tag{3.4}
\]

gives

\[
                         q(t)\le\binom p2\beta_m.          \tag{3.5}
\]

For \(z=m^{-1/20}\),

\[
 T=O(m\log m),\qquad
 \alpha={m^{-2+o(1)}\over z^2}=m^{-19/10+o(1)}.           \tag{3.6}
\]

The sharp sufficient current estimate is

\[
 \beta_m(t)\le {(\log m)^{O(1)}\over m^2u(t)^2}.           \tag{3.6a}
\]

Since \(u(t)\ge z\), equations (3.5)--(3.6a) give

\[
 Q=m^{-9/10+o(1)},\qquad A\alpha=m^{-9/10+o(1)}.          \tag{3.7}
\]

Taking \(B=C_0(\log m)^2\) proves (0.5).  Notice that the maximum pair
codegree alone gives only \(\beta_m=O(m^{-1})\); after the \(p^2\)
arm-pair multiplicity this would give \(Q=O((\log m)^5)\), too large
for the \(\Theta((\log m)^3)\) cutoff credit.

Finally, a core of excess \(s+j\) can have \(2(s+j)\) nonprivate
witness incidences.  Therefore the static initializer really requires
(0.6).  Fixing the formal row set does not remove this order condition.

## 4. Literal failure of deletion-hereditary HCE

Choose \(|C|=M-1\), labels \(a,b\notin C\), and tops

\[
                         U=C\cup\{a\},\qquad
                         U'=C\cup\{b\}.                   \tag{4.1}
\]

Use aligned cyclic orders, replacing \(a\) by \(b\) in the same
position.  The \(m\) windows containing that position give pairs
\((Y_i,Z_i)\) at Johnson distance one.  The other \(H\) windows are
common to the two frame arms \(f,f'\).

The exact distance-one link has size

\[
                         D_1={2D\over m^2}.                \tag{4.2}
\]

Any third owner or top vertex belongs to at most

\[
                         {20D_1\over(m-1)^2}               \tag{4.3}
\]

members of that link.  For owners this follows because three owners in
one cyclic deck cannot be pairwise Johnson-adjacent, and the distance-two
pair codegree is \(4D_1/(m-1)^2\); the distance-\(H\) boundary is
smaller.  For a top, fixing one of the
\(\binom{m-1}{H-1}\) compatible tops gives an even smaller fraction.

Greedily, for \(\ell=\lfloor m/100\rfloor\), choose a frame \(g_i\)
through \(Y_i,Z_i\), avoiding all vertices of previous \(g_j\)'s, all
other designated endpoints, and all vertices of \(f\cup f'\) except
\(Y_i,Z_i\).  Before step \(i\) there are at most
\((1/50+o(1))m^2\) forbidden vertices.  Equation (4.3) excludes less
than the whole \(D_1\)-link, so the choice exists.

The \(g_i\)'s are pairwise disjoint, and \(g_i\) meets \(f\) only at
\(Y_i\) and \(f'\) only at \(Z_i\).  In the subhypergraph

\[
                         \{f,f',g_1,\ldots,g_\ell\},       \tag{4.4}
\]

the maximum degree is two, while at least \(\ell\) edges meet both
\(f,f'\).  Hence

\[
 {\#\{g:g\cap f\ne\varnothing,\ g\cap f'\ne\varnothing\}
  \over r\Delta}
 \ge {\ell\over2r}=\Omega(1).                            \tag{4.5}
\]

This remains true after quotienting the \(H\) owners common to
\(f,f'\): every \(g_i\) uses the exclusive pair \(Y_i,Z_i\).

## 5. Why this is not the requested near-factor obstruction

Let \(V_*\) be the union of the vertices in (4.4).  The matching
\(\{g_1,\ldots,g_\ell\}\) covers \(\ell r\) vertices.  All uncovered
vertices lie in \(f\cup f'\), so there are at most \(2r\) of them.
Consequently

\[
 { |V_*\setminus\bigcup_i g_i|\over|V_*|}
 \le {2r\over\ell r}=O(1/m).                              \tag{5.1}
\]

Thus the explicit HCE counterstate has a near-perfect matching on its
own support.  It is a no-go for a deterministic hereditary tower lemma,
not a Hall-deficient catalogue.  Nor has (4.4) been shown to equal the
vertex-induced residual of a legal matching trajectory.

The even sharper fixed-pair core consisting of all frames through one
Johnson-adjacent pair has identical owner stars and matching number one,
but all its edges share those two owners.  It therefore has no
near-perfect fractional point and is likewise not a macroscopic
obstruction to the original regular catalogue.

The exact unresolved positive statement is therefore:

> Along the actual compensated ordinary-frame trajectory, after an
> incidence-weighted quarantine of \(o(W)\) owners and the corresponding
> \(o(N)\) tops, every equality-resolved arm pair occurring in the
> corrected cutoff hierarchy has common-event clock mass
> \(m^{-2}u(t)^{-2}(\log m)^{O(1)}\) in aggregate.
> **(HCE)**

This is HCE/ADLE.  Static degrees, the complete finite higher-codegree
table, and binary edge monotonicity do not prove it.  Conversely, (5.2)
and the certified initializer range (0.6) make the finite tower close by
Section 3.  No ordinary-frame near-resolution or coefficient-one theorem
is claimed here.

## 6. Pair-resolved odd cuts are quantitatively too small

The preceding residual is not an odd-set obstruction.  In fact every
obstruction which survives only in a pair resolution is too small at the
physical codegree scale.

### Theorem 6.1 (bounded-atom fractional matchings have small deficiency)

Let \(G=(S,E)\) be a finite graph with a fractional perfect matching
\(y\), so

\[
 \sum_{e\ni v}y_e=1\quad(v\in S),\qquad
 0\le y_e\le\rho.                                        \tag{6.1}
\]

Then

\[
                         |S|-2\nu(G)\le\rho|S|.           \tag{6.2}
\]

#### Proof

By Tutte--Berge, the left side of (6.2) is

\[
 \max_{A\subseteq S}\bigl(q(G-A)-|A|\bigr),              \tag{6.3}
\]

where \(q\) counts odd components.  Fix \(A\).  If an odd component
\(C\) of \(G-A\) has \(c=|C|\le1/\rho\), then

\[
 y(C,A)=c-2y(E(C))
 \ge c-\rho c(c-1)\ge1.                                  \tag{6.4}
\]

The total \(y\)-mass leaving \(A\) is at most \(|A|\), so there are at
most \(|A|\) such small odd components.  Every remaining odd component
has more than \(1/\rho\) vertices, and hence there are at most
\(\rho|S|\) of them.  Therefore
\(q(G-A)-|A|\le\rho|S|\).  Maximize over \(A\).  \(\square\)

For the physical application, let a **saturated pair resolution** assign
each uniformly weighted frame one charged owner pair, fractionally if
necessary, while giving every charged owner its full uniform load
\(\lambda=D/R\).  If \(S\) is the charged owner set and
\(\theta_{F,p}\) are the assignment coefficients, the defining
identities are

\[
 \sum_{p\subseteq F}\theta_{F,p}=1,\qquad
 {1\over R}\sum_{F\ni v}\sum_{p\ni v}\theta_{F,p}
 =\lambda\quad(v\in S).                                  \tag{6.5a}
\]

Summing the second identity over \(v\) and using the first forces

\[
 \lambda|S|=2N,\qquad |S|={2N\over\lambda}={2W\over M}.   \tag{6.5}
\]

The projected edge weights

\[
 y_p={1\over\lambda R}\sum_F\theta_{F,p}                  \tag{6.6}
\]

form a fractional perfect matching on \(S\).  Since
\(\theta_{F,p}\le1\) and \(\lambda R=D\), the exact physical
pair-codegree table gives

\[
                         y_p\le {d(p)\over D}\le {2\over m^2}. \tag{6.7}
\]

Theorem 6.1 and (6.5) imply

\[
 \nu(G)\ge {W\over M}-{2W\over Mm^2}.                     \tag{6.8}
\]

The target frame count is \(N=\lambda W/M\le W/M\).  Hence a graph
odd-set certificate in this saturated pair projection can force at
most

\[
                         {2W\over Mm^2}=O(W/m^3)           \tag{6.9}
\]

missing frames, and therefore at most \(2W/m^2=o(W)\) additional
missing owners.

This does **not** lift the graph matching to disjoint physical frames:
representing frames can still collide in their uncharged owners or
tops.  Its exact force is negative.  A macroscopic near-factor
obstruction cannot consist solely of bounded odd cycles, domino pairs,
or another saturated pair-resolved Tutte cut while retaining the
ordinary normalized pair-codegree scale.  Any genuine obstruction must
live in the higher-order frame lift, in exterior physical collisions, or
in a trajectory-induced concentration which destroys (6.7).
