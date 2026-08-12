# Direct edgewise dual transversals: exact matching-loss rank and the complete \(n=3\) census

Date: 2026-07-31  
Status: theorem and complete finite classification. Two independent exhaustive implementations agree on every shared aggregate and rediscover the same positive physical support; one independent consumer replays both encodings exactly. The all-\(n\) direct recursive forest theorem (DERF) remains open.

## 0. Verdict

For an oriented Catalan linear forest \(F\), the two direct edgewise pullback matroids admit an exact Hall-loss rank formula. If \(E=E(F)\), \(|E|=N\), and \(\tau,\eta:E\to X\) are the tail and head injections, define

\[
\begin{aligned}
 \kappa_F^-(S)
   &=P-\nu\bigl(G_F^-[W^-,X\setminus\tau(S)]\bigr),\\
 \kappa_F^+(S)
   &=P-\nu\bigl(G_F^+[W^+,X\setminus\eta(S)]\bigr).
\end{aligned}                                                   \tag{0.1}
\]

Then

\[
 r_{\mathcal A_F^{\rm dir}}(S)=|S|-\kappa_F^-(S),
 \qquad
 r_{\mathcal B_F^{\rm dir}}(S)=|S|-\kappa_F^+(S).               \tag{0.2}
\]

Consequently, with

\[
 p=\frac CN=\frac{2(2n+1)}{n(n+2)},
 \qquad q=1-p=\frac{N-C}{N},                                    \tag{0.3}
\]

the exact uniform-marginal tests are

\[
 p\mathbf 1_E\in B(\mathcal A_F^{\rm dir})
 \iff
 \kappa_F^-(S)\le q|S|\quad(S\subseteq E),                     \tag{0.4}
\]

and dually for \(\mathcal B_F^{\rm dir}\). The exact direct common-basis test is

\[
 \boxed{
 \kappa_F^-(S)+\kappa_F^+(E\setminus S)\le N-C
 \quad(S\subseteq E).}                                          \tag{0.5}
\]

At \(n=3\), the complete catalogue consists of \(458{,}544\) undirected Catalan forests and \(9{,}549{,}888\) coherent component orientations. The exact results are:

* \(7{,}136{,}784\) orientations have a direct common basis;
* \(1{,}242{,}576\) are uniform-marginal on the upper shore, and separately the same number are uniform-marginal on the lower shore;
* \(364{,}176\) are uniform-marginal on both shores;
* the minimum individual direct rank density over the whole catalogue is \(2/3\);
* the maximum possible simultaneous minimum density is \(14/15=C/N\);
* a both-uniform forest with a literal joint direct physical extension exists.

The last assertion is stronger than incidence: its two direct side representatives satisfy both outer palettes, the inherited anchor caps, physical degree at most two, and the complete contracted graphic row. It is an actual \(n=3\to4\) DERF base. The census does **not** prove that every both-uniform orientation physically extends, because physical enumeration stopped after the first positive witness.

## 1. Parameters and direct occurrence graphs

Let \(|\Omega|=2n\), and put

\[
 M=\binom{2n}{n},\qquad
 N=\binom{2n}{n-1},\qquad
 P=\binom{2n}{n-2},\qquad
 C=M-P.                                                         \tag{1.1}
\]

An oriented child atom is

\[
 e=(L_e,U_e,t_e,h_e),\qquad
 L_e=t_e\cap h_e,\quad U_e=t_e\cup h_e.                         \tag{1.2}
\]

The child forest has \(N\) edges on the \(M\) middle vertices. Its component orientation makes

\[
 \tau(e)=t_e,\qquad \eta(e)=h_e                                \tag{1.3}
\]

injections \(E\to X=\binom\Omega n\).

The upper direct occurrence graph \(G_F^-\) has outer shore
\(W^-=\binom\Omega{n+2}\), middle shore \(X\), and the occurrence

\[
 L_e+x\longleftrightarrow U_e+x
 \qquad(x\notin U_e).                                           \tag{1.4}
\]

