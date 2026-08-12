# Hash-twisted Chung--Feller rows: the exact Latin system and the hereditary excursion cocycle obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let \(D_m\) be the Catalan set of Dyck roots and

\[
        X_t(u)=f^t(u),\qquad u\in D_m,\quad 0\le t\le m,
\]

the canonical MSW/Chung--Feller layers. A hash does not by itself define
a new exact factor. If

\[
        \chi:D_m\longrightarrow A
\]

is a hash and \(g_{t,a}\in\operatorname {Sym}(D_m)\) is the phase-\(t\),
hash-\(a\) option, put

\[
        p_t(u)=g_{t,\chi(u)}u.                                      \tag{0.1}
\]

The phase-\(t\) lower states are owned once each if and only if

\[
        \{g_{t,a}(\chi^{-1}(a)):a\in A\}                            \tag{0.2}
\]

partitions \(D_m\). Full exactness additionally requires Johnson
adjacency, the aggregate upper-colour bijection, and zero endpoint
monodromy. These conditions are exact and integral.

The decisive obstruction is independent of the entropy or locality of
the hash. Consider a length-\(r\) recursive excursion on a coordinate
block \(J\), \(|J|=2r\), whose left local port is
\(P_u\in\binom Jr\) and whose right local port is
\(J\setminus P_{\tau u}\). If its exterior endpoint sets are
\(O_L(u),O_R(u)\), then geodesicity gives

\[
 \boxed{|O_L(u)\setminus O_R(u)|
              =|P_u\setminus P_{\tau u}|}                         \tag{0.3}
\]

and the local contribution to a window swallowing the whole excursion is
exactly

\[
 \boxed{\Phi(u)=
   \bigl(O_L(u)\cap O_R(u)\bigr)\mathbin{\dot\cup}
   \bigl(P_u\setminus P_{\tau u}\bigr).}                           \tag{0.4}
\]

Thus a fixed common exterior forces \(\tau=1\) and makes \(\Phi\)
constant. More generally, a closed recursive child-order twist has zero
local monodromy; it can break blindness only by making its stationary
exterior collar genuinely filling-dependent.

There is a quantitative hash-alphabet no-go. Put

\[
 p=2m+1,\qquad W=\binom{2m+1}{m}=p\operatorname {Cat}_m,
\]

and suppose that at every aligned size-\(r\) context the swallowed target
map (0.4) has at most \(M\) values. Choose \(r\) minimally with

\[
                  \operatorname {Cat}_r\ge4pM.                    \tag{0.5}
\]

Then, at every boundary-served depth \(r\le q\le m/2\),

\[
 \boxed{
 K_{q,p}:=\sum_T(\mu_q(T)-p)_+
 \ge {H_{m,r}\over2}\bigl(\operatorname {Cat}_r-2pM\bigr)
 \ge {H_{m,r}\operatorname {Cat}_r\over4},}                       \tag{0.6}
\]

where

\[
                  H_{m,r}={1\over2}\binom{2(m-r)}{m-r}.            \tag{0.7}
\]

Uniformly for \(r=o(m)\),

\[
 {H_{m,r}\operatorname {Cat}_r\over W}
       ={1+o(1)\over4\sqrt\pi\,r^{3/2}}.                           \tag{0.8}
\]

Consequently any hash-pure collar twist with

\[
                  \log(pM)=o(m^{1/5})                             \tag{0.9}
\]

has a non-\(o(W)\) aggregate shallow missing-target defect. This includes
every fixed, polynomial, or \(\exp(o(m^{1/5}))\)-size hash alphabet when
the swallowed target depends only on the hash value.

This does not rule out an arbitrary globally braided Chung--Feller
factor. It isolates its exact escape condition: on a positive mass of
logarithmic-size contexts, rows sharing one hash value must nevertheless
acquire many different values of (0.4). This requires either nontrivial
boundary monodromy with the exactly matched exterior displacement (0.3),
or filling-dependent stationary collars crossing a parent seam. A
recursive choice among fixed-port internal interleavings does neither.

## 1. The exact hash--Latin ownership equations

Let

\[
                  D=D_m,\qquad D_a=\chi^{-1}(a).
\]

At phase \(t\), choose \(g_{t,a}\in\operatorname {Sym}(D)\) for each
\(a\in A\), and define \(p_t\) by (0.1).

