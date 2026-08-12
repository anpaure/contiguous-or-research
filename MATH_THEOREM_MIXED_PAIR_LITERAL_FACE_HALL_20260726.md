# Mixed pair frames: literal-face Hall expansion and the minimal frozen-bin obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, script, solver, or web input
is used.

## 0. Verdict

Let

\[
 \mathcal M=\binom{[2m]}m,
 \qquad W=|\mathcal M|,
 \qquad \mathcal L_q=\binom{[2m]}{m-q},
 \qquad N_q=|\mathcal L_q|,
 \qquad \rho_q={N_q\over W}.
 \tag{0.1}
\]

For the polynomial mixed-pair catalogue constructed from the size-bias
identity, the **literal union compatibility graph** at every certified
depth has the uniform target-set expansion

\[
 \boxed{
 |\Gamma_q^*(\mathcal Z)|
 \ge {1-\varepsilon\over1+\varepsilon}\,\rho_q^{-1}
             |\mathcal Z|
 \qquad(\mathcal Z\subseteq\mathcal L_q).}
 \tag{0.2}
\]

Here a target and middle owner are adjacent only when some catalogue frame
literally realizes the target by \(q\) distinct pair flips. For
\(\varepsilon=m^{-3}\),

\[
 \boxed{
 |\Gamma_q^*(\mathcal Z)|
 \ge\left(1+{q^2\over2m}\right)|\mathcal Z|}
 \tag{0.3}
\]

for all sufficiently large \(m\) and every \(q\ge1\) in the certified
range. Consequently every one-depth union graph satisfies Hall with
explicit slack and has a matching saturating every lower target. The upper
statement follows by complementation.

This is an actual target-set theorem, not a pair-type average.

It does not yet give the required common owner-frame assignment. Once every
owner has been frozen into one frame, the exact criterion is Hall in the
induced graph. With optional frame/type capacities \(c_{j,f}\), the exact
max-flow criterion is

\[
 \boxed{
 \sum_{j,f}\min\{c_{j,f},
       |\Gamma_{j,f}(\mathcal Z)|\}\ge|\mathcal Z|
 \quad\hbox{for every }\mathcal Z\subseteq\mathcal L_q.}
 \tag{0.4}
\]

Integral type-bin quotas alone do not imply (0.4). The minimal obstruction
is already a singleton. In a central bin, a target has exactly

\[
 d^{\rm tar}_{f,q}=2^q\binom{f+q}{q}
 \tag{0.5}
\]

compatible sources, whereas its integral source quota is

\[
 b_{j,f}=\exp((2\log2+o(1))m).
 \tag{0.6}
\]

For \(q\log(m/q)=o(m)\), in particular throughout
\(q\le O(\sqrt{m\log m})\),

\[
 d^{\rm tar}_{f,q}=\exp(o(m)),
 \qquad {d^{\rm tar}_{f,q}\over b_{j,f}}
          =\exp(-(2\log2+o(1))m).
 \tag{0.7}
\]

Thus a bin may have its exact quota and arbitrarily large cardinality slack
while containing no neighbor of a prescribed target. Pair-type quotas are
therefore exponentially too coarse to certify literal Hall.

The exact boundary is:

\[
 \boxed{
 \begin{array}{c}
 \text{unfrozen mixed-frame union: literal Hall is proved;}\\
 \text{one common frozen owner-frame partition: a hereditary Hall theorem
 remains necessary.}
 \end{array}}
 \tag{0.8}
\]

## 1. Literal pair-flip compatibility

Let

\[
 \mathscr P=(P_1,\ldots,P_J)
 \tag{1.1}
\]

be a catalogue of perfect matchings of \([2m]\). For a mask \(A\), let
\(f_j(A)\) be the number of full \(P_j\)-pairs in \(A\).

Fix \(T\in\mathcal L_q\) and \(X\in\mathcal M\). Write

\[
 T\sim_jX
 \tag{1.2}
\]

when

1. \(T\subset X\); and
2. every element of \(X\setminus T\) belongs to a split \(P_j\)-pair of
   \(X\).

