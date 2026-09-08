# The canonical MSW antipodal factor is not a sparse refinement of the all-zero MW factor

## 1. Outcome

Put

\[
        n=m+1,\qquad C_n=\operatorname {Cat}_n.
\]

Let `H_0` be the all-zero Mütze--Weber dangling-path factor in

\[
        Q_{2n}(n,n+1),
\]

and let `H_CF` be the canonical Mütze--Standke--Wiechert
Chung--Feller factor: for every Dyck word `w` of semilength `n`, it contains
the path

\[
 w=x_0,g(x_0),x_1,g(x_1),\ldots,g(x_{n-1}),x_n=\bar w,
 \qquad x_{i+1}=h(g(x_i)).                         \tag{1.1}
\]

The second factor has exactly the desired target endpoints

\[
 T=\mathcal D_n\mathbin{\dot\cup}\overline{\mathcal D_n}.
\]

It is nevertheless much too far from `H_0` for the sparse signed-`T`-join
program.

### Theorem 1 (super-Catalan support lower bound)

For every `n>=2`,

\[
 \boxed{
 |H_0\mathbin\triangle H_{CF}|\ge 2(n-1)C_n.
 }                                                       \tag{1.2}
\]

Equivalently, in the induction notation `n=m+1`,

\[
 |H_0\mathbin\triangle H_{CF}|\ge 2mC_{m+1}
       =(8+o(1))mC_m.                                   \tag{1.3}
\]

Consequently the literal canonical MSW factor is not an `O(C_m)`-support
signed `T`-join from the published MW factor.  Any bounded-size local-switch
description of this particular transformation needs `Omega(m C_m)`
switches.  Allowing `O(m)`-edge switches can reduce the *number* of switches
to Catalan scale, but not the changed-edge support or the OR seam-halo cost.

The theorem does **not** rule out another complementary path factor at
`O(C_m)` support from `H_0`.  It rules out the cleanest proposed target,
namely replacing `H_0` by the already-antipodal canonical MSW factor.

## 2. The reversed lexical matching inside `H_0`

Let

\[
 R_n=\operatorname {rev}(LM_{2n}(n,n+1))              \tag{2.1}
\]

be the middle matching of the reversed Greene--Kleitman symmetric-chain
decomposition.  Mütze--Weber's relation-to-lexicographic-matchings lemma
gives

\[
                         R_n\subseteq H_0.             \tag{2.2}
\]

The matching saturates rank `n+1`, so

\[
                         |R_n|={2n\choose n+1}=nC_n.   \tag{2.3}
\]

Both path factors have `C_n` components and visit both complete ranks.
Therefore each has

\[
 |H_0|=|H_{CF}|
   ={2n\choose n}+{2n\choose n+1}-C_n
   =2nC_n                                                \tag{2.4}
\]

edges.  The key point is that only Catalan-many edges of `R_n` lie in the
canonical Chung--Feller factor.

## 3. The one-crossing lemma

For a Dyck word `w`, write its first-return decomposition as

\[
                         w=1u0v                        \tag{3.1}
\]

and put `mu(u)=overline{rev(u)}`.  Number the edges of the MSW path (1.1)
from zero.  Define recursively

\[
 a(10v)=1,
 \qquad
 a(1u0v)=1+a(\mu(u))\quad(u\ne\epsilon).             \tag{3.2}
\]

### Lemma 2 (exact reversed-GK crossing)

For every `w in D_n`, the path `P(w)` has exactly one edge in `R_n`, and
that edge has index `a(w)`.

### Proof

The explicit reversed-GK rule says the following.  Match `10` pairs in the
lower word, recursively through already matched blocks.  Equivalently,
reverse the word and use the usual `01` parenthesis matching.  The edge
which flips coordinate `q` upward is in `R_n` precisely when the reversed
coordinate is the first unmatched zero in the reversed lower word.

The MSW flip-coordinate recursion is

\[
 \rho(1u0v)=
 (d,\ d-\rho(\mu(u)),\ 1,\ d+\rho(v)),
 \qquad d=|u|+2.                                      \tag{3.3}
\]