### Lemma 1.1 (hash--Latin section)

The map \(p_t:D\to D\) is a bijection if and only if

\[
                  D=\mathbin{\dot\bigcup}_{a\in A}g_{t,a}D_a.     \tag{1.1}
\]

Equivalently, for every \(v\in D\),

\[
       \#\{a\in A:\chi(g_{t,a}^{-1}v)=a\}=1.                       \tag{1.2}
\]

#### Proof

The image of \(p_t\) on \(D_a\) is exactly \(g_{t,a}D_a\). Since the
\(D_a\) partition \(D\), \(p_t\) is bijective exactly when these images
partition \(D\). A point \(v\) lies in \(g_{t,a}D_a\) precisely when
\(g_{t,a}^{-1}v\in D_a\), proving (1.2). \(\square\)

Suppose now \(A=\{0,1\}\), and put

\[
                  \theta_t=g_{t,0}^{-1}g_{t,1}.
\]

### Corollary 1.2 (binary orbit condition)

The phase map \(p_t\) is bijective if and only if \(D_1\) is invariant
under \(\theta_t\), equivalently \(\chi\) is constant on every orbit of
\(\langle\theta_t\rangle\).

#### Proof

After applying \(g_{t,0}^{-1}\), (1.1) becomes

\[
                  D_0\mathbin{\dot\cup}\theta_tD_1=D.
\]

Since \(D_0=D\setminus D_1\), this is equivalent to
\(\theta_tD_1=D_1\). \(\square\)

Use the canonical layer bijections

\[
                  i_t:D\longrightarrow L_t,\qquad i_t(u)=X_t(u),
\]

and define

\[
                  X'_t(u)=X_t(p_tu).                              \tag{1.3}
\]

### Theorem 1.3 (necessary and sufficient phase-respecting test)

The rows (1.3) form an exact rooted Chung--Feller factor if and only if
all four conditions below hold.

1. For every \(t\), the hash--Latin partition (1.1) holds.
2. For every \(u\) and \(0\le t<m\),

   \[
   |X_t(p_tu)\mathbin\triangle X_{t+1}(p_{t+1}u)|=2.               \tag{1.4}
   \]

3. The upper colours form the exact multiset

   \[
   \mathbin{\dot\bigcup}_{t=0}^{m-1}
   \mathbin{\dot\bigcup}_{u\in D}
   \{X_t(p_tu)\cup X_{t+1}(p_{t+1}u)\}
       =\binom{[2m]}{m+1}.                                        \tag{1.5}
   \]

4. The endpoint monodromy vanishes:

   \[
                              p_m=p_0.                             \tag{1.6}
   \]

After a common relabelling of rows one may take \(p_0=p_m=1\).

#### Proof

At phase \(t\), the states \(X_t(v)\), \(v\in D\), are exactly the
Chung--Feller layer \(L_t\). They occur once each in (1.3) exactly when
\(p_t\) is a bijection, which is Lemma 1.1. This is the complete
lower-state ownership ledger.

Condition (1.4) is Johnson adjacency. Condition (1.5) says every
\((m+1)\)-set is used once as an adjacent union; after the standard
complement-and-adjoin-\(\infty\) operation, this is precisely the
other-shore ownership ledger.

Finally the canonical endpoint identity is

\[
                 X_m(v)=[2m]\setminus X_0(v).
\]

The terminal state of row \(u\) is therefore complementary to its
initial state if and only if \(X_0(p_mu)=X_0(p_0u)\). Injectivity of
\(X_0\) gives (1.6). The conditions are also sufficient. \(\square\)

Put

\[
                  \sigma_t=p_{t+1}p_t^{-1}.
\]

Then

\[
        \sigma_{m-1}\sigma_{m-2}\cdots\sigma_0=p_mp_0^{-1}.        \tag{1.7}
\]

This is the exact row-interleaving cocycle. A nonconstant hash does not
make the product nontrivial: complementary endpoint closure forces the
root-scale product to be the identity. Nor do the Latin equations imply
the upper ledger (1.5); both ledgers must be checked.

## 2. Boundary monodromy determines a swallowed target

The next theorem does not assume the canonical MSW recursion or fixed
Chung--Feller layers.

Let \(J,E\) be disjoint coordinate sets, \(|J|=2r\), and let

\[
        u\longmapsto P_u\in\binom Jr
\]