The lower direct occurrence graph \(G_F^+\) is its deletion dual between
\(W^+=\binom\Omega{n-2}\) and \(X\):

\[
 L_e-x\longleftrightarrow U_e-x
 \qquad(x\in L_e).                                              \tag{1.5}
\]

Both outer shores have order \(P\). The direct note proves that each outer vertex has occurrence-degree \(n+2\), each middle vertex \(v\) has occurrence-degree \(n-d_F(v)\), and both unpunctured graphs saturate their outer shores.

Let \(\mathcal T_F^-\) be the transversal matroid on \(X\) represented by \(G_F^-\). Pull the restriction of \((\mathcal T_F^-)^*\) to the tail image back along \(\tau\); this is \(\mathcal A_F^{\rm dir}\). Define \(\mathcal B_F^{\rm dir}\) from \(G_F^+\) and \(\eta\).

The ranks of these pullbacks are at most \(C\), not automatically \(C\). Rank \(C\) is itself a terminal-bank matching assertion. This corrects the only scope ambiguity in the first version of the direct recursion note.

## 2. Exact matching-loss rank theorem

### Theorem 2.1

For every \(S\subseteq E\),

\[
 \kappa_F^-(S)
 =\max_{\mathcal U\subseteq W^-}
 \bigl(|\mathcal U|-|N(\mathcal U)\setminus\tau(S)|\bigr),      \tag{2.1}
\]

and

\[
 r_{\mathcal A_F^{\rm dir}}(S)=|S|-\kappa_F^-(S).              \tag{2.2}
\]

The corresponding identities hold on the head shore.

#### Proof

The maximum matching in \(G_F^-[W^-,X\setminus\tau(S)]\) has size

\[
 P-\max_{\mathcal U\subseteq W^-}
 \bigl(|\mathcal U|-|N(\mathcal U)\setminus\tau(S)|\bigr)
\]

by the deficiency form of Hall's theorem, proving (2.1). Since
\(r_{\mathcal T_F^-}(X)=P\), dual rank gives

\[
\begin{aligned}
 r_{\mathcal A_F^{\rm dir}}(S)
 &=|S|-P+r_{\mathcal T_F^-}(X\setminus\tau(S))\\
 &=|S|-\kappa_F^-(S).
\end{aligned}
\]

The head-shore proof is identical. \(\square\)

### Corollary 2.2 (uniform marginal iff matching interdiction is small)

Equation (0.4) is necessary and sufficient.

#### Proof

The base-polytope inequalities are
\(p|S|\le r_{\mathcal A_F^{\rm dir}}(S)\). Applying (2.2) gives
\(\kappa_F^-(S)\le(1-p)|S|=q|S|\). At \(S=E\), the inequality also forces rank \(C\): the pullback rank is at most \(C\), while the displayed inequality gives at least \(C\). \(\square\)

Equivalently, after contracting the terminal bank
\(Z^-=X\setminus\tau(E)\), the remaining primal terminal matroid must be uniformly dense at density \(q\). This is a substantially stronger demand than unpunctured one-sided Hall.

### Corollary 2.3 (exact common-basis cut)

The largest common independent set has size

\[
 \max|I|
 =N-\max_{S\subseteq E}
 \bigl(\kappa_F^-(S)+\kappa_F^+(E\setminus S)\bigr).            \tag{2.3}
\]

Thus a common basis of order \(C\) exists exactly when (0.5) holds.

#### Proof

Edmonds' matroid-intersection formula and (2.2) give

\[
\begin{aligned}
 \max|I|
 &=\min_{S\subseteq E}
 \bigl(r_{\mathcal A}(S)+r_{\mathcal B}(E\setminus S)\bigr)\\
 &=N-\max_{S\subseteq E}
 \bigl(\kappa_F^-(S)+\kappa_F^+(E\setminus S)\bigr).
\end{aligned}
\]

Each pullback has rank at most \(C\), so the maximum is \(C\) precisely under (0.5). \(\square\)

This is the weakest exact all-\(n\) incidence gate visible from the direct construction. Proving both individual uniform-marginal inequalities is sufficient but not necessary.

