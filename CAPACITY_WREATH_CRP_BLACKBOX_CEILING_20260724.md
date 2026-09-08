# Capacity-respecting wreath packing: exact black-box ceilings

## 1. Scope

Let

\[
 n=2m+1,\qquad W={n\choose m},\qquad
 h=(1+o(1))\sqrt{m\log\log m}.
\]

The capacity-respecting packing reduction asks for a family of cyclic-order
wreaths whose middle intervals are pairwise disjoint, whose depth-`q` loads
do not exceed balanced floor/ceiling capacities for every `q<=h`, and whose
middle leftover satisfies

\[
                         L=o(W/h).                    \tag{1.1}
\]

The transfer from such a packing to a `(1+o(1))W` OR word is valid.  This
note audits whether a published general matching theorem currently supplies
the remaining packing.  The answer is **no**.  There is an intrinsic
middle-layer pair-codegree bottleneck, and every presently relevant black
box either has fixed-uniformity hypotheses or stops quantitatively before
the scale in (1.1).

Nothing below disproves the existence of the desired packing.  A bespoke
switching, absorption, or exact-factor rebundling theorem can evade all of
the ceilings below.

## 2. The pair-codegree bottleneck is invariant

Let `H_m` be the multihypergraph whose vertices are the middle `m`-sets and
whose edges are the `n` middle intervals in an oriented cyclic order.  The
full hypergraph is regular of degree

\[
                         D=m!(m+1)!.
\]

More generally, let `G` be any `d`-regular spanning submultihypergraph of
`H_m`.

### Lemma 2.1 (unavoidable disjoint-pair codegree)

\[
                 \boxed{\Delta_2(G)\ge {2d\over m+1}.}             \tag{2.1}
\]

#### Proof

Fix a middle set `X`.  There are exactly `m+1` middle sets disjoint from
`X`.  In every wreath containing `X`, exactly two other middle intervals are
disjoint from `X`: if `X` occupies cyclic positions `0,...,m-1`, they are
the length-`m` intervals starting at positions `m` and `m+1`.  Therefore

\[
 \sum_{Y:Y\cap X=\varnothing}\deg_G(X,Y)=2d.
\]

Taking the largest of the `m+1` summands proves (2.1).  For the full wreath
hypergraph equality is attained, since

\[
 {\deg_{H_m}(X,Y)\over D}
 ={2\over {m\choose t}{m+1\choose t}},
 \qquad t=|X\setminus Y|,
\]

and the maximum occurs at `t=m`.  \(\square\)

Random edge sparsification does not improve this normalized obstruction:
if it preserves approximate regularity, averaging still gives
`Delta_2/d >= (2-o(1))/(m+1)`.

## 3. The 2025 full-codegree nibble still stops too early

Gould and Kelly, *Advancing the Rodl Nibble: New bounds on matchings and the
list chromatic index of hypergraphs*, arXiv:2511.11375, Theorem 1.4, use a
parameter `B` satisfying, among other bounds,

\[
                         B\le\sqrt{D/D_2},             \tag{3.1}
\]

and return a leftover bounded by

\[
                  |V|B^{-1+\gamma}\log_A D.            \tag{3.2}
\]

See <https://arxiv.org/abs/2511.11375>.

By Lemma 2.1, even an ideal regular sparsification has

\[
             B\le\sqrt{(m+1)/2}.                       \tag{3.3}
\]

Thus, even if one formally suppresses the factors
`B^gamma log_A D` and ignores every other hypothesis, this theorem can
certify only the scale

\[
                          L=O(W/\sqrt m).                \tag{3.4}
\]

The capacity transfer needs

\[
 {W\over h}=(1+o(1)){W\over\sqrt{m\log\log m}},         \tag{3.5}
\]

and in fact needs little-`o` of (3.5).  Hence there is a diverging
`sqrt(log log m)` gap before the capacity conflicts are even imposed.

There is also a prior applicability failure: Theorem 1.4 assumes the
hierarchy

\[
             1/D\ll1/A\ll\gamma\ll1/k\le1,
\]