be injective. Let \(\tau\) be a permutation of the row labels. Suppose a
contiguous length-\(r\) segment in row \(u\) has endpoints

\[
 Z_0(u)=O_L(u)\mathbin{\dot\cup}P_u,\qquad
 Z_r(u)=O_R(u)\mathbin{\dot\cup}(J\setminus P_{\tau u}),           \tag{2.1}
\]

where \(O_L(u),O_R(u)\subseteq E\) have the same cardinality. Assume the
segment is a Johnson geodesic. This is automatic when it is a subpath of
a length-\(m\) Johnson path joining complementary \(m\)-sets.

### Theorem 2.1 (geodesic boundary-cocycle identity)

For every \(u\),

\[
 |O_L(u)\setminus O_R(u)|=|P_u\setminus P_{\tau u}|,               \tag{2.2}
\]

and

\[
 \bigcap_{t=0}^r Z_t(u)
 =\bigl(O_L(u)\cap O_R(u)\bigr)\mathbin{\dot\cup}
   \bigl(P_u\setminus P_{\tau u}\bigr).                            \tag{2.3}
\]

In particular:

* if \(O_L(u)=O_R(u)\), then \(P_{\tau u}=P_u\), hence \(\tau u=u\);
* if the same exterior \(O\) is used for every filling \(u\), the full
  excursion intersection is the common target \(O\);
* a nonidentity boundary braid is possible only with exactly matching
  exterior Hamming displacement.

#### Proof

Johnson distance between equal-size sets is the number of coordinates
present in the first and absent from the second. From (2.1),

\[
\begin{aligned}
 d_J(Z_0(u),Z_r(u))
 &=|O_L(u)\setminus O_R(u)|
   +|P_u\setminus(J\setminus P_{\tau u})|\\
 &=|O_L(u)\setminus O_R(u)|+|P_u\cap P_{\tau u}|.                  \tag{2.4}
\end{aligned}
\]

The path has geodesic length \(r\), so (2.4) equals \(r\). Since

\[
 |P_u\cap P_{\tau u}|=r-|P_u\setminus P_{\tau u}|,
\]

equation (2.2) follows.

On a Johnson geodesic, every coordinate common to the endpoints stays
present throughout. Otherwise it would be deleted and later reinserted,
using two moves which do not reduce the endpoint distance. Conversely
every coordinate in the full intersection belongs to both endpoints.
Thus the intersection of the segment equals \(Z_0(u)\cap Z_r(u)\), and
(2.3) follows. If \(O_L(u)=O_R(u)\), (2.2) and injectivity of
\(u\mapsto P_u\) give \(\tau u=u\). \(\square\)

Theorem 2.1 distinguishes two notions.

1. **Motion along one row:** \(O_L(u)\ne O_R(u)\). This is forced by a
   nontrivial local boundary monodromy.
2. **Variation between fillings:** even when
   \(O_L(u)=O_R(u)=O(u)\), the stationary collar \(O(u)\) may vary with
   \(u\).

The first is a cross-parent braid. The second is a context-dependent
placement of a closed excursion. Either can break blindness. A fixed
common-exterior substitution has neither.

## 3. Closed recursive hash twists remain blind

Consider an aligned one-hole context \(C[\ ]\) with a hole on block
\(J\), and fillings \(u\in D_r\). Suppose a recursive rule, possibly
using the entire ambient word \(C[u]\), changes the internal chronology
but has these sealed-context properties.

1. The excursion has exactly \(r\) Johnson moves on every row.
2. It begins at \(O_C\cup P_u\) and ends at
   \(O_C\cup(J\setminus P_u)\), with the same \(O_C\) for all \(u\).
3. Outside the excursion, the serviced window has a common collar
   intersection \(B_{C,q}\), independent of \(u\).

The internal choice may be an arbitrary function of a nonlocal hash.

### Corollary 3.1 (hash-independent sealed blindness)

Every boundary-served window swallowing the excursion has target

\[
                         B_{C,q}\cup O_C,                         \tag{3.1}
\]

independent of \(u\in D_r\).

#### Proof

The boundary monodromy is the identity and the exterior is common.
Theorem 2.1 gives local intersection \(O_C\). Adjoin the common
outside-window intersection. \(\square\)

