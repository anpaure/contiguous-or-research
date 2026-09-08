# Scarce-first all-arity compilation: exact run geometry, port-captured Hall, and the positive-density collar law

Date: 2026-07-30  
Lane: K, pure-mathematics all-`k` compiler lane  
Status: unconditional fixed-chronology theorems and unconditional architecture-specific obstructions. The required PBBS/Pascal port or target-tiling hypothesis is not proved.

## 0. Outcome

This note turns the next-occurrence/run-boundary reduction into three concrete compiler theorems.

First, after the scarce facet and singleton choices have been forced and exact unit closure has been performed, the residual all-arity problem has an exact deterministic Hall solution whenever its candidates carry physical port lists that capture every minimal conflict. If

\[
 \delta=\max_{X}(|X|-|N(X)|)
\]

is the target-to-port Hall defect, then

\[
 \boxed{\nu(k)\le B(k)+|\mathcal O|+\delta.} \tag{0.1}
\]

Thus `delta=O(k)` gives `B(k)+O(k)`, while `delta=0` gives the sharp upper bound. This is an integral theorem inside one literal chronology; it is not a fractional or averaged construction.

Second, there is a deterministic weighted-pruning alternative to port capture. For `1<c<M`, score a residual candidate `v` by

\[
 \Sigma_M(v)=
 \sum_{F\in\mathcal A(v)}
 { (c/M)^{|F|}\over 1-(c/M)^{|F|}}.                 \tag{0.2}
\]

If every residual target part contains at least `M` candidates satisfying
`Sigma_M(v)<=log c`, pruning to any `M` such candidates proves the
existence of an exact compiler. This is a genuine rank-by-rank deterministic
use of the atomic lopsided theorem: all scores are computed after the scarce
choices and their physical reservations have been contracted.

Third, the literal run geometry can be made completely explicit. A family
of target intervals is compatible exactly when each coordinate's deleted
source runs have length at most `d` and every selected positive coordinate
retains an occurrence in its own interval. This gives a deterministic
collar-overwrite construction and a guarded local atom producing
`binom(ell+1,2)` distinct deep labels in a collar of length `ell`.

There is also a sharp scale obstruction. Any flat maximal-erosion
antecedent whose own short intervals miss only `h=o(W)` lower targets must
delete `Omega(W)` source-coordinate incidences and edit `Omega(W/d)` source
sites. This includes the fixed-antecedent, literal append-only route to
`B(k)+O(k)`, but not an arbitrary extension using new cross-boundary
intervals. For odd `k=2m+1`,

\[
 |\Delta|\ge(c_*+o(1))W,
 \qquad
 |E|\ge(4\Phi(-\sqrt{\pi/2})+o(1)){W\over d},       \tag{0.3}
\]

where

\[
 c_*={4\sqrt{2\pi}\over\pi}
 \left(\phi(\sqrt{\pi/2})-\sqrt{\pi/2}\,
       \Phi(-\sqrt{\pi/2})\right)>0.                \tag{0.4}
\]

For the separated local-collar architecture, the edited collar support itself must have asymptotic density at least

\[
                         4\Phi(-\sqrt{\pi/2})>0.     \tag{0.5}
\]

Consequently, `o(W/d)` edited sites cannot prove `B(k)+O(k)` by this
fixed-antecedent append-only architecture. In the separated local-collar
architecture, even `o(W)` total collar support is impossible. In particular,
Catalan-many seams are insufficient when each changes only `O(1)` source
sites; no unqualified seam-count obstruction is claimed. The remaining
positive theorem must be a positive-density Catalan/Pascal tiling or a
genuinely nonlocal cross-collar port construction.

## 1. Fixed chronology and exact physical atlas

Put

\[
 r=\lceil k/2\rceil,
 \qquad W={k\choose r},
 \qquad \Lambda=\sum_{s=1}^{r-1}{k\choose s},       \tag{1.1}
\]

and let

\[
 d=\min\left\{j\ge0:jW+{j+1\choose2}\ge\Lambda\right\},
 \qquad B(k)=W+d.                                    \tag{1.2}
\]

The case `d=0` is immediate, so assume `1<=d<r`. Let

\[
 T=(T_0,\ldots,T_{W-1})                              \tag{1.3}
\]