## 3. A path-sensitive all-\(n\) cut bound

The general occurrence-degree argument can be sharpened using the orientation of the child paths.

For \(S\subseteq E\), let \(\iota^-(S)\) be the number of selected edges whose tail is an initial endpoint of its oriented child path. Choose a Hall set \(\mathcal U\subseteq W^-\) attaining (2.1), and put

\[
 d=\kappa_F^-(S),\qquad
 g=|N(\mathcal U)\setminus\tau(S)|.                             \tag{3.1}
\]

Then \(|\mathcal U|=d+g\).

### Theorem 3.1 (path-sensitive deficiency inequality)

For every such \(S,\mathcal U\),

\[
 \boxed{(n+2)d+2g\le(n-2)|S|+\iota^-(S).}                      \tag{3.2}
\]

Consequently,

\[
 r_{\mathcal A_F^{\rm dir}}(S)
 \ge
 \left\lceil\frac{4|S|-\iota^-(S)+2g}{n+2}\right\rceil
 \ge
 \left\lceil\frac{3|S|}{n+2}\right\rceil.                       \tag{3.3}
\]

#### Proof

There are exactly \((n+2)(d+g)\) occurrences leaving \(\mathcal U\). The \(g\) surviving middle neighbours receive at most \(n\) occurrences each. A tail \(t_e\) receives \(n-1\) occurrences when it is the initial endpoint of its child path and \(n-2\) otherwise, because its child degree is respectively one or two. Hence the deleted tail bank \(\tau(S)\) receives at most

\[
 (n-2)|S|+\iota^-(S)
\]

occurrences. Therefore

\[
 (n+2)(d+g)\le ng+(n-2)|S|+\iota^-(S),
\]

which is (3.2). Substitute \(r(S)=|S|-d\), and then use
\(\iota^-(S)\le|S|\), to obtain (3.3). \(\square\)

The required uniform density is

\[
 p|S|=\frac{4|S|+2|S|/n}{n+2}.                                 \tag{3.4}
\]

Thus any violation of the uniform-marginal inequality must have a **near-starved Hall witness** satisfying

\[
 \boxed{2g<\iota^-(S)+\frac{2|S|}{n}.}                         \tag{3.5}
\]

Conversely, excluding (3.5) for every maximum-deficiency witness proves the upper direct uniform-marginal theorem. The head version is identical. If the \(g\)-term is discarded, degree counting misses the target before integer rounding by exactly

\[
 \frac{\iota^-(S)+2|S|/n}{n+2}.                                \tag{3.6}
\]

This explains why bare biregularity cannot prove DERF: only cuts with a very small surviving neighbour bank remain dangerous, but those cuts are not forbidden by degrees alone.

## 4. The \(n=3\) collapse

At \(n=3\),

\[
 (M,N,P,C)=(20,15,6,14),\qquad p=\frac{14}{15},\quad q=\frac1{15}. \tag{4.1}
\]

Because \(\kappa\) is integral and monotone, (0.4) becomes

\[
 \kappa(S)=0\qquad(S\subsetneq E),\qquad \kappa(E)=1.           \tag{4.2}
\]

Equivalently, it is enough to check the fifteen co-singletons
\(E\setminus\{e\}\). If

\[
 Z^-=X\setminus\tau(E),\qquad |Z^-|=5,                         \tag{4.3}
\]

then every six-element terminal bank

\[
 Z^-\cup\{\tau(e)\}                                            \tag{4.4}
\]

must perfectly match the six upper outer colours. Hence

\[
 p\mathbf1_E\in B(\mathcal A_F^{\rm dir})
 \iff
 \mathcal A_F^{\rm dir}=U_{14,15}.                             \tag{4.5}
\]

The same holds on the head shore. This reduces the full uniform test to thirty exact six-by-six matching tests per oriented forest.

For density enumeration one can alternatively inspect only the \(63\) nonempty outer-shore subsets. Define first