This includes every recursive child-order construction which merely
chooses, by a hash, how to interleave exchanges internal to the same node
while retaining that node's fixed complementary ports. Its local
transition permutations may be nontrivial, but their ordered product is
the identity. The argument is hereditary at every descendant node whose
ports and stationary collar remain sealed.

The word “nonlocal” alone gives no escape. A full-word hash can help only
if it changes the boundary data in (2.3), not merely the chronology
between those boundaries.

## 4. The exact target-map escape condition

For a general context, include the outside-window collar and define

\[
 \Phi_{C,q}(u)=B_{C,q}(u)
   \cup\bigl(O_L(u)\cap O_R(u)\bigr)
   \cup\bigl(P_u\setminus P_{\tau_Cu}\bigr),                       \tag{4.1}
\]

where the displayed unions lie in disjoint coordinate blocks. This is
the literal target of the selected swallowed window.

### Proposition 4.1 (one-sided fibre criterion)

Within one context \(C\), the swallowed occurrences have pointwise load
at most \(B\) if and only if

\[
                  \max_T|\Phi_{C,q}^{-1}(T)|\le B.                 \tag{4.2}
\]

#### Proof

There is one swallowed occurrence for each \(u\in D_r\), and its target
is (4.1). Its multiplicity at \(T\) is therefore exactly
\(|\Phi_{C,q}^{-1}(T)|\). \(\square\)

Equation (4.1) displays the only three mechanisms available to this
class:

* a filling-dependent outside collar \(B_{C,q}(u)\);
* a filling-dependent stationary exterior collar
  \(O_L(u)=O_R(u)\);
* nontrivial boundary monodromy, accompanied by the exterior displacement
  forced by (2.2).

If none occurs, the full Catalan fibre remains. If only \(M\) different
boundary records occur, the fibre is compressed into at most \(M\)
physical targets.

## 5. Quantitative Catalan compression

At lower depth \(q\), let \(\mu_q(T)\) be the number of rooted factor
windows with target \(T\). There are \(W\) occurrences in total. For
\(b\ge1\), put

\[
                         K_{q,b}=\sum_T(\mu_q(T)-b)_+.              \tag{5.1}
\]

For each aligned size-\(r\) context \(C\), boundary service chooses one
length-\(q\) swallowed window at its left or right boundary. Assume that
this context--occurrence incidence has degree at most two: one physical
rooted occurrence is selected by at most two contexts. This is automatic
for the canonical left/right boundary service when the designated
size-\(r\) recursive block remains identifiable and contiguous in the
rooted occurrence, because it must begin at the left window boundary or
end at the right window boundary. It is an explicit hypothesis for an
arbitrary chronology or global braid. There are

\[
                         H_{m,r}={1\over2}
                         \binom{2(m-r)}{m-r}                       \tag{5.2}
\]

contexts.

Write

\[
 n_{C,T}=|\{u\in D_r:\Phi_{C,q}(u)=T\}|,\qquad
 \sum_Tn_{C,T}=d:=\operatorname {Cat}_r.                            \tag{5.3}
\]

### Theorem 5.1 (compressed-fibre cap lower bound)

For every \(b\ge1\),

\[
 \boxed{K_{q,b}\ge {1\over2}\sum_C\sum_T(n_{C,T}-2b)_+.}           \tag{5.4}
\]

If every context target map has image size at most \(M\), then

\[
 \boxed{K_{q,b}\ge {H_{m,r}\over2}(d-2bM)_+.}                      \tag{5.5}
\]

#### Proof

Put \(I_T=\sum_Cn_{C,T}\). Since one physical occurrence is counted in
at most two context families,

\[
                              \mu_q(T)\ge I_T/2.                    \tag{5.6}
\]

Therefore

\[
 K_{q,b}\ge {1\over2}\sum_T(I_T-2b)_+.
\]

For \(x,y,a\ge0\),

\[
                         (x+y-a)_+\ge(x-a)_++(y-a)_+.
\]

Iterating over contexts proves (5.4). If at most \(M\) of the
\(n_{C,T}\) are nonzero, then

\[
 \sum_T(n_{C,T}-2b)_+
 \ge\sum_Tn_{C,T}-2bM=d-2bM.
\]

Summing over all contexts proves (5.5). \(\square\)

The overlap factor two is essential. It explicitly accounts for the two
possible boundary services of one rooted window. For a token-disjoint
context family, \(2b\) may be replaced by \(b\).