be a strict linearly `d`-resident Johnson ordering of all rank-`r` masks. Its maximal erosion is the length-`W+d` word

\[
 P_p=\bigcap_{i=\max(0,p-d)}^{\min(p,W-1)}T_i
 \qquad(0\le p<W+d).                                \tag{1.4}
\]

Residence gives `D^dP=T`. Write

\[
 F_p=(P_p\setminus P_{p-1})\cup(P_p\setminus P_{p+1}),\tag{1.5}
\]

with nonexistent endpoint terms omitted. The run-boundary theorem says that `F_p` is nonempty and is contained in every nonzero antecedent `A_p` satisfying `A<=P` and `D^dA=T`.

For a nonempty source interval `I` of length at most `d`, put

\[
 P(I)=\bigcup_{p\in I}P_p,
 \qquad F(I)=\bigcup_{p\in I}F_p.                   \tag{1.6}
\]

A physical candidate for a strict lower target `S` is a pair `(S,I)` satisfying

\[
                         F(I)\subseteq S\subseteq P(I).\tag{1.7}
\]

These candidates are partitioned by their target `S`. The negative-window conflict hypergraph has as its edges the inclusion-minimal transversal families of candidates that cannot coexist in one antecedent. Before any Hall or local-lemma argument, all forced candidates are conditioned exactly, opposing candidates are discarded, incident conflicts are contracted, forbidden candidates are deleted, and newly forced parts are propagated. This is the exact unit closure from the atomic compiler theorem.

## 2. Exact run-component and positive-guard criterion

Let `Theta` be any family of candidates satisfying (1.7). For each coordinate `x`, define

\[
 N_x=\bigcup_{\substack{(S,I)\in\Theta\\x\notin S}}I,
 \qquad E_x=\{p:x\in P_p\},
 \qquad D_x=N_x\cap E_x,                             \tag{2.1}
\]

and define the canonical deletion antecedent

\[
 A_p=P_p\setminus\{x:p\in N_x\}.                    \tag{2.2}
\]

### Theorem 2.1 (exact run/guard normal form)

The family `Theta` is realized by (2.2), with `D^dA=T` and `A(I)=S` for every `(S,I) in Theta`, if and only if both conditions below hold.

1. Every ordinary consecutive component of every `D_x`, including a component meeting a source endpoint, has length at most `d`.
2. For every `(S,I) in Theta` and every `x in S`,

   \[
   (E_x\setminus N_x)\cap I\ne\varnothing.          \tag{2.3}
   \]

Every source letter `A_p` is automatically nonempty.

#### Proof

First note that the canonical antecedent loses no generality. If some
`A'<=P` realizes `Theta`, every negative demand `(S,I), x notin S` forces
`x notin A'_p` for all `p in I`, and hence `A'<=A`. Monotonicity gives

\[
 T=D^dA'\subseteq D^dA\subseteq D^dP=T.              \tag{2.4}
\]

Thus `D^dA=T`. Moreover `S=A'(I) subseteq A(I)`, while the canonical
negative deletions give `A(I) subseteq S`; hence `A(I)=S`. It is therefore
enough, and necessary, to test the canonical antecedent (2.2).

Since `A<=P`, the derivative `D^dA` has no false positive relative to `T=D^dP`. If `D_x` contains `d+1` consecutive positions `[u,u+d]`, then `u<=W-1`, `x in P_u subseteq T_u`, and the `u`th derivative window loses `x`. This proves necessity of the first condition.

Conversely, suppose the window `[i,i+d]` loses `x in T_i`. Let `[a,b]` be the positive `x`-run of `T` containing `i`. Its support in `P` is

\[
 [a',b'],\qquad
 a'=\begin{cases}0,&a=0,\\a+d,&a>0,\end{cases}
 \quad
 b'=\begin{cases}W+d-1,&b=W-1,\\b,&b<W-1.\end{cases} \tag{2.5}
\]

If `E_x cap [i,i+d]` is truncated at a finite end of (2.5), it contains that endpoint. The endpoint lies in its mandatory core `F_p`, and (1.7) prevents its deletion. Hence truncation is impossible and

\[
                         E_x\cap[i,i+d]=[i,i+d].      \tag{2.6}
\]

The failed window is therefore a component of `D_x` of length at least `d+1`, a contradiction.