Equivalently, the \(q\) elements of \(X\setminus T\) can be removed in any
order by \(q\) distinct pair flips. The resulting \((q+1)\)-vertex Johnson
path is contained in the up-set of \(T\), and its intersection is exactly
\(T\).

If \(f_j(T)=f\), then every compatible source has \(f_j(X)=f\). In frame
\(j\), the exact source and target orbit sizes are

\[
 V_f={m!\over f!^2(m-2f)!}\,2^{m-2f},
 \tag{1.3}
\]

\[
 T_{f,q}={m!\over f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.
 \tag{1.4}
\]

The literal compatibility graph between these two orbits is biregular with
degrees

\[
 d^{\rm src}_{f,q}=\binom{m-2f}{q},
 \qquad
 d^{\rm tar}_{f,q}=2^q\binom{f+q}{q}.
 \tag{1.5}
\]

Indeed, a source chooses the \(q\) split pairs to empty, while a target
chooses \(q\) of its \(f+q\) empty pairs and one endpoint in each. Hence

\[
 \lambda_{f,q}:={d^{\rm tar}_{f,q}\over d^{\rm src}_{f,q}}
 ={V_f\over T_{f,q}}
 ={2^q\binom{f+q}{q}\over\binom{m-2f}{q}}.
 \tag{1.6}
\]

## 2. The normalized literal incidence measure

Let \(\mathcal B\) be the balanced type interval from the mixed-pair
rounding theorem, and put

\[
 \tau=\Pr_{\pi_0}(F\notin\mathcal B),
 \qquad \alpha=J(1-\tau).
 \tag{2.1}
\]

Assume that the catalogue is \((\varepsilon,\mathcal B,H)\)-uniform, meaning
that every middle owner satisfies

\[
 a_X:=|\{j:f_j(X)\in\mathcal B\}|
       \le(1+\varepsilon)\alpha,
 \tag{2.2}
\]

and every \(T\in\mathcal L_q\), \(1\le q\le H\), satisfies

\[
 S_{T,q}:=
 \sum_{j:f_j(T)\in\mathcal B}\lambda_{f_j(T),q}
 \ge(1-\varepsilon){\alpha\over\rho_q}.
 \tag{2.3}
\]

Such a catalogue exists with \(J=m^{O(1)}\) and
\(\varepsilon=m^{-3}\) for \(H=O(\sqrt{m\log m})\). The proof is the exact
size-bias cancellation

\[
 \pi_q(f)\lambda_{f,q}=\rho_q^{-1}\pi_0(f)
 \tag{2.4}
\]

followed by Bernstein concentration and a union bound over all masks.

Give each literal edge \((T,X,j)\), where \(f_j(T)=f\in\mathcal B\), the
weight

\[
 w_q(T,X,j)={1\over d^{\rm src}_{f,q}}
 ={1\over\binom{m-2f}{q}}.
 \tag{2.5}
\]

The crucial point is that this normalization is exact on both sides.

### Lemma 2.1 (two exact marginals)

For a fixed target \(T\) and allowed frame \(j\),

\[
 \sum_{X:T\sim_jX}w_q(T,X,j)=\lambda_{f_j(T),q}.
 \tag{2.6}
\]

For a fixed middle owner \(X\) and allowed frame \(j\),

\[
 \sum_{T:T\sim_jX}w_q(T,X,j)=1.
 \tag{2.7}
\]

#### Proof

Equations (2.6) and (2.7) are (1.5) divided by
\(d^{\rm src}_{f,q}\). \(\square\)

Thus the size-biased target mass becomes ordinary unit source mass without
discarding literal face incidence.

## 3. Uniform Hall expansion in the unfrozen union

Define the balanced literal union graph

\[
 G_q^*=(\mathcal L_q,\mathcal M;E_q^*)
 \tag{3.1}
\]

by putting \(T X\in E_q^*\) if \(T\sim_jX\) in at least one frame \(j\)
with \(f_j(T)\in\mathcal B\). Multiple witnessing frames make only one
unlabelled edge.

### Theorem 3.1 (literal mixed-frame neighborhood theorem)

For every \(\mathcal Z\subseteq\mathcal L_q\), \(1\le q\le H\),

\[
 \boxed{
 |\Gamma_q^*(\mathcal Z)|
 \ge {1-\varepsilon\over1+\varepsilon}\,
       \rho_q^{-1}|\mathcal Z|.}
 \tag{3.2}
\]

#### Proof

Sum the weights (2.5) of all frame-labelled edges leaving \(\mathcal Z\).
By (2.3) and (2.6),

\[
 \begin{aligned}
 I_q(\mathcal Z)
 &:=\sum_{T\in\mathcal Z}
       \sum_{j:f_j(T)\in\mathcal B}
       \sum_{X:T\sim_jX}w_q(T,X,j)\\
 &=\sum_{T\in\mathcal Z}S_{T,q}\\
 &\ge(1-\varepsilon){\alpha\over\rho_q}|\mathcal Z|.
 \end{aligned}
 \tag{3.3}
\]

Now sum from the owner side. Only owners in
\(\Gamma_q^*(\mathcal Z)\) contribute. For one owner and one allowed frame,
the contribution from the restricted target family is at most its full
mass one in (2.7). Therefore (2.2) gives

\[
 I_q(\mathcal Z)
 \le\sum_{X\in\Gamma_q^*(\mathcal Z)}a_X
 \le(1+\varepsilon)\alpha
           |\Gamma_q^*(\mathcal Z)|.
 \tag{3.4}
\]

Comparing (3.3) and (3.4) proves (3.2). Notice that repeated frame witnesses
cause no problem: they are retained in the weighted double count but each
owner-frame contributes at most one. \(\square\)

The theorem is stronger than the orbit calculation
\(V_f/T_{f,q}=\lambda_{f,q}\): it holds for every target family, including
families cutting arbitrarily across all pair types in all frames.

### Corollary 3.2 (explicit growing-depth expansion)

With \(\varepsilon=m^{-3}\), for all sufficiently large \(m\),

\[
 |\Gamma_q^*(\mathcal Z)|
 \ge\left(1+{q^2\over2m}\right)|\mathcal Z|
 \tag{3.5}
\]

for every nonempty \(\mathcal Z\subseteq\mathcal L_q\) and
\(1\le q\le H\).

#### Proof

Exactly,

\[
 \rho_q^{-1}
 ={W\over N_q}
 =\prod_{i=0}^{q-1}{m+i+1\over m-i}
 =\prod_{i=0}^{q-1}
       \left(1+{2i+1\over m-i}\right).
 \tag{3.6}
\]

Since a product of numbers \(1+x_i\), \(x_i\ge0\), is at least
\(1+\sum_i x_i\),

\[
 \rho_q^{-1}
 \ge1+\sum_{i=0}^{q-1}{2i+1\over m}
 =1+{q^2\over m}.
 \tag{3.7}
\]

Combining (3.2) and (3.7), the surplus over one is at least

\[
 {q^2/m-\varepsilon q^2/m-2\varepsilon\over1+\varepsilon}.
 \tag{3.8}
\]

For \(q\ge1\) and \(\varepsilon=m^{-3}\), this is at least
\(q^2/(2m)\) for all sufficiently large \(m\). \(\square\)

### Corollary 3.3 (one-depth literal matching)

For every \(1\le q\le H\), the graph \(G_q^*\) has a matching saturating
all \(N_q\) targets.

#### Proof

Equation (3.5) implies Hall's inequality. \(\square\)

Every matched edge has at least one witnessing pair frame, so the matching
can be decorated by a literal frame and a literal set of \(q\) pair flips.
The conclusion is integral. It uses no fractional targets and no abstract
type slots.

The matchings supplied for different \(q\)'s need not choose the same frame
for a common middle owner, and their deleted sets need not be nested. This
is why Corollary 3.3 is not yet the Stage-B compiler.

## 4. Exact max-flow criterion after freezing owner frames

Let

\[
 \phi:\mathcal M\longrightarrow[J]
 \tag{4.1}
\]

be an integral owner-frame assignment, and put

\[
 A_{j,f}=\{X:\phi(X)=j, f_j(X)=f\}.
 \tag{4.2}
\]

For \(\mathcal Z\subseteq\mathcal L_q\), define the actual frozen-bin
neighborhood

\[
 \Gamma_{j,f}^{\phi}(\mathcal Z)
 =\{X\in A_{j,f}:T\sim_jX
       \text{ for some }T\in\mathcal Z\}.
 \tag{4.3}
\]

Suppose at most \(c_{j,f}\le|A_{j,f}|\) depth-\(q\) targets may be routed
through bin \((j,f)\). This includes optional reserved source slots.

### Theorem 4.1 (capacitated literal Hall criterion)

There is an integral matching of every target in \(\mathcal L_q\) to a
distinct compatible frozen owner, using at most \(c_{j,f}\) owners from
each bin, if and only if

\[
 \boxed{
 \sum_{j,f}\min\{c_{j,f},
       |\Gamma_{j,f}^{\phi}(\mathcal Z)|\}
       \ge|\mathcal Z|
 \quad\hbox{for every }\mathcal Z\subseteq\mathcal L_q.}
 \tag{4.4}
\]

#### Proof

Construct the network

\[
 s\longrightarrow T\longrightarrow X
 \longrightarrow (j,f)\longrightarrow t.
 \tag{4.5}
\]

The first and third displayed arcs have capacity one; the last arc from bin
\((j,f)\) to \(t\) has capacity \(c_{j,f}\). Include \(T\to X\) exactly
when \(X\in A_{j,f}\) and \(T\sim_jX\).

The usable rank of a right-side set \(U\subseteq\mathcal M\) in this
network is the partition-matroid rank

\[
 r(U)=\sum_{j,f}\min\{c_{j,f},|U\cap A_{j,f}|\}.
 \tag{4.6}
\]

The max-flow/min-cut theorem, equivalently the Hall--Rado theorem for this
partition matroid, says that all targets can be saturated exactly when

\[
 r(\Gamma^{\phi}(\mathcal Z))\ge|\mathcal Z|
 \tag{4.7}
\]

for every target family. Substituting (4.3) into (4.6) gives (4.4). All
capacities are integral, so a maximum flow can be chosen integral. \(\square\)

If \(c_{j,f}=|A_{j,f}|\), (4.4) reduces to ordinary Hall in the union of
the frozen-frame graphs:

\[
 \sum_{j,f}|\Gamma_{j,f}^{\phi}(\mathcal Z)|
 =|\Gamma^{\phi}(\mathcal Z)|\ge|\mathcal Z|.
 \tag{4.8}
\]

If the targets themselves have already been assigned to bins, with family
\(B_{j,f,q}\) in bin \((j,f)\), the flows split by bin. The necessary and
sufficient conditions are then

\[
 \boxed{
 |\Gamma_{j,f}^{\phi}(\mathcal Z)|\ge|\mathcal Z|
 \quad
 (\mathcal Z\subseteq B_{j,f,q})}
 \tag{4.9}
\]

for every \(j,f\). Equation (4.9) is the precise literal replacement for
the cardinality inequality \(|B_{j,f,q}|\le|A_{j,f}|\).

## 5. Why integral type quotas do not imply literal Hall

Fix a balanced frame/type bin \((j,f)\) and a target
\(T\in\mathcal L_{j,f,q}\). Its full literal neighborhood inside that bin
has the exact size

\[
 |\Gamma_{j,f,q}(T)|
 =d^{\rm tar}_{f,q}
 =2^q\binom{f+q}{q}.
 \tag{5.1}
\]

Let \(b_{j,f}\) be one of the integral source quotas from the mixed owner
allocation. With \(\alpha=J(1-\tau)\) and
\(\varepsilon=m^{-3}\), it satisfies

\[
 {V_f\over(1+\varepsilon)\alpha}-1
 \le b_{j,f}\le
 {V_f\over(1-\varepsilon)\alpha}+1.
 \tag{5.2}
\]

### Proposition 5.1 (minimal quota-invisible Hall obstruction)

Whenever

\[
 b_{j,f}\le V_f-d^{\rm tar}_{f,q},
 \tag{5.3}
\]

there is a source subset \(A_{j,f}\subseteq\mathcal M_{j,f}\) of the exact
quota size \(b_{j,f}\) such that

\[
 \Gamma_{j,f,q}(T)\cap A_{j,f}=\varnothing.
 \tag{5.4}
\]

Consequently, assigning \(T\) to this bin violates (4.9) on the singleton
family \(\{T\}\), despite the exact equality \(|A_{j,f}|=b_{j,f}\).

#### Proof

By (5.1), the complement of the target neighborhood inside the source
orbit has size \(V_f-d^{\rm tar}_{f,q}\). Under (5.3), choose any
\(b_{j,f}\) sources from that complement. Then (5.4) is immediate. \(\square\)

This is minimal in two senses: the Hall witness has one target, and no
smaller amount of information than its literal neighborhood can detect it.

### Proposition 5.2 (exact asymptotic scale of the singleton obstruction)

Suppose

\[
 f={m\over4}+O(\sqrt{m\log m}),
 \qquad q=o(m),
 \tag{5.5}
\]

and \(J=m^{O(1)}\). Then

\[
 \log V_f=2m\log2-O(\log m),
 \tag{5.6}
\]

where the implicit constant depends on the width in (5.5), while

\[
 \log d^{\rm tar}_{f,q}
 =q\log{em\over2q}
   +O\left({q^2\over m}+\log(q+1)
            +{q|f-m/4|\over m}\right).
 \tag{5.7}
\]

In particular, if

\[
 q\log(m/q)=o(m),
 \tag{5.8}
\]

then

\[
 {d^{\rm tar}_{f,q}\over b_{j,f}}
 =\exp(-(2\log2+o(1))m).
 \tag{5.9}
\]

Hence (5.3) holds with exponentially large slack throughout
\(q\le O(\sqrt{m\log m})\).

#### Proof

The local Stirling expansion of (1.3) in the central type window gives
(5.6). From (5.1),

\[
 d^{\rm tar}_{f,q}
 =2^q{(f+q)_{\underline q}\over q!}.
 \tag{5.10}
\]

Stirling's formula for \(q!\), followed by expansion of
\(\sum_{i=1}^q\log(f+i)\) around \(m/4\), gives (5.7). Under (5.8), its
right side is \(o(m)\). Equations (5.2), (5.6), and polynomiality of
\(\alpha\) give

\[
 \log b_{j,f}=2m\log2-O(\log m).
 \tag{5.11}
\]

Subtracting proves (5.9), and therefore (5.3). \(\square\)

Proposition 5.1 concerns what the quota data can certify. It does not claim
that every global owner partition has such an isolated target. The positive
successor theorem must choose the owner partition specifically to prevent
all these singleton cuts, and then all higher Hall cuts, simultaneously.

## 6. Exact residual gate

The results separate three levels which must not be conflated.

1. **Unfrozen union.** Theorem 3.1 proves uniform literal expansion and an
   integral target matching at every depth.

2. **Frozen owner frames.** Theorem 4.1 gives the exact capacitated Hall
   criterion. No type census remains in it; it depends on actual target
   neighborhoods.

3. **One physical cycle system.** In addition to satisfying (4.4) at every
   lower and upper depth, the matched targets belonging to one owner must
   form nested prefixes, and owner-frame classes must be unions of complete
   isometric cycles except for the permitted residual.

Accordingly the next sufficient statement is now sharply formulated.

> **Hereditary mixed-frame assignment theorem.** There is one integral
> owner-frame partition \(\phi\), with the prescribed polynomial-catalogue
> type quotas up to the available depth-one reserve, such that for every
> \(q\le H\) and every target family \(\mathcal Z\),
> \[
>  \sum_{j,f}\min\{c_{j,f,q},
>       |\Gamma_{j,f}^{\phi}(\mathcal Z)|\}
>       \ge|\mathcal Z|,
> \]
> simultaneously for the lower and upper graphs.

Theorem 3.1 proves this before \(\phi\) is frozen. Propositions 5.1--5.2
show why preserving only integral type-bin quotas cannot prove it. Thus the
remaining constant-one problem is a dependent owner-frame rounding theorem
with hereditary literal-neighborhood control, followed by nested-prefix and
cycle bundling.