### Corollary 5.2 (exact \(p\)-cap obstruction)

Let \(p=2m+1\), and choose \(r\) minimally so that

\[
                         d=\operatorname {Cat}_r\ge4pM.            \tag{5.7}
\]

Then \(d<16pM\), \(r=\Theta(\log(pM+2))\), and, whenever
\(r\le q\le m/2\),

\[
                         K_{q,p}\ge {H_{m,r}d\over4}.               \tag{5.8}
\]

Uniformly for \(r=o(m)\),

\[
 {K_{q,p}\over W}
       \ge {1-o(1)\over16\sqrt\pi\,r^{3/2}}.                       \tag{5.9}
\]

#### Proof

Minimality and
\(\operatorname {Cat}_r/\operatorname {Cat}_{r-1}<4\) give
\(d<16pM\); standard Catalan estimates give
\(r=\Theta(\log(pM+2))\). Equation (5.5), with \(b=p\), and
\(d-2pM\ge d/2\), gives (5.8).

Moreover

\[
\begin{aligned}
 {H_{m,r}d\over W}
 &= {\frac12\binom{2(m-r)}{m-r}\operatorname {Cat}_r
        \over \binom{2m+1}{m}}\\
 &= {1+o(1)\over4\sqrt\pi\,r^{3/2}}
\end{aligned}                                                       \tag{5.10}
\]

uniformly for \(r=o(m)\). Combine (5.8) and (5.10). \(\square\)

## 6. Multidepth consequence

Let

\[
                      N_q=\binom{2m+1}{m-q}
\]

be the number of lower targets at depth \(q\), and

\[
                      M_q=|\{T:\mu_q(T)=0\}|
\]

the number missed. For every nonnegative integral load of total \(W\),

\[
 \boxed{M_q\ge K_{q,p}-(W-N_q).}                                  \tag{6.1}
\]

Indeed,

\[
 K_{q,p}\le\sum_{\mu_q(T)>0}(\mu_q(T)-1)=W-N_q+M_q.                \tag{6.2}
\]

The same lower bound is phase-robust. Let \(\sigma\) be any coordinate
\(p\)-cycle and give every physical row an arbitrary exponent. All
occurrences whose old target was \(T\) then lie among the at most \(p\)
translates \(\{\sigma^aT:a\in\mathbb Z_p\}\). Hence the total number of
covered targets after phasing is at most

\[
 \sum_T\min\{\mu_q(T),p\}=W-K_{q,p}.
\]

If \(M_q^{\rm ph}\) is the resulting missing count, even without assuming
the phased rows remain an exact factor, then

\[
 \boxed{M_q^{\rm ph}\ge K_{q,p}-(W-N_q).}                           \tag{6.2a}
\]

Thus every conclusion below holds both for the hash-twisted seed itself
and after arbitrary cyclic row powers.

For \(q=o(\sqrt m)\), uniformly,

\[
                         {W-N_q\over W}=O(q^2/m).                  \tag{6.3}
\]

Take

\[
                         Q=\left\lfloor{\sqrt m\over r}\right\rfloor.
                                                                         \tag{6.4}
\]

Suppose \(r\to\infty\) and \(r=o(m^{1/5})\). Then
\(2r\le Q=o(\sqrt m)\), and (5.9), (6.1), and (6.3) give

\[
\begin{aligned}
 {1\over W}\sum_{q=2r}^{Q}M_q
 &\ge {1-o(1)\over16\sqrt\pi\,r^{3/2}}(Q-2r)
       -O(Q^3/m)\\
 &= {1-o(1)\over16\sqrt\pi}
       {\sqrt m\over r^{5/2}}.                                    \tag{6.5}
\end{aligned}
\]

The error \(O(Q^3/m)=O(\sqrt m/r^3)\) is smaller than the main term by
\(O(r^{-1/2})\). Under \(r=o(m^{1/5})\), the right side of (6.5)
diverges. Every fixed Gaussian band \(q\le A\sqrt m\) contains the
interval in (6.4) for all sufficiently large \(m\).

### Theorem 6.1 (subexponential hash-pure collar no-go)

Suppose that a hash-twisted recursive factor has boundary-service
incidence degree at most two and, at every aligned size-\(r\) context and
every boundary-served depth, at most \(M=M_m\) different swallowed
targets, where \(r\) is chosen by (5.7). If