Apply the preceding unmatched-zero test successively to the four blocks in
(3.3).  Parenthesis matching is unaffected by deleting a surrounding
matched `10` block.  The resulting complete block table is

\[
\begin{array}{c|cccc}
 &d&d-\rho(\mu(u))&1&d+\rho(v)\\ \hline
 u=\epsilon&0&\text{empty}&1&0\\
 u\ne\epsilon&0&\text{the }R_{|u|/2}\text{ test}&0&0.
\end{array}                                           \tag{3.4}
\]

For completeness, the middle entry in the second row means literal
coordinatewise equivalence: after deleting the fixed outer matched pair,
the unmatched-zero stack at the edge indexed `1+j` is the stack for the
edge indexed `j` of `P(mu(u))`.  In the other three blocks a fixed unmatched
symbol precedes the flipped coordinate, so that coordinate cannot be the
distinguished reversed-GK zero.  If `u` is empty, that blocker disappears
exactly at the coordinate-`1` edge, giving index one.

The base word `10` has its unique `R_1` edge at index one.  Table (3.4)
therefore proves by induction both uniqueness and recurrence (3.2).
\(\square\)

Since the MSW paths partition their edge set and there are `C_n` roots,
Lemma 2 gives the exact count

\[
                         |R_n\cap H_{CF}|=C_n.         \tag{3.5}
\]

## 4. Proof of Theorem 1

By (2.2)--(2.4) and (3.5),

\[
\begin{aligned}
 |H_0\cap H_{CF}|
 &\le |H_0\setminus R_n|+|R_n\cap H_{CF}|\\
 &=nC_n+C_n=(n+1)C_n.                                \tag{4.1}
\end{aligned}
\]

Thus

\[
 |H_0\setminus H_{CF}|
 \ge2nC_n-(n+1)C_n=(n-1)C_n.                        \tag{4.2}
\]

The two factors have equal size, so the same number of new edges must be
inserted.  Doubling (4.2) proves (1.2).  The Catalan ratio

\[
 {C_{m+1}\over C_m}={4m+2\over m+2}=4+O(m^{-1})      \tag{4.3}
\]

gives (1.3).  \(\square\)

## 5. Exact audit and the sharper identity

The accompanying independent constructor
`mw_msw_difference_probe.cpp` implements:

1. equations `(ind-step1-P)`, `(new-paths)`, and `(ind-step2-P)` of the
   actual Mütze--Weber recursion with every `alpha` bit zero; and
2. the published MSW maps `g` and `h` from every Dyck root.

It was compiled and run on the remote RunPod, not on the local Mac.  It
checks Lemma 2 and recurrence (3.2) root by root.  The subsequent exact
second-matching recurrence proved in `MW_MSW_CATALAN_BRAID.md` strengthens
the result to

\[
 |H_0\cap H_{CF}|=3C_n,
 \qquad
 |H_0\triangle H_{CF}|=2(2n-3)C_n.                  \tag{5.1}
\]

Every individual MSW root path has exactly three common edges: its initial
edge, one reversed-GK edge, and one further edge of the complementary MW
matching.  The exact recurrences for both latter edges and the resulting
Catalan alternating-component theorem are in `MW_MSW_CATALAN_BRAID.md`.

## 6. Signed `T`-join and provenance consequence

The vector

\[
 x=1_{H_{CF}\setminus H_0}-1_{H_0\setminus H_{CF}}   \tag{6.1}
\]

is a valid integral signed `T`-join from the old MW endpoint set to
`D_n union overline(D_n)`, and the augmented components automatically have
one antipodal edge each because `H_CF` already consists of complementary
paths.  Theorem 1 says that this valid `T`-join has support
`Omega(m C_m)`, not `O(C_m)`.

Hence the canonical factor solves endpoint pairing but destroys the sparse
two-copy provenance needed by the critical Catalan lift.  A positive MW
route must construct a *different* antipodal refinement inside a genuinely
small alternating-trail neighborhood of `H_0`; importing the canonical MSW
factor wholesale cannot work.