\[
 g_j=\min\{|S|:\kappa(S)\ge j\}.                                \tag{4.6}
\]

The deficiency form of Hall gives the equivalent outer-cut formula

\[
 g_j=\min_{\substack{\mathcal U\subseteq W^-\\
 |N(\mathcal U)\setminus\tau(E)|\le|\mathcal U|-j}}
 \bigl(|N(\mathcal U)|-|\mathcal U|+j\bigr),                    \tag{4.7}
\]

with \(g_j=+\infty\) when the indexing family is empty. Then

\[
 \min_{\varnothing\ne S\subseteq E}\frac{r(S)}{|S|}
 =1-\max_j\frac{j}{g_j}.                                      \tag{4.8}
\]

This is the cut compression used by both exhaustive implementations; it does not sample edge subsets.

## 5. Complete catalogue and independent agreement

The catalogue enumerates, without quotienting by coordinate symmetry:

1. one atom for each of the fifteen rank-two lower colours;
2. each rank-four upper colour exactly once;
3. physical rank-three degree at most two and no physical cycle;
4. both orientations of every nontrivial path component.

The first three rows produce exactly \(458{,}544\) undirected Catalan forests. The fourth produces exactly \(9{,}549{,}888\) coherent orientations.

Two independently written C++ enumerators agree exactly on the following shared counts:

\[
\begin{array}{l|r}
\text{quantity}&\text{count}\\ \hline
\text{undirected forests}&458{,}544\\
\text{coherent orientations}&9{,}549{,}888\\
\text{orientations with at least one common basis}&7{,}136{,}784\\
\text{orientations with no common basis}&2{,}413{,}104\\
\text{upper-uniform orientations}&1{,}242{,}576\\
\text{lower-uniform orientations}&1{,}242{,}576\\
\text{both-uniform orientations}&364{,}176.
\end{array}                                                     \tag{5.1}
\]

The exact number of direct common bases has histogram

\[
\begin{array}{c|rrrrrrrr}
b&0&1&2&3&4&5&6&7\\ \hline
\#&2413104&738000&1319760&990720&780480&1206288&231840&306000\\[2mm]
b&8&9&10&11&12&13&14&15\\ \hline
\#&314640&156240&195840&128880&138960&190800&74160&364176.
\end{array}                                                     \tag{5.2}
\]

The independent implementation additionally records:

\[
\begin{aligned}
 &458{,}544 &&\text{undirected forests have some common-basis orientation},\\
 &160{,}536 &&\text{undirected forests have some both-uniform orientation}.
\end{aligned}                                                   \tag{5.3}
\]

Thus every undirected \(n=3\) Catalan forest can be oriented to pass the direct incidence common-basis row, although only a proper subfamily can be oriented to make both direct pullbacks uniform.

## 6. Exact density extrema and literal cuts

Across all \(9{,}549{,}888\) orientations, the minimum individual shore density is

\[
 \boxed{\min_{F,\pm}\min_{\varnothing\ne S\subseteq E}
 \frac{r_{\mathcal A_F^\pm}(S)}{|S|}=\frac23.}                  \tag{6.1}
\]

No smaller density occurs. There are \(3{,}600\) orientations whose two density coordinates are simultaneously \((2/3,2/3)\).

One exact upper-shore witness is forest 5, orientation 7 in the independent canonical enumeration. For the singleton outer colour

\[
 V=0x3e,\qquad N(V)=\{0x1a,0x1c,0x26\},                        \tag{6.2}
\]

all three neighbours are tails of the edge set

\[
 S=\{5,9,11\}.                                                  \tag{6.3}
\]

Deleting \(\tau(S)\) isolates \(V\). The remaining five outer colours still match through

\[
\begin{aligned}
0x1f&\mapsto0x07,&0x2f&\mapsto0x0b,&0x37&\mapsto0x13,\\
0x3b&\mapsto0x19,&0x3d&\mapsto0x25.
\end{aligned}                                                   \tag{6.4}
\]

Hence

\[
 \kappa_F^-(S)=1,\qquad r_{\mathcal A_F^{\rm dir}}(S)=3-1=2.  \tag{6.5}
\]