where the hypergraph is `(k+1)`-uniform.  Here `k=n-1=2m` grows.  The
calculation above is therefore deliberately generous: it shows that even a
hypothetical uniform-in-`k` reading of the displayed conclusion would not
reach (1.1).

Higher codegrees do not remove this particular ceiling, because the
square-root term in (3.1) is an explicit member of the minimum defining
`B`.

## 4. Capacity cloning does not make ABKV applicable

One can encode each capacity by clones of the corresponding lower target.
An expanded cyclic-order edge then contains

* `n` middle vertices; and
* `n` capacity vertices at every depth `q<=h`.

Its uniformity is therefore

\[
                     K=n(h+1).                          \tag{4.1}
\]

The old middle-middle pair codegrees remain present, so an approximately
regular expanded hypergraph of degree `d` has

\[
                       \Gamma/d\ge{2-o(1)\over m+1}.    \tag{4.2}
\]

The growing-uniformity Alon--Bollobas--Kim--Vu matching/cover theorem used
elsewhere in the project requires

\[
                       e^{2K}\Gamma\log d=o(d).          \tag{4.3}
\]

See <https://web.math.princeton.edu/~nalon/PDFS/abkv4.pdf>.
But (4.2) gives

\[
 {e^{2K}\Gamma\log d\over d}
 \ge (2-o(1)){e^{2n(h+1)}\log d\over m+1}\longrightarrow\infty. \tag{4.4}
\]

The condition fails already if only the middle and first-shadow rows are
cloned (`K=2n`), and even for the middle wreath hypergraph alone (`K=n`).
The exact middle factor exists because of special odd-graph structure, not
because ABKV applies.

## 5. Conflict-free matching theorems do not bridge the gap

The theorem of Glock, Joos, Kim, Kuhn and Lichev, *Conflict-free hypergraph
matchings*, JLMS 109 (2024), arXiv:2205.05564, is a fixed-uniformity theorem.
Its quantitative general form (Theorem 3.1) assumes

\[
 \Delta_2(H)\le d^{1-\varepsilon},\qquad
 |V(H)|\le\exp\!\left(d^{\varepsilon^2/\ell}\right),
 \qquad
 \mu^{-\Gamma\ell}\le d^{\varepsilon^2},               \tag{5.1}
\]

for a `(d,ell,Gamma,epsilon)`-bounded conflict system, and gives a matching
of relative leftover `mu`.  See <https://arxiv.org/abs/2205.05564>.

The intrinsic ratio (2.1) forces, up to lower-order terms,

\[
 \varepsilon\log d\le\log m.                            \tag{5.2}
\]

The vertex-count hypothesis is already incompatible with the wreath scale
under the theorem's fixed-parameter regime.  Indeed, also using
`epsilon<=1`,

\[
 \varepsilon^2\log d
 \le \min\{\log d,(\log m)^2/\log d\}
 \le \log m.                                            \tag{5.3}
\]

Consequently

\[
 d^{\varepsilon^2/\ell}\le m^{1/\ell},                 \tag{5.4}
\]

whereas `log |V(H)|=log W=Theta(m)`.  For every `ell>=2`, (5.4) is
`o(m)`, so the vertex bound in (5.1) cannot hold.  This remains true if one
tries to tune the sparsification degree `d`.

There is a second, independent higher-capacity obstruction.  A capacity
`b_q(S)` is naturally enforced by forbidding `b_q(S)+1` selected wreaths
through `S`, so the largest conflict size satisfies

\[
 \ell\ge 1+\max_{q\le h,S}b_q(S)
 =(1+o(1)){W\over N_h}.
\]

At the reservoir threshold

\[
 h^2/m=\log\log m+\gamma(m)+o(1),
\]

this gives

\[
                    \ell\ge (1+o(1))e^{\gamma(m)}\log m. \tag{5.5}
\]

Thus the exact growth condition `mu^{-Gamma ell}<=d^{epsilon^2}` becomes
strictly harder at the outer controlled depths.  Treating only pair
conflicts at depth one does not enforce the higher capacities and therefore
does not prove CRP.

The independent theorem of Delcourt and Postle and the later
conflict-free matching-and-covering variants have the same fixed-rank
nature for the relevant black-box statements; none supplies a uniform
remainder at rank `2m+1` satisfying (1.1).