For a selected `(S,I)`, every `x notin S` is absent from all `A_p`, `p in I`, because `I subseteq N_x`. A coordinate `x in S` occurs in `A(I)` exactly when (2.3) holds. This proves the target condition.

Finally, every selected interval through `p` has `F_p subseteq F(I) subseteq S`. Thus `F_p subseteq A_p`, so `A_p` is nonempty. QED.

This theorem is the promised next-occurrence/run-boundary normal form. All arities are present, but they are encoded by deleted run components and positive guards rather than by an explicit enumeration of hyperedges.

## 3. Deterministic collar compilation

Let `J_1,...,J_t` be pairwise disjoint source collars, each of length at most `d`, with at least one untouched source position between consecutive collars. For `p in J_1 union ... union J_t`, choose

\[
                         F_p\subseteq G_p\subseteq P_p.\tag{3.1}
\]

Set

\[
 A_p=\begin{cases}
      G_p,&p\in\bigcup_jJ_j,\\
      P_p,&p\notin\bigcup_jJ_j.
     \end{cases}                                      \tag{3.2}
\]

### Theorem 3.1 (separated-collar overwrite)

The word (3.2) satisfies `D^dA=T`. Every interval `I` disjoint from all collars retains its envelope label

\[
                         A(I)=P(I),                   \tag{3.3}
\]

and every subinterval `I subseteq J_j` has the literal label

\[
                         A(I)=G(I)=\bigcup_{p\in I}G_p.\tag{3.4}
\]

Consequently, if `T` is upper-complete and the labels in (3.3)--(3.4) include every strict lower target except a family `O`, then

\[
                         \nu(k)\le B(k)+|\mathcal O|.\tag{3.5}
\]

#### Proof

Every coordinate-deletion component is contained in a single collar and hence has length at most `d`. The mandatory cores survive. Theorem 2.1, or its central-window part, gives `D^dA=T`. Equations (3.3) and (3.4) are immediate from the definition.

Every middle target occurs in `T=D^dA`. If an upper target is a union of `T_i,...,T_j`, it is the union of the single source interval from `i` through `j+d`; upper completeness of `T` therefore transfers literally to `A`. The displayed lower labels cover all lower targets outside `O`, and appending each member of `O` as one literal letter proves (3.5). QED.

If a forced facet or singleton witness crosses a collar, (3.3) does not
apply. It survives precisely when the literal two-sided equality `A(I)=S`
holds: every source letter on `I` must be contained in `S`, and every
positive coordinate of `S` must pass the guard (2.3). Thus the guard alone
is necessary but is not sufficient for an arbitrary collar overwrite.

### Lemma 3.2 (guarded collar atom)

Put `R=r-d`, and let `J` be a flat collar of length `ell`. Assume `R>=3ell+1`, and choose

\[
 K\subseteq\bigcap_{p\in J}P_p,
 \qquad |K|\le R-3\ell-1.                            \tag{3.6}
\]

There are distinct markers

\[
 z_p\in P_p\setminus(K\cup F(J))\qquad(p\in J)      \tag{3.7}
\]

such that, for

\[
                         G_p=K\cup F_p\cup\{z_p\},   \tag{3.8}
\]

the `binom(ell+1,2)` nonempty subintervals of `J` produce pairwise distinct nonempty targets

\[
 S_I=K\cup F(I)\cup\{z_p:p\in I\},
 \qquad |S_I|\le R-1.                                \tag{3.9}
\]

#### Proof

On a flat collar, `|P_p|=R` and `|F(J)|<=2ell`. Hence every marker list in (3.7) has size at least

\[
 R-|K|-|F(J)|\ge\ell+1.                              \tag{3.10}
\]

There are only `ell` lists, so Hall's theorem supplies distinct representatives. They avoid both `K` and the entire set `F(J)`. Thus the marker subset in (3.9) recovers `I`, proving distinctness. Finally,

\[
 |S_I|\le |K|+|F(I)|+|I|
 \le R-3\ell-1+2\ell+\ell=R-1.                      \tag{3.11}
\]

Nonemptiness follows from the nonempty mandatory cores. QED.