One exact lower-shore witness is forest 3, orientation 7. For the singleton outer colour

\[
 A=0x01,\qquad N(A)=\{0x0d,0x13,0x23\},                        \tag{6.6}
\]

the neighbours are precisely the heads of

\[
 S=\{5,6,11\}.                                                  \tag{6.7}
\]

After their deletion, the other five outer colours match through

\[
\begin{aligned}
0x02&\mapsto0x07,&0x04&\mapsto0x15,&0x08&\mapsto0x0b,\\
0x10&\mapsto0x1a,&0x20&\mapsto0x25.
\end{aligned}                                                   \tag{6.8}
\]

Thus \(\kappa_F^+(S)=1\) and the rank density is \(2/3\).

At the other extreme, no direct pullback can have minimum density exceeding \(C/N=14/15\). The catalogue attains this simultaneously on both shores exactly \(364{,}176\) times. In each such case both direct pullbacks are \(U_{14,15}\).

For comparison, the previously authenticated chained base is not uniform: its exact upper obstruction is

\[
 S=\{0,1,5,11\},\qquad
 \tau(S)=\{0x13,0x0d,0x0e,0x07\}=N(0x1f),                     \tag{6.9}
\]

giving density \(3/4\); its lower minimum is \(10/11\). Nevertheless it has four common bases, retained-edge ids \(0,1,5,11\). Uniformity is therefore a useful sufficient state, not a necessary direct incidence state.

## 7. A both-uniform literal physical extension

The first exhaustive producer finds the following both-uniform forest. The corrected independent producer rediscovers the same child atom set and the same six physical edges and occurrence labels on each side, up to order. Its source explicitly deduplicates parallel occurrence labels only when they induce the same direct cell and the same undirected physical edge; no per-parent capacity row distinguishes such labels. Masks below are hexadecimal.

\[
\begin{array}{c|cccc}
e&L_e&U_e&t_e&h_e\\ \hline
0&03&0f&0b&07\\
1&05&17&07&15\\
2&06&1e&0e&16\\
3&09&1b&19&0b\\
4&0a&2e&2a&0e\\
5&0c&1d&0d&1c\\
6&11&33&31&13\\
7&12&36&16&32\\
8&14&3c&1c&34\\
9&18&39&38&19\\
10&21&27&25&23\\
11&22&2b&23&2a\\
12&24&35&34&25\\
13&28&2d&2c&29\\
14&30&3a&32&38.
\end{array}                                                     \tag{7.1}
\]

Take \(Q=E\setminus\{1\}\). One upper direct occurrence set is

\[
 (e,x)=(8,0),(2,0),(10,3),(9,1),(7,0),(2,5),                   \tag{7.2}
\]

and one lower direct occurrence set is

\[
 (e,x)=(0,1),(9,3),(10,0),(2,2),(5,3),(4,1).                  \tag{7.3}
\]

An independent consumer reconstructs the graphs rather than trusting the producer and verifies:

\[
\begin{array}{c|ccc}
\text{graph}&\Delta&\beta&\#\text{components}\\ \hline
\text{child physical forest}&2&0&5\\
\text{complete uncontracted variable support}&2&0&9.
\end{array}                                                     \tag{7.4}
\]

It also recomputes all \(2^{15}\) rank inequalities on each shore, obtains minimum density \(14/15\), and verifies that all fifteen co-singletons are bases. The side palettes, inherited punctures and anchor caps pass. Contracting the fixed forest fragments preserves cycle rank, so the uncontracted forest test also proves the contracted graphic row. Therefore Theorem 3.1 of the direct recursion note gives a literal joint physical strict extension.

The second exhaustive implementation independently rediscovers this physical support. Applying the same independent consumer to that second encoding again gives \(\Delta=2\) and \(\beta=0\). This is a positive existence theorem, not a count of all physically extendable orientations.

## 8. Consequences for DERF

The finite result settles the direct \(n=3\) base strongly:

1. direct common bases are abundant but not automatic for an orientation;
2. every undirected \(n=3\) forest has at least one good common-basis orientation;
3. simultaneous uniform marginals are achievable;
4. simultaneous uniform marginals are compatible with the literal physical partition/graphic row.

What remains for all \(n\) is not another one-sided Hall theorem. The exact nested targets are:

\[
 \kappa_F^-(S)+\kappa_F^+(E\setminus S)\le N-C              \tag{8.1}
\]

for some coherent orientation, followed by representatives satisfying the anchor partitions and contracted graphic row. The stronger uniform route asks separately for

\[
 \kappa_F^\pm(S)\le\frac{N-C}{N}|S|.                           \tag{8.2}
\]

Theorem 3.1 shows that any failure of (8.2) is confined to a near-starved cut (3.5). This is the concrete all-\(n\) rank inequality and obstruction class exposed by the census. No present argument excludes those cuts recursively, and no claim is made about residence, deep shadows, the compiler, or the full formula \(\nu(k)=B(k)\).

## 9. Audit and artifacts

Primary complete producer:

    scratch/census_catalan_direct_edgewise_n3_all_forests_20260731.cpp
      SHA-256 8dbdfcaea43a5f58c97cdb9ed0abdde7d91f8d6e43e4b2f38b6ec95ecb310899
    scratch/catalan_direct_edgewise_n3_all_forests_20260731.audit.json
      SHA-256 8ab02b0592e7609bc44aea25a72fb67c780d7334bc48ffe58cf16d5ed894242e
    scratch/catalan_direct_edgewise_n3_all_forests_20260731.run.log
      SHA-256 7a7e76b909056ea47271df8e9346f8edaec70c6592ccecee91ac8c847e950c70

Independent complete producer:

    scratch/enumerate_catalan_direct_edgewise_n3_all_forests_20260731.cpp
      SHA-256 87c86fbae95742de13a456deadf9991e7b8315693aec80101ea6467b6fea5423
    scratch/catalan_direct_edgewise_n3_all_forests_20260731.independent.v2.json
      SHA-256 011f8dea68963daef0ad57acf7b421a5f642a1a22b2ccc64974dc3fc3ada4655
    scratch/catalan_direct_edgewise_n3_all_forests_20260731.independent.v2.run.log
      SHA-256 f83cf79403f4fb7d53084e22dedcd7f17710379e24b39b9428e10661875f8b49

Independent positive-witness replay, applied separately to both producer outputs:

    scratch/audit_catalan_direct_edgewise_n3_uniform_physical_witness_20260731.py
      SHA-256 cb524c1c3a483453e79a30e551886132142d4af7f4dec53bed51e7964589cd57
    scratch/catalan_direct_edgewise_n3_uniform_physical_witness_20260731.replay.json
      SHA-256 7ffbf20ebb2f720eef71655b3f58d4f2da2d25f579ddce5754813eb456669c53
    scratch/catalan_direct_edgewise_n3_uniform_physical_witness_20260731.independent.v2.replay.json
      SHA-256 a115261a24654efee3edceeaed803e1c6e78874e412fc414384c7bb79d6036c5

Cross-census audit:

    scratch/audit_catalan_direct_edgewise_n3_two_censuses_20260731.py
      SHA-256 df1a2c05389944c6454d7035d7889926a0ad6b2764e38731385732445bc30c98
    scratch/catalan_direct_edgewise_n3_two_censuses_20260731.crossaudit.v2.json
      SHA-256 41058a94bd9d5261db585b3507b09dbff4468aacf97b9cd1bb4a387c3e41b0a8

Both exhaustive jobs were launched on one H100 CPU core, at nice level 15, under a 2 GiB virtual-memory cap and a two-hour timeout. The frozen run logs authenticate completion in \(15.12\) and \(17.29\) seconds, maximum resident set size \(3584\) KiB, and exit status zero; the nice and virtual-memory settings are launch provenance rather than fields echoed by those logs. The corrected independent run retained assertions. No exhaustive job ran on the local machine.