## 6. The corrected local conflict estimate is useful but not sufficient

For a fixed wreath `e`, a middle set `Y` outside `e`, and `q<m/2`, the exact
fraction of wreaths through `Y` that contain a prescribed
`(m-q)`-subset `S` of `Y` as an interval is

\[
                         {q+1\over {m\choose q}}.        \tag{6.1}
\]

That calculation alone does **not** bound all shared targets, because a
common interval need not lie inside `Y`.  Accounting also for targets inside
`Y^c` and for intervals crossing either boundary gives the corrected union
bound

\[
 \Pr(\mathcal C_q(e)\cap\mathcal C_q(f)\ne\varnothing\mid Y\in f)
 \le {q(q+1)\over {m\choose q}}
 +{(q+1)(q+2)\over {m+1\choose q+1}}
 +{2n\over (m+1){m\choose q+1}}.                       \tag{6.2}
\]

Consequently

\[
 \sum_{q=1}^h
 \Pr(\mathcal C_q(e)\cap\mathcal C_q(f)\ne\varnothing\mid Y\in f)
 \le {2\over m}+{32\over m^2}+O(m^{-3})                \tag{6.3}
\]

uniformly for `h<=m/3`.

The exact derivation and the `n=7,m=3,q=1` counterexample to the shorter
bound are in `CAPACITY_RESPECTING_WREATH_PACKING_AUDIT_20260724.md`.
The corrected estimate confirms that the added conflicts are locally
first-shadow dominated.
It does **not** remove Lemma 2.1, and it does not provide the
`o(1/h)` leftover required in (1.1).  In particular, “normalized local
conflict degree `O(1/m)`” is not by itself a quantitative correlated
matching theorem.

## 7. Pruning the canonical exact factor cannot work

Let `F` be any exact middle factor and let `P subseteq F` be obtained only by
deleting wreaths.  If `M_q(F)` depth-`q` targets are absent from `F`, they
remain absent from `P`, so

\[
                          M_q(P)\ge M_q(F).              \tag{7.1}
\]

If `P` respects balanced capacities and has middle leftover `L`, the exact
capacity ledger gives `M_q(P)<=L`.  Therefore

\[
                          L\ge M_q(F)                    \tag{7.2}
\]

for every controlled depth.

The unchanged canonical MSW factor has a positive observed first-shadow
defect (for example `270337/1144066` of the first-shadow targets at `m=11`,
and `1098850/4457400` at `m=12`).  Thus no deletion-only argument starting
from that factor can give (1.1) in those dimensions; asymptotically, a proof
needs positive-density rebundling or a different factor.  The finite data do
not prove a positive limiting defect, so this is not an all-dimensional
nonexistence result.

More conceptually, CRP itself forces

\[
                     M_q=o(W/h)\quad(q\le h),            \tag{7.3}
\]

which is stronger than the weak vertical condition
`sum_(q<=h) M_q=o(W)`.  The capacity formulation is an exact and useful
sufficient gate, but not a relaxation of the shadow-surjectivity problem.

## 8. What a genuine bridge must add

The audit leaves three plausible escape routes, none currently proved.

1. **Exact-factor switching/rebundling.**  Start from an exact middle factor
   and use correlated trades that preserve middle ownership while flattening
   all shallow loads.  This can beat nibble ceilings because it never asks a
   random matching process to rediscover middle ownership.
2. **Absorption below the square-root codegree scale.**  A first-stage
   matching may leave `Theta(W/sqrt(m))` vertices, but a structured absorber
   would have to remove an additional diverging `sqrt(log log m)` factor
   while preserving every capacity.
3. **A path/segment formulation with smaller native rank.**  Breaking a
   wreath into correlated Johnson-path pieces can evade the invariant
   wreath pair codegree, but one must then prove endpoint closure and the
   literal OR transfer.  This is a different construction, not an
   application of CRP as stated.

Accordingly, the capacity-respecting transfer theorem is a sound reduction,
but its existence hypothesis remains a genuinely new structured-design
problem.  No currently identified general matching theorem proves it.