The atom gives an explicit local generator, not a global target tiling. The
missing constructive task is to choose collars, bases, and markers so that
their labels enumerate the required deep Boolean ideal without duplication
while every forced shallow and tight witness is literally retained, with
both its negative exclusions and its positive guards.

## 4. Scarce-first port-captured Hall theorem

Fix any compatible family of scarce candidates, for example selected facet
and singleton witnesses, and perform exact unit closure. Let `H` be the
resulting transversal minimal-conflict hypergraph on residual target parts
`mathcal Q`; let `O` be the already omitted target family. Give every
residual candidate `v` a fixed, nonempty list `R(v)` of **physical ports**.
These ports and the reservations made by the forced candidates are fixed
before any matching is chosen.

A partial selector is port-rainbow if there is an injection `varphi` from its candidates to ports with `varphi(v) in R(v)`.

### Theorem 4.1 (port capture is the exact universal rainbow condition)

The following are equivalent.

1. Every port-rainbow partial selector is compatible.
2. No minimal conflict `E` has an SDR from the lists `(R(v))_(v in E)`.
3. For every minimal conflict `E`, there is `E' subseteq E` such that

   \[
   \left|\bigcup_{v\in E'}R(v)\right|<|E'|.          \tag{4.1}
   \]

#### Proof

Hall's theorem says that the lists on `E` admit an SDR if and only if (4.1) fails for every subfamily. Such an SDR makes `E` itself a port-rainbow incompatible partial selector. Conversely, if no conflict admits an SDR, no port-rainbow partial selector can contain a conflict. QED.

Form the bipartite target-port graph `G`: join target part `S` to port `q` when some candidate `v in V_S` has `q in R(v)`. Put

\[
 \delta(G)=\max_{X\subseteq\mathcal Q}(|X|-|N_G(X)|).\tag{4.2}
\]

### Corollary 4.2 (exact port-Hall compiler)

Under the equivalent conditions of Theorem 4.1, a maximum matching in `G`
supports a compatible selector for exactly
`|mathcal Q|-delta(G)` residual targets. If `T` is upper-complete, then

\[
 \boxed{\nu(k)\le B(k)+|\mathcal O|+\delta(G).}       \tag{4.3}
\]

#### Proof

The deficiency form of Hall's theorem gives a matching of size `|mathcal Q|-delta(G)`. For each matched edge `S-q`, choose a supporting candidate `v in V_S` with `q in R(v)`. The matched ports are distinct, so the selected candidates are port-rainbow and hence compatible. Append the omitted and unmatched lower targets. QED.

The number `delta(G)` is the exact loss inside this port-rainbow architecture, not necessarily the defect of the unrestricted compiler hypergraph. Similarly, port capture is necessary and sufficient for the **universal** guarantee that every rainbow partial selector is safe; it is not necessary for the mere existence of one specially chosen safe rainbow selector.

For singleton port lists `R(v)={rho(v)}`, capture is simply

\[
                         |\rho(E)|<|E|                \tag{4.4}
\]

for every minimal conflict. For a pair conflict, even list-valued capture forces the two nonempty port lists to be the same singleton. A convenient sufficient Hall test is also immediate: if every target has at least `M` adjacent ports and every port is adjacent to at most `M` targets, edge counting gives `|N(X)|>=|X|` and hence `delta=0`.

Once the matching is known, Corollary 4.2 is consistent with the atomic lopsided theorem by putting Dirac mass on the selected candidates and taking `y_E=0`, `c_v=1`. Every conflict then has probability zero. This is a retrospective verification, not a separate existence proof.

## 5. Weighted deterministic pruning of all-arity conflicts

Port capture may be too rigid. There is a second exact scarce-first theorem that retains the whole candidate-opposing conflict geometry.

After unit closure, suppose `H` has no unary edge. For a candidate `v in V_S`, let

\[
 \mathcal A(v)=
 \{F\in E(H):F\text{ uses a candidate in }V_S\setminus\{v\}\}.\tag{5.1}
\]

Fix integers `M>=2` and a real `1<c<M`, and define the full-atlas score (0.2).

### Theorem 5.1 (weighted opposition pruning)

If every residual target part contains at least `M` candidates `v` satisfying

\[
                         \Sigma_M(v)\le\log c,         \tag{5.2}
\]

then `H` has an independent full transversal. Therefore, for an upper-complete chronology,

\[
                         \nu(k)\le B(k)+|\mathcal O|.\tag{5.3}
\]

#### Proof

Prune every part to any `M` candidates satisfying (5.2), and select uniformly and independently from the pruned parts. For a retained conflict `F`, set

\[
                         y_F=(c/M)^{|F|}.              \tag{5.4}
\]

Its probability is `M^(-|F|)=y_F/c^|F|`. Pruning only deletes opposing conflicts, so the additive candidate-opposing pressure at every retained candidate is at most its original score (0.2), hence at most `log c`. The atomic lopsided product theorem applies and gives an integral independent transversal. The fixed-middle wrapper proves (5.3). QED.

### Corollary 5.2 (average rankwise test)

If a residual part has size `n_S>=2M` and

\[
 {1\over n_S}\sum_{v\in V_S}\Sigma_M(v)
 \le {1\over2}\log c,                               \tag{5.5}
\]

then it contains at least `M` candidates satisfying (5.2). Thus (5.5) in every residual part is sufficient for Theorem 5.1.

This follows directly from Markov's inequality. It is the precise Hall/LLL test requested after scarce ranks are forced: it is candidate-specific, all-arity, and evaluated in the same contracted physical chronology.

## 6. Rank-by-rank deterministic compiler theorem

The preceding results combine into the following construction protocol.

### Theorem 6.1 (scarce-first compiler)

Let `T` be strict, `d`-resident, and upper-complete. Process the lower target ranks in any fixed scarcity order, with rank `r-1` facets and rank `1` singletons first. At each step do one of the following:

1. force a certified physical candidate and perform exact unit closure;
2. omit the target and charge one appended letter;
3. leave the target for the residual compiler.

Assume the forced choices do not create an empty conflict or target part. Let `O` be the omitted family. Any one of the following residual certificates is sufficient.

1. Fixed physical port lists satisfy conflict capture (4.1), with Hall defect `delta`.
2. The weighted good-candidate condition (5.2) holds in every residual part.
3. A separated-collar word (3.2) literally realizes every forced crossing
   witness and covers the residual lower targets except a family `O'`.

The respective conclusions are

\[
 \nu(k)\le B(k)+|O|+\delta,                           \tag{6.1}
\]

\[
 \nu(k)\le B(k)+|O|,                                  \tag{6.2}
\]

and

\[
 \nu(k)\le B(k)+|O|+|O'|.                            \tag{6.3}
\]

In particular, `|O|+delta=O(k)`, `|O|=O(k)`, or `|O|+|O'|=O(k)` gives `B(k)+O(k)`; zero total defect gives the sharp upper bound.

#### Proof

Exact unit closure gives a bijection between compatible residual selectors and compatible full selectors extending the forced choices. Apply Corollary 4.2, Theorem 5.1, or Theorem 3.1 respectively, and append exactly the charged omissions. QED.

This theorem is not a hidden all-`k` solution: no present PBBS/Pascal theorem supplies any of the three residual certificates. It does isolate a finite, literal, rank-by-rank target whose verification would close the upper bound.

### Corollary 6.2 (the exact singleton/facet split)

For a `B(k)+O(k)` target one may put all `k` singleton masks into `O` at
the outset. Their tight-return sockets then impose no residual condition.
The rank-`(r-1)` facet layer, by contrast, has `binom(k,r-1)` targets and
cannot be appended within an `O(k)` budget; all but `O(k)` of those parts
must be forced or passed to the residual Hall/LLL certificate. After their
unit closure, Theorem 6.1 applies rank by rank to the remaining layers.

For the exact coefficient-one target, neither shortcut is available: the
singletons as well as the facets must have physical candidates in the final
selector. This is why the exact tight-run statistic remains relevant only
to the coefficient-one branch, whereas the facet-port problem is already
decisive for `B(k)+O(k)`.

## 7. Positive-density law for every flat antecedent

The preceding collar construction cannot be sparse. The obstruction below applies to every antecedent of one flat maximal erosion, not merely to the guarded atom.

Put

\[
 b=r-d\ge2,
 \quad
 \mathcal D_{\rm deep}=\{S:1\le |S|\le b-1\},        \tag{7.1}
\]

and

\[
 D_{\rm deep}=\sum_{s=1}^{b-1}{k\choose s},
 \qquad
 Q_{\rm deep}=\sum_{s=1}^{b-1}(b-s){k\choose s},
 \qquad
 C_d={d+1\choose2}.                                  \tag{7.2}
\]

Let `A<=P` be nonzero with `D^dA=T`, and suppose its short intervals cover all but `h` lower targets in total. Define its deletion tokens and edited sites by

\[
 \Delta=\{(p,x):x\in P_p\setminus A_p\},
 \qquad E=\{p:A_p\ne P_p\}.                          \tag{7.3}
\]

### Theorem 7.1 (exact deletion and edited-site lower bounds)

One has

\[
 |\Delta|\ge
 {Q_{\rm deep}-(h+2d^2)(b-1)\over C_d},              \tag{7.4}
\]

and

\[
 |E|\ge {D_{\rm deep}-h-2d^2\over C_d}.              \tag{7.5}
\]

Negative right sides may of course be replaced by zero.

#### Proof

Choose one witnessing interval for every covered deep target. Different targets use different intervals. At most `2d^2` intervals of length at most `d` meet either of the two source ramps: at each end there are at most `d` possible starts and `d` possible lengths. Discard those witnesses.

For a remaining flat witness `I` of a target `S` of rank `s<b`, choose any `p in I`. Then `|P_p|=b`, while `A(I)=S`. Hence every coordinate in `P_p\setminus S` is absent from `A_p`; this gives at least `b-s` deletion tokens. Removing an arbitrary missed or ramp target loses at most `b-1` from this charge. Every fixed token `(p,x)` is chargeable by at most `C_d` short intervals, the number of intervals of length at most `d` containing `p`. Summing proves (7.4).

The same flat witness contains an edited position: if some `p in I` satisfied `A_p=P_p`, then the rank-`b` set `P_p` would be contained in the rank-`s` union `A(I)`, impossible. A fixed position belongs to at most `C_d` short intervals, which proves (7.5). QED.

### Corollary 7.2 (odd-dimensional asymptotics)

Let `k=2m+1`, `r=m+1`, and `h=o(W)`; in particular `h=O(k)` is allowed. Put

\[
                         a=\sqrt{\pi/2}.              \tag{7.6}
\]

Here `phi` and `Phi` denote the standard normal density and distribution
function.

Then

\[
 d=\left({\sqrt\pi\over2}+o(1)\right)\sqrt m,
\]

and (0.3)--(0.4) hold.

#### Proof

For `X~Bin(2m+1,1/2)`, the local central estimate and the central limit theorem give

\[
 W\sim {2^k\over\sqrt{\pi m}},
 \qquad {D_{\rm deep}\over2^k}\longrightarrow\Phi(-a),\tag{7.7}
\]

and uniform integrability gives

\[
 {Q_{\rm deep}\over2^k\sqrt{m/2}}
 \longrightarrow \phi(a)-a\Phi(-a).                 \tag{7.8}
\]

Also `C_d~pi m/8`. Substitution into (7.4)--(7.5) gives the
displayed constants. Positivity of `c_*` follows from

\[
 a\Phi(-a)<\int_a^\infty t\phi(t)\,dt=\phi(a).      \tag{7.9}
\]

The `h=o(W)` and ramp terms are lower order. QED.

### Corollary 7.3 (separated collars must have positive density)

Assume all collars are flat, pairwise separated by an untouched position, have lengths `ell_j<=d`, and `A=P` outside their union. Put `L=sum_j ell_j`. If all but `h=o(W)` deep targets occur, then

\[
 D_{\rm deep}-h
 \le\sum_j{\ell_j+1\choose2}
 \le {d+1\over2}L.                                  \tag{7.10}
\]

Consequently,

\[
 L\ge {2(D_{\rm deep}-h)\over d+1}
   =(4\Phi(-a)+o(1))W,                               \tag{7.11}
\]

and, if `t` is the number of collars, then

\[
 t\ge\left\lceil {L\over d}\right\rceil
   \ge(4\Phi(-a)+o(1)){W\over d}.                    \tag{7.12}
\]

Indeed, a deep witness cannot contain an untouched site, because that site contributes the rank-`b` letter `P_p` to its union. Hence it lies wholly inside one collar, and one collar supplies at most its number of subintervals. This corollary does not apply to a nonlocal cross-collar braid that deliberately opens and recloses the intervening full-rank separator.

## 8. Why the obvious port colours fail

The port theorem is useful only if its ports have enough capacity and capture the real conflicts.

Let `mathcal P` be an active pool of physical columns, let `L` be the
number of residual target parts, and suppose a target-independent singleton
colour `rho:mathcal P->C` supports a rainbow selector omitting `e` targets.
Then necessarily

\[
 |\mathcal P|-|\rho(\mathcal P)|
 \le (|\mathcal P|-L)+e.                             \tag{8.1}
\]

For the untouched full short-interval atlas,

\[
 |\mathcal I_d|=dW+{d+1\choose2}=\Lambda+\sigma,     \tag{8.2}
\]

so (8.1) becomes

\[
 |\mathcal I_d|-|\rho(\mathcal I_d)|\le\sigma+e.   \tag{8.3}
\]

Let `G_2` be the underlying simple graph on interval columns in which
`I-J`, with `I ne J`, is an edge when distinct-target candidates supported
on `I,J` form a minimal pair conflict. Same-column conflicts give no graph
edge. Nonrainbow capture forces `rho` to be constant on every component,
and hence

\[
 \operatorname{rank}(G_2)
 =|\mathcal I_d|-\kappa(G_2)\le\sigma+e.             \tag{8.4}
\]

Thus rank larger than `sigma+Ck` rules out `B(k)+Ck` for this target-independent interval-colour architecture. After forcing and unit closure one must use the residual surplus in (8.1), not blindly reuse the original `sigma`.

The natural colour `rho(I)=I` fails even before this capacity test: for
every proved stable-coordinate arity `2<=j<=d+1` satisfying `Q>=j-1`, the
where `Q=2^(r-2d-2)-1`, the minimal conflicts use pairwise disjoint
intervals partitioning one central `d+1` window, so they are rainbow. The
exact `j=3` bank shows that checking or capturing pair conflicts alone
cannot certify all-conflict capture. These are architecture-specific no-go
statements; target-dependent ports, list ports, the weighted theorem, and
nonlocal braids remain open.

## 9. Exact proved/conditional boundary

The unconditional advances are:

1. the run-component/positive-guard equivalence, including endpoint runs;
2. the separated-collar overwrite theorem and the guarded deep-label atom;
3. the port-captured Hall theorem with exact deficiency;
4. deterministic weighted opposition pruning after scarce-first unit closure;
5. the rank-by-rank `B(k)+O(k)` implication under any one of those residual certificates;
6. the positive-density deletion, edited-site, and separated-collar lower bounds, with audited Gaussian constants;
7. the target-independent interval-colour capacity obstruction.

Exactly one constructive gate remains in this lane:

> **Positive-density PBBS/Pascal compiler gate.** Construct, for every `k`, one upper-complete `d(k)`-resident chronology whose physically forced facet/singleton rows admit exact unit closure and whose residual targets satisfy either (i) a port-captured target graph of Hall defect `O(k)`, (ii) the weighted good-candidate condition (5.2) with only `O(k)` omissions, or (iii) a positive-density collar/cross-collar target tiling with only `O(k)` duplicate or missing labels.

The Catalan all-depth support theorem alone does not prove this gate: deep owner flags are not automatically compiler sockets, and the density theorem shows that a sparse exterior-socket repair cannot suffice. Conversely, nothing proved here obstructs a positive-density Catalan rebundling or a genuinely nonlocal Pascal braid.

## 10. Independent audit

Three independent proof audits checked the theorem package before recording it.

* The run audit checked endpoint components, the finite eroded-run endpoint argument, source nonemptiness, collar separation, and the marker Hall bound. It identified the necessary scope `r-d>=3ell+1` for the guarded atom.
* The port audit checked Hall deficiency, forced-port contraction, the difference between universal rainbow safety and existence of one safe selector, the retrospective Dirac-LLL interpretation, and the residual-surplus correction to the colour-capacity bound.
* The density audit checked the `2d^2` ramp count, the `binom(d+1,2)` token incidence, both Gaussian constants, the hypothesis `h=o(W)`, and the exact scope of the separated-collar conclusion.

No SAT solving, finite exhaustive search, web access, or long-running local or remote computation was used.
