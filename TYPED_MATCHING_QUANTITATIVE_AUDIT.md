# Quantitative audit of the radius-typed matching step

## 1. Verdict

No currently stated quantitative hypergraph-matching theorem rounds the
fractional matching (8.6) of `PARTIAL_BLOCK_MULTISCALE.md` through

\[
        H=\sqrt{m\,\xi_m},\qquad \xi_m\longrightarrow\infty,
\]

with total defect `o(W)`, where

\[
        W=\binom{2m}{m}.
\]

There are three independent reasons.

1.  The typed edges are nonuniform and have maximum size

    \[
      K=2\ell(1+2H)=(4+o(1))\ell H\longrightarrow\infty,
    \]

    whereas the available theorems take the uniformity as fixed.  Their
    published parameter hierarchies do not give a diagonal statement for
    this `K`.
2.  More decisively, the typed complex has weighted relative pair-codegree

    \[
      \frac{2}{m+1}\leq \delta_2^{(x)}
      \leq \frac{2}{m-H}=(2+o(1))/m.                 \tag{1.1}
    \]

    The `sqrt(D/D_2)` bottleneck in Gould--Kelly therefore permits only
    `B<=sqrt((m+1)/2)`.  The band has

    \[
      V_H=(\sqrt\pi+o(1))W\sqrt m                    \tag{1.2}
    \]

    vertices, so even the lossless nominal scale `V_H/B` is

    \[
      (\sqrt{2\pi}+o(1))W,                            \tag{1.3}
    \]

    not `o(W)`.
3.  The pseudorandom weight-function clauses control the distribution of
    the leftover; they do not beat the matching theorem's leftover scale.
    In the Gould--Kelly theorem they actually put a lower bound
    `tau(V)/B` on each tracked leftover weight.

Thus arXiv:2511.11375 is directionally relevant but does **not** prove the
needed rounding.  The missing result must improve by a little-oh factor over
the square-root-codegree barrier **and** use the nested-chain/pair-flip
geometry.  Such a conclusion is false for arbitrary hypergraphs with the
same degree, codegree, and edge-size parameters.

This audit used the complete primary papers, not search summaries:

* Stephen Gould and Tom Kelly,
  [*Advancing the Roedl Nibble: New bounds on matchings and the list
  chromatic index of hypergraphs*](https://arxiv.org/abs/2511.11375),
  especially Theorem 1.4;
* Stefan Ehard, Stefan Glock, and Felix Joos,
  [*Pseudorandom hypergraph matchings*](https://arxiv.org/abs/1907.09946),
  especially Theorems 1.2 and 1.3.
* Noga Alon, Bela Bollobas, Jeong Han Kim, and Van H. Vu,
  [*Economical covers with geometric applications*](https://web.math.princeton.edu/~nalon/PDFS/abkv4.pdf),
  especially Theorem 1.2 and Corollary 1.5.

An important transcription point is that Gould--Kelly's loss is

\[
             B^{-1+\gamma}(\log D)^A,
\]

not `B^{-1+gamma} log_A D`.

## 2. Exact scale of the typed complex

Use the tail-compressed regime of Section 12 of
`PARTIAL_BLOCK_MULTISCALE.md`:

\[
 \begin{split}
 H&=\sqrt{m\xi_m},\qquad \xi_m\to\infty,\qquad
 H=o(m^{2/3}),\\
 \ell&=L_mH,\qquad L_m\to\infty,\qquad \ell=o(m),\\
 R&=2\ell.
 \end{split}                                           \tag{2.1}
\]

Put

\[
 N_q=\binom{2m}{m-q},\qquad \rho_q=N_q/W.
\]

The physical parameter-block family has

\[
 E_0=W(m)_\ell^2,
 \qquad D_0=R(m)_\ell^2,                              \tag{2.2}
\]

where `D_0` is the degree of a middle set.  Its logarithm is

\[
        \log D_0=(2+o(1))\ell\log m.                  \tag{2.3}
\]

For a block `B` and certification radius `d`, the typed edge is

\[
 e(B,d)=\mathcal M(B)\cup
        \bigcup_{q=1}^{d}(\mathcal L_q(B)\cup\mathcal U_q(B)),
\]

and

\[
             |e(B,d)|=R(1+2d).                        \tag{2.4}
\]

Thus the full fractional support contains exactly `(H+1)E_0` typed edge
copies, in `H+1` size classes.  The random pretyping used below retains
exactly `E_0` of them, one for each parameter block.

Consequently

\[
 \begin{split}
 K_{\max}&=R(1+2H)=(4+o(1))\ell H,\\
 K_{\rm av}
 &=R\left(1+2\sum_{q=1}^{H}\rho_q\right)
   =(2\sqrt\pi+o(1))\ell\sqrt m.                    \tag{2.5}
 \end{split}
\]

In particular,

\[
       \frac{K_{\max}}{\log D_0}
       =(2+o(1))\frac{H}{\log m}\longrightarrow\infty. \tag{2.6}
\]

The vertex set is the complete central band.  The local central-binomial
estimate `rho_q=exp(-q^2/m+o(1))`, uniformly on the relevant summation
range, gives

\[
 \begin{split}
 V_H
 &=W+2\sum_{q=1}^{H}N_q\\
 &=W\left(1+2\sum_{q=1}^{H}\rho_q\right)
   =(\sqrt\pi+o(1))W\sqrt m.                         \tag{2.7}
 \end{split}
\]

The required repair budget is `o(W)`, so the matching must leave the much
smaller relative fraction

\[
              o(W/V_H)=o(m^{-1/2}).                  \tag{2.8}
\]

## 3. Fractional regularity and an ordinary random support

The certification probabilities are

\[
 p_0=1-\rho_1,\qquad
 p_d=\rho_d-\rho_{d+1}\ (d<H),\qquad
 p_H=\rho_H.                                         \tag{3.1}
\]

They obey

\[
       \sum_{d=0}^{H}p_d=1,
       \qquad \sum_{d=q}^{H}p_d=\rho_q.              \tag{3.2}
\]

Giving `(B,d)` weight `p_d/D_0` makes every band vertex have weighted
degree exactly one.  The unweighted hypergraph containing all typed copies
is not regular: a middle vertex has degree `(H+1)D_0`, while a depth-`q`
vertex has degree `(H-q+1)D_0/rho_q`.

There is, however, a harmless way to obtain an ordinary nearly regular
support.  Independently give every parameter block `B` one type `d` with
probability `p_d`, and retain only `e(B,d)`.  Then

* every middle degree is exactly `D_0`;
* every depth-`q` degree has mean
  `(D_0/rho_q) sum_(d>=q)p_d=D_0`;
* Chernoff bounds and a union bound over fewer than `4^m` vertices give,
  simultaneously,

  \[
        \deg(v)=(1\pm D_0^{-1/4})D_0;                \tag{3.3}
  \]

* the analogous Bernstein bound over fewer than `16^m` pairs preserves all
  weighted pair-codegrees up to additive `D_0^{-1/4}D_0`.

The last union bounds are overwhelmingly safe because
`log D_0=Omega(ell log m)` while their failure exponents are
`Omega(D_0^(1/2))`.

This random typing removes the need to represent the rational `p_d` by
parallel identical copies.  It does **not** remove the variable edge sizes
(2.4).

## 4. Exact pair-codegree bottleneck

The symmetric block calculation in `MIXED_PAIR_ROUNDING.md` gives, for two
vertices at ranks `m+a` and `m+b`, the following conditional co-occurrence
ratios.

* For nested vertices whose ranks differ by `t>0`, the ratio is

  \[
       \frac{t+1}{\binom{m-a}{t}}
       \quad\hbox{or}\quad
       \frac{t+1}{\binom{m+a}{t}}.                   \tag{4.1}
  \]

* For equal ranks and Johnson distance `t`, it is

  \[
       \frac{2}{\binom{m+a}{t}\binom{m-a}{t}}.       \tag{4.2}
  \]

* If neither set contains the other, writing
  `v=|A-B|` and `u=|B-A|`, symmetry and the at most `2ell` candidates at a
  fixed rank give

  \[
   \frac{2\ell}
        {\binom{m+a}{v}\binom{m-a}{u}}
       \leq \frac{2}{m-H}                            \tag{4.3}
  \]

  for all sufficiently large `m`.

The nested expression is maximized at `t=1`.  Therefore the maximum
fractional pair load satisfies

\[
          \delta_2^{(x)}\leq\frac{2}{m-H}.            \tag{4.4}
\]

There is also an exact matching lower bound.  Fix a middle set `X` and a
facet `S subset X`.  Among blocks through `X`, exactly two of the `m`
facets of `X` occur as adjacent depth-one intersections.  Symmetry therefore
gives conditional block frequency `2/m`.  The pair is present only for
types `d>=1`, whose total probability is

\[
               \sum_{d=1}^{H}p_d=\rho_1=\frac{m}{m+1}.
\]

Hence

\[
 \boxed{
    \sum_{e\supseteq\{X,S\}}x_e
       =\frac{2}{m}\rho_1=\frac{2}{m+1}.             \tag{4.5}
 }
\]

Combining (4.4)--(4.5),

\[
          \delta_2^{(x)}=(2+o(1))/m.                 \tag{4.6}
\]

After the random typing of Section 3, with positive probability the ordinary
support has

\[
 \begin{split}
 D&=(1+o(1))D_0,\\
 \frac{D_2}{D}&\leq\frac{2}{m-H}+o(1/m),\\
 \frac{D_2}{D}&\geq\frac{2}{m+1}-o(1/m).             \tag{4.7}
 \end{split}
\]

The large codegree is not an artefact of loose counting.  It is the intended
adjacent-rank nesting inside every certified symmetric-chain segment.

## 5. Exact substitution into Gould--Kelly

Theorem 1.4 of Gould--Kelly concerns a `(k+1)`-**uniform**,
`(n,D,epsilon)`-regular hypergraph.  For codegree bounds `D_j`, it permits

\[
 B\leq\min\left\{
       \sqrt{D/D_2},
       \min_{4\leq j\leq k+1}(D/D_j)^{1/(j-1)},
       1/\epsilon
       \right\},                                     \tag{5.1}
\]

and returns a matching leaving at most

\[
           nB^{-1+\gamma}(\log D)^A                  \tag{5.2}
\]

vertices, under

\[
           1/D\ll1/A\ll\gamma\ll1/k\leq1.           \tag{5.3}
\]

First ignore the nonuniformity, the growing `k`, and every possible
higher-codegree bottleneck.  The exact pair (4.5) alone forces

\[
             B\leq(1+o(1))\sqrt{\frac{m+1}{2}}.       \tag{5.4}
\]

For the random support of Section 3 one may take the regularity error
`epsilon=D^(-1/4)`, so the `1/epsilon` term is much larger than the right
side of (5.4).  Any higher-codegree term can only make `B` smaller.

Consequently the smallest nominal right side obtainable from (5.2), even
after deleting the factors `B^gamma(log D)^A`, is no smaller than

\[
 \frac{V_H}{B}
 \geq(\sqrt{2\pi}+o(1))W.                            \tag{5.5}
\]

The desired conclusion is `o(W)`.  Thus the theorem misses by a genuine
little-oh factor at the square-root-codegree boundary.  Better estimates for
`D_j`, `j>=3`, cannot help because (5.4) remains one of the mandatory
minimum terms.

The actual statement is still less applicable.

* Our edges have all sizes `R,3R,...,(1+2H)R`; Theorem 1.4 requires one
  uniform size.
* Its hierarchy fixes the uniformity before the asymptotic limit.  Here
  `k+1=K` tends to infinity and (2.6) shows that it even exceeds `log D` by
  an unbounded factor.  The paper supplies no bound on its threshold that
  can be diagonalized in this regime.
* If one formally chose `gamma=o(1/K)` and then `A` according to (5.3), the
  factor `(log D)^A` would make (5.2) much worse, not better.

Padding a type-`d` edge with private dummy vertices up to size `K` preserves
the original matching conflicts, but every dummy has degree one.  It
therefore destroys the near-regularity hypothesis of Theorem 1.4.  Splitting
by type also fails: one type has unequal degrees across its rank classes and
the types must compete for the same middle vertices.

### Weight functions do not repair the rate

Gould--Kelly's extra functions are vertex weights
`tau:V(H)->R_{>=0}`.  They must satisfy

\[
 \begin{array}{ll}
 \text{(P1)}&\tau(V)\geq B\max_v\tau(v),\\
 \text{(P2)}&|\operatorname{supp}\tau|\leq D^{\log D},\\
 \text{(P3)}&\text{each vertex belongs to at most }D^{\log D}
              \text{ supports}.
 \end{array}                                          \tag{5.6}
\]

For every accepted weight it guarantees

\[
 \frac{\tau(V)}B
 \leq\tau(V\setminus V(M))
 \leq\tau(V)B^{-1+\gamma}(\log D)^A.                 \tag{5.7}
\]

The natural layer indicators give only `2H+1` very simple `0/1` functions.
In fact (2.3) gives

\[
       \log(D^{\log D})=(\log D)^2\gg m\asymp\log V_H, \tag{5.8}
\]

so every whole rank class already satisfies (P2); (P1) is immediate because
`N_H >> B`, and each vertex occurs in exactly one of these supports, giving
(P3).  There is no global bound on the number of functions in Theorem 1.4
beyond the local condition (P3).  Thus the required number and complexity
of coarse weights -- exactly `2H+1` indicator functions -- is **not** the
main obstruction.  Rather, summing the lower bounds in (5.7) over these
disjoint rank classes shows that the particular pseudorandom matching
promised by the theorem leaves at least `V_H/B=Theta(W)` tracked weight.

The weights also do not encode the fractional edge probabilities `p_d`:
they are vertex weights, not an input fractional matching.  The random
pretyping in Section 3 is still needed before any ordinary matching theorem
can be considered.  Likewise, a singleton target indicator fails (P1) as
soon as `B>1`, and an indicator of blocks of a given certification type is
an **edge** weight, outside Theorem 1.4.  The theorem can therefore track
coarse leftover counts in the `2H+1` rank classes, but it cannot by itself
enforce the type law or individual shadow occurrences.  Tail compression in
Section 12 removes the latter requirement; it does not remove the total
defect obstruction (5.5).

Gould--Kelly's bounded reserve theorem (Theorem 1.5) does not bypass this
conclusion.  It assumes an explicit bipartite reserve hypergraph satisfying
strong degree and codegree conditions.  No such reserve is supplied here;
constructing one capable of absorbing the `Theta(W)` square-root-barrier
leftover is essentially the missing absorption theorem, not a consequence
of the black box.

## 6. Exact substitution into Ehard--Glock--Joos

Theorem 1.2 of Ehard--Glock--Joos is useful to audit because it allows a
maximum-degree hypothesis rather than near-regularity.  Thus private-dummy
padding can make the typed support `K`-uniform without causing an immediate
minimum-degree failure.

Their theorem assumes, for fixed uniformity `r`,

\[
 \Delta^c\leq\Delta^{1-\delta},
 \qquad \varepsilon=\frac{\delta}{50r^2},             \tag{6.1}
\]

allows at most `exp(Delta^(epsilon^2))` edges and weight functions, and gives
relative weight error

\[
                         \Delta^{-\varepsilon}.       \tag{6.2}
\]

Put `r=K` and take `Delta=(1+o(1))D`.  From (4.7), the largest permissible
codegree exponent satisfies

\[
 \delta\leq
 \frac{\log((m+1)/2)+o(1)}{\log D}.                  \tag{6.3}
\]

Even at equality, (6.2) becomes

\[
 \Delta^{-\varepsilon}
 \geq
 \exp\left[-\frac{\log((m+1)/2)+o(1)}{50K^2}\right]
 =m^{-1/(50K^2)+o(1/K^2)}=1-o(1).                   \tag{6.4}
\]

It does not even yield a vanishing relative defect.  Moreover,

\[
 \varepsilon^2\log\Delta
 \leq
 \frac{(\log m)^2}{2500K^4\log D}=o(1),             \tag{6.5}
\]

so

\[
             \exp(\Delta^{\varepsilon^2})=O(1).      \tag{6.6}
\]

The actual typed support has

\[
       E_0=W(m)_\ell^2,
       \qquad \log E_0=\Theta(m+\ell\log m),          \tag{6.7}
\]

and hence violates the edge-count hypothesis after this formal diagonal
substitution.  Even the `H+1` natural type weights eventually exceed the
formal `O(1)` weight-function allowance.  As with Gould--Kelly, the theorem
also fixes `r` before sending `Delta` to infinity and gives no diagonal
threshold.

Thus the earlier Ehard--Glock--Joos theorem fails both its hypotheses and
its required output rate.

## 7. The genuinely growing-uniformity theorem also fails

Alon--Bollobas--Kim--Vu is the most relevant located primary theorem which
genuinely permits the uniformity to grow.  Corollary 1.5 of *Economical
covers with geometric applications* says that a `D`-regular `k`-uniform
hypergraph with maximum codegree `C` has a matching whose uncovered set is

\[
 O\left(
   k\left(\frac{C\log(1+C)}D\right)^{1/(k-1)}n
 \right),                                             \tag{7.1}
\]

provided

\[
                 e^{2k}C=o(D/\log D).                 \tag{7.2}
\]

Optimistically suppose again that the typed support could be made
`K`-uniform and regular without changing (4.7).  With
`C/D=(2+o(1))/m`, condition (7.2) would require

\[
       \frac{e^{2K}\log D}{m}=o(1).                  \tag{7.3}
\]

But `K=(4+o(1))ell H` and `H/log m -> infinity`, so the left side diverges
superexponentially.  The hypothesis fails.

The conclusion is also quantitatively useless even if (7.2) is deleted.
When `C log(1+C)/D<1`,

\[
 \left(\frac{C\log(1+C)}D\right)^{1/(K-1)}
 =\exp\left[-O\left(\frac{\log m+\log\log D}{K}\right)\right]
 =1-o(1),                                             \tag{7.4}
\]

and otherwise the displayed bound is already trivial.  Thus (7.1) cannot
give even an `o(V_H)` leftover in the present regime, much less `o(W)`.

This closes the most natural growing-uniformity escape route: its explicit
dependence on `K` fails by an enormous margin.

## 8. Why no degree/codegree-only theorem can suffice

The failure above is not just a bad constant in one nibble proof.  A
projective plane of order `s-1`, viewed as an `s`-uniform hypergraph of
points and lines, is `s`-regular, has relative pair-codegree `1/s`, and has
matching number one because every two lines intersect.  Taking `s>=m`
matches or improves the numerical `O(1/m)` pair-codegree of the typed
complex while remaining maximally nonmatchable.  There is always a prime
power between `m` and `2m`, so such examples exist with `s=Theta(m)`; this
already lies below the present maximum edge size `K >> m`.  Parallel copies
of every line give arbitrarily large degree while preserving matching number
one and the relative codegree.

Therefore a theorem using only

\[
       K,\quad D,\quad D_2/D=O(1/m),
\]

cannot prove the desired matching.  It must use structure which the
projective-plane example lacks.  In the present complex:

* every typed edge is a disjoint union of `R=2ell` saturated symmetric-chain
  segments;
* the `R` middle members form one pair-flip cycle;
* the large `Theta(1/m)` codegrees occur only along adjacent nested ranks;
* equal-rank middle codegrees are only `O(1/m^2)`;
* along a prescribed nested flag, every additional vertex costs another
  factor of order `1/m`.

Those are the inputs a successful theorem has to exploit.

## 9. The weakest useful successor theorem

Let `G_m` be either the exact fractional typed complex or a random pretyped
support satisfying (3.3) and (4.7).  Since (2.7) holds, the exact required
conclusion is

\[
       |V(G_m)\setminus V(M)|
       =o\left(\frac{V_H}{\sqrt m}\right)=o(W).       \tag{9.1}
\]

In terms of the pair load, this is

\[
       |V(G_m)\setminus V(M)|
       =o\bigl(V_H\sqrt{\delta_2^{(x)}}\bigr).        \tag{9.2}
\]

Gould--Kelly reaches the corresponding `O` scale (up to its losses); the
needed theorem requires a genuine little-oh improvement.

A correct specialized statement would be:

> **Radius-typed chain-bundle rounding theorem.**  For (2.1), the
> certification law (3.1), and the partial pair-flip block family, the exact
> fractional perfect matching `x(B,d)=p_d/D_0` has an integral matching
> leaving `o(W)` central-band vertices.

This is the weakest direct theorem that closes Sections 8--12 of
`PARTIAL_BLOCK_MULTISCALE.md`.  A generic version must add hypotheses
encoding the chain-bundle geometry or a strong edge--link spread/absorption
condition; it cannot follow from pair codegree alone.

The most plausible two-stage version lowers the effective uniformity:

1. first resolve almost all band vertices into compatible symmetric-chain
   segments;
2. contract each segment to one atom and bundle `R=2ell` atoms into
   pair-flip necklaces.

The resulting bundling problem has edge size `R`, not
`Theta(ell sqrt(m))`, and its middle-only relative codegree is
`O(1/m^2)`.  Since

\[
                  R^2/m^2=O(\ell^2/m^2)=o(1),         \tag{9.3}
\]

this is quantitatively compatible with a growing-uniformity nibble.  What
remains is precisely the shift-compatible/wreath-resolved SCD condition of
Sections 9--10; no audited paper currently supplies it.

## 10. Final theorem ledger

Proved and usable:

* exact fractional degree one at every band vertex;
* `V_H=(sqrt(pi)+o(1))W sqrt(m)`;
* maximum edge size `(4+o(1))ell H` and average edge size
  `(2sqrt(pi)+o(1))ell sqrt(m)`;
* weighted pair load between `2/(m+1)` and `2/(m-H)`;
* an ordinary nearly regular **nonuniform** support obtained by random
  pretyping.

Not supplied by current matching theorems:

* a diagonal growing-uniformity statement for these parameters;
* rounding of an input fractional matching with variable edge sizes;
* an error `o(m^(-1/2))` on the complete band;
* an absorption theorem exploiting the nested-chain clusters.

The 2025 Gould--Kelly theorem therefore clarifies the obstruction rather
than removing it: its mandatory square-root pair-codegree bottleneck lands
exactly at the `Theta(W)` repair scale.  Progress must come from the
chain-bundle quotient or a new structural absorption theorem, not from a
stronger black-box reading of the existing nibble.