\[
                         \log(pM)=o(m^{1/5}),                       \tag{6.6}
\]

then its aggregate missing-target count through every fixed Gaussian band
is not \(o(W)\), before or after arbitrary powers of one ambient
coordinate \(p\)-cycle. Hence it cannot establish coefficient one through
the weak vertical-wreath criterion.

This applies when the stationary collar and all other boundary data
depend only on a hash with at most \(M\) values. The hash may be nonlocal
and the internal row chronology arbitrary.

## 7. Exact escape condition for a recursive seed

The preceding theorem gives a necessary structural alternative. At
logarithmic and mildly growing excursion scales, a successful twist must
make the physical boundary map (4.1) have far more outcomes than its
coarse hash alphabet. On a positive mass of contexts, at least one of the
following must occur.

1. **Filling-dependent stationary collar.** Rows with the same hash value
   place the excursion under different common exterior sets \(O(u)\).
2. **Nonzero local monodromy.** The endpoint pairing is
   \(u\mapsto\tau_Cu\ne u\), and

   \[
   |O_L(u)\setminus O_R(u)|=|P_u\setminus P_{\tau_Cu}|.
   \]

3. **Parent-crossing outside collar.** The serviced window's exterior
   intersection \(B_{C,q}(u)\) varies inside a hash fibre.

In every case, the phase maps must still satisfy the hash--Latin
bijections (1.1), adjacency (1.4), the full upper ledger (1.5), and root
zero monodromy (1.6). A formal recursive permutation is not enough.

The exact pointwise condition is

\[
                 \max_T|\Phi_{C,q}^{-1}(T)|\le B,                  \tag{7.1}
\]

or, allowing the two boundary services and aggregating contexts, the
weaker cap condition

\[
 \sum_C\sum_T
 (|\Phi_{C,q}^{-1}(T)|-2p)_+=o(W)                                 \tag{7.2}
\]

at relevant depths. Formula (5.4) proves that (7.2), or comparable
cross-context cancellation strong enough to imply it, is necessary for
small \(p\)-cap excess.

## 8. Audit and scope

The load-bearing steps were checked as follows.

1. **Distance sign.** In (2.4) the local contribution is
   \(P_u\cap P_{\tau u}\), not \(P_u\setminus P_{\tau u}\). Replacing
   the intersection size by \(r-|P_u\setminus P_{\tau u}|\) gives the
   positive equality (2.2).
2. **Intersection.** Equality of full-path and endpoint intersections
   uses geodesicity. It can fail for a path with detours. Every
   middle-factor row joining complements has minimum possible length, so
   all contiguous subpaths are geodesic.
3. **Two-boundary overlap.** The factor two in (5.4) is retained. No
   global disjointness of aligned context groups is assumed.
4. **Positive-part direction.** The inequality used is
   \((x+y-a)_+\ge(x-a)_++(y-a)_+\), valid for \(x,y,a\ge0\).
5. **Missing versus cap.** Equation (6.1) follows from
   \(K_{q,p}\le W-N_q+M_q\); the direction is correct.
6. **Phase capacity.** Equation (6.2a) counts a union of at most \(p\)
   translates for each old target; overlaps between different old targets
   can only reduce coverage.
7. **Range.** The interval is nonempty under \(r=o(m^{1/4})\). The
   stronger \(r=o(m^{1/5})\) makes the main term in (6.5) diverge.

What is proved:

* the exact hash--Latin and upper-ledger conditions for phase-respecting
  row interleavings;
* the exact boundary-monodromy and swallowed-target formulas;
* blindness for every common-exterior fixed-port recursive twist;
* a quantitative no-go for subexponential hash-pure collar compression;
* the precise boundary-data escape condition.

What is not proved:

* that every nonlocal recursive hash is common-exterior or hash-pure;
* that a general cross-context braid retains boundary-service incidence
  degree two;
* that nonzero local monodromy satisfying (2.2) completes to both exact
  ownership ledgers;
* that a filling-dependent stationary collar cannot have enough physical
  values;
* CPCR, MWB, or coefficient one.

The route is therefore narrowed to a genuinely cross-context construction:
a successful nonconjugate factor must realize a dispersed boundary target
map inside the simultaneous integral \(X/Y\) Latin system. Merely hashing
the choice of a closed MSW interleaving leaves hereditary excursion
blindness intact.
