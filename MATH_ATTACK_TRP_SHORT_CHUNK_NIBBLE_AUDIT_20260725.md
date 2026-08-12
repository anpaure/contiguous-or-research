# Short TRP chunks: the growing-rank nibble and its exact missing moment

Date: 2026-07-25

Pure mathematics only. No fixed-uniformity matching theorem, computation,
solver, or web input is used.

## 0. Verdict

For the short-chunk TRP owner hypergraph, the audited parameters are

\[
 r=\ell+1,\qquad
 \varepsilon=O\left(\frac{H+\ell}{m}\right)=o(1),
 \qquad
 \delta:=\frac{\Delta_2}{D}=O(m^{-2}),                \tag{0.1}
\]

with

\[
 Q\ll\ell\ll m.
\]

Hence

\[
 r^2\delta=O(\ell^2/m^2)=o(1).                        \tag{0.2}
\]

This is enough for a rigorous first nibble bite, but it is **not enough
information to justify iteration**. The obstruction is exact: after one
wasteful bite, the second moment of a residual pair link contains

\[
 (1-p)^{-|\Gamma(e)\cap\Gamma(f)|}                    \tag{0.3}
\]

for two candidate chunks \(e,f\). If they share \(k\) owners, this factor
can be

\[
 \exp\{\Theta(hk/r)\},                                \tag{0.4}
\]

where \(p=h/(rD)\). The pair-codegree estimate controls the unweighted
second overlap moment

\[
 \sum_{e,f}|e\cap f|(|e\cap f|-1),                    \tag{0.5}
\]

but the recurrence also contains its \(k\)-weighted version, equivalently
a third overlap moment. In the worst case (0.2) permits \(k\asymp r\).
The resulting pair-energy multiplier is \(1+O(h)\), not
\(1+O(h/r)\). Since a constant reduction of the uncovered population
requires \(\Theta(r/h)\) bites, this error is not summable.

Long common cores genuinely occur in the TRP path family: two shifted
length-\(\ell\) subchunks of one repetition-free length-\((\ell+1)\) rotor
walk share exactly \(\ell-1\) owners. Their *frequency* may be tiny enough
to save the nibble, but that frequency is a higher-overlap statistic and
does not follow from \(\Delta_2/D=O(m^{-2})\).

Thus the precise answer is:

> \(r^2\delta=o(1)\) does not, by itself, prove the short-chunk TRP
> near-factor. It clears the first-bite collision scale, but a
> self-contained iteration additionally needs an exponentially weighted
> common-core bound, or an equivalent full overlap hierarchy.

This note proves the exact one-bite bound, identifies the false step in the
pair-energy iteration, and states the quantitative link condition which
would give the desired leave. No owner near-factor is claimed from the
pair codegree alone.

## 1. The grouped chunk hypergraph

Let

\[
 T=K N_H,\qquad K=\lfloor M/\ell\rfloor
\]

be the number of labelled carrier copies. For each tag \(a\in[T]\), let
\(\mathcal P_a\) be its repetition-free length-\(\ell\) rotor chunks. Every
chunk has \(\ell\) distinct middle owners. Write

\[
 D_a=|\mathcal P_a|=D_L
\]

and, for an owner \(X\),

\[
 d(X)=|\{(a,P):X\in P,\ P\in\mathcal P_a\}|
 =D_R.
\]

The exact degree ratio is

\[
 \rho_\ell:=\frac{D_R}{D_L}
 =\frac{K\ell N_H}{W}
 =1-O\left(\frac{H+\ell}{m}\right).                  \tag{1.1}
\]

Equivalently,

\[
 \ell T=\rho_\ell W.                                  \tag{1.2}
\]

For a tag \(a\), put

\[
 p_{aX}
 =\Pr_{P\text{ uniform in }\mathcal P_a}(X\in P).
\]

Then

\[
 \sum_a p_{aX}=\rho_\ell                              \tag{1.3}
\]

for every owner \(X\). This identity, not pair codegree, is the input to
the first bite.

The ordinary hypergraph has one vertex for each tag and one for each owner;
an edge is \(\{a\}\cup P\). Its rank is \(r=\ell+1\). Two tags have
codegree zero, a tag-owner codegree is
\(O(\ell/\binom Mm)\) relative to \(D_L\), and the owner-owner codegree is
\(O(m^{-2})\). Therefore (0.1)--(0.2) hold.

## 2. A complete one-bite theorem

### Theorem 2.1 (grouped alteration bite)

For every \(0<\theta\le1\), the chunk hypergraph contains a matching of at
least

\[
 \boxed{
 \left(\theta-\frac{\rho_\ell\theta^2}{2}\right)
 \frac{T}{\ell}}                                      \tag{2.1}
\]

chunks. It covers at least

\[
 \boxed{
 \left(\theta-\frac{\rho_\ell\theta^2}{2}\right)T}     \tag{2.2}
\]

distinct owners.

#### Proof

Activate every tag independently with probability

\[
 q=\frac{\theta}{\ell},
\]

and at each active tag choose one uniform chunk. Let \(A\) be the number
of active tags. Join two active tags in a collision graph when their chosen
chunks share an owner, and let \(C\) be the number of collision-graph edges.

Clearly

\[
 \mathbb EA=qT=\frac{\theta T}{\ell}.                 \tag{2.3}
\]

A union bound over the possible common owners and then (1.3) give

\[
 \begin{aligned}
 \mathbb EC
 &\le q^2\sum_X\sum_{a<b}p_{aX}p_{bX}\\
 &\le\frac{q^2}{2}\sum_X\left(\sum_a p_{aX}\right)^2\\
 &=\frac{q^2W\rho_\ell^2}{2}
 =\frac{\rho_\ell\theta^2}{2}\frac{T}{\ell},
                                                               \tag{2.4}
 \end{aligned}
\]

where (1.2) was used last.

Deleting one endpoint of every collision-graph edge leaves an independent
set of at least \(A-C\) chosen chunks. Its expected lower bound is (2.1),
so some outcome attains it. Multiplying by \(\ell\) gives (2.2).
\(\square\)

At \(\theta=1\), this covers

\[
 \left(\frac12-o(1)\right)T
 =\left(\frac{1}{2\ell}-o(1/\ell)\right)W             \tag{2.5}
\]

owners. Thus a first bite removes only a \(\Theta(1/\ell)\) fraction of
the owner population. Reaching \(o(W)\) leave requires a genuinely
iterated theorem.

## 3. The wasteful-nibble chronology

The cleanest attempted iteration is the following. In a current
\(r\)-uniform residual \(G\) of average degree \(D_t\), mark every edge
independently with probability

\[
 p_t=\frac{h}{rD_t}.                                   \tag{3.1}
\]

Add every isolated marked edge to the matching, but delete every vertex
lying in any marked edge, including vertices in collisions. If \(Z_t\) is
the deleted set, the new residual is

\[
 G_{t+1}=G_t[V(G_t)\setminus Z_t].
\]

The advantage is the exact survival identity

\[
 \Pr(S\cap Z_t=\varnothing)
 =(1-p_t)^{|\Gamma_t(S)|}                              \tag{3.2}
\]

for every vertex set \(S\). A bite removes

\[
 (1+o(1))\frac h r
\]

of the current vertices and wastes only \(O(h^2/r)\) of them at the
one-round level. Therefore

\[
 \Theta\left(\frac r h\log\frac1\eta\right)            \tag{3.3}
\]

bites would be needed to reach owner density \(\eta\).

The one-vertex and one-edge expectations follow from (3.2) and are
controlled by degree variance plus the unweighted pair-codegree sum. The
first failure occurs when one tries to propagate pair-link flatness.

## 4. Exact residual pair-link formula

For owners \(u,v\), let

\[
 \lambda_t(u,v)=d_{G_t}(u,v).
\]

For an edge \(e\), put

\[
 I_e=\mathbf1_{\{e\cap Z_t=\varnothing\}}.
\]

Then

\[
 \lambda_{t+1}(u,v)
 =\sum_{e\supset\{u,v\}}I_e,                           \tag{4.1}
\]

and the exact second moment is

\[
 \boxed{
 \mathbb E\lambda_{t+1}(u,v)^2
 =
 \sum_{\substack{e,f\supset\{u,v\}}}
 (1-p_t)^{|\Gamma_t(e)\cup\Gamma_t(f)|}.}             \tag{4.2}
\]

Writing

\[
 |\Gamma(e)\cup\Gamma(f)|
 =|\Gamma(e)|+|\Gamma(f)|
  -|\Gamma(e)\cap\Gamma(f)|                           \tag{4.3}
\]

exhibits the covariance multiplier

\[
 (1-p_t)^{-|\Gamma(e)\cap\Gamma(f)|}.                 \tag{4.4}
\]

If \(e\) and \(f\) share \(k\) vertices, their \(k\) vertex stars are
contained in both conflict neighborhoods. In a regular diffuse system this
gives

\[
 |\Gamma(e)\cap\Gamma(f)|=\Theta(kD_t)
\]

up to the same multiple-intersection corrections that the nibble is trying
to control. For the initial TRP chunk hypergraph this lower bound is
explicit:

\[
 \begin{aligned}
 |\Gamma(e)\cap\Gamma(f)|
 &\ge
 \left|\bigcup_{x\in e\cap f}\Gamma(x)\right|\\
 &\ge kD_R-\binom{k}{2}\Delta_2
 =\bigl(k-O(k^2/m^2)\bigr)D_L.                        \tag{4.5}
 \end{aligned}
\]

Consequently (4.4) has scale

\[
 \exp\left\{\Theta\left(\frac{hk}{r}\right)\right\}.
                                                               \tag{4.6}
\]

For \(k=O(1)\), this is \(1+O(h/r)\), which is summable over (3.3). For
\(k=\Theta(r)\), it is \(1+\Theta(h)\), which is not.

## 5. What pair codegree actually controls

For two edges write \(j(e,f)=|e\cap f|\). The exact identities are

\[
 \sum_{e,f}j(e,f)
 =\sum_x d(x)^2,                                      \tag{5.1}
\]

\[
 \sum_{e,f}j(e,f)(j(e,f)-1)
 =\sum_{x\ne y}d(x,y)^2.                              \tag{5.2}
\]

If \(G\) is \(D\)-regular and
\(\Delta_2\le\delta D\), then

\[
 \sum_{x\ne y}d(x,y)^2
 \le\Delta_2\sum_{x\ne y}d(x,y)
 \le nD^2r\delta.                                     \tag{5.3}
\]

After normalizing and multiplying by the \(r\) positions tested by one
edge, this gives the familiar parameter

\[
 r^2\delta.                                           \tag{5.4}
\]

But expanding (4.4) to first order also produces

\[
 \frac{h}{r}
 \sum_{e,f}j(e,f)^2(j(e,f)-1),                        \tag{5.5}
\]

up to harmless degree-normalization factors. Pair codegree gives only

\[
 j^2(j-1)\le r\,j(j-1),                               \tag{5.6}
\]

so (5.5) may be \(h\) times the whole pair-link energy rather than
\((h/r)\) times it.

This is the precise error in the tempting recurrence

\[
 B_{t+1}\stackrel{\rm false}{\le}
 (1+O(h/r))B_t+\cdots.                                \tag{5.7}
\]

The bound justified by pair data alone is only

\[
 B_{t+1}\le(1+O(h))B_t+\cdots.                        \tag{5.8}
\]

Over (3.3), the multiplier allowed by (5.8) is

\[
 \exp\{\Theta(r\log(1/\eta))\},                       \tag{5.9}
\]

which destroys every \(o(1)\) initial pair-energy bound of polynomial
size. Therefore the condition \(r^2\delta=o(1)\) does not close this
self-contained nibble.

## 6. Long common cores exist in the TRP family

Take any repetition-free directed rotor walk

\[
 \omega_0,\omega_1,\ldots,\omega_\ell
\]

in one carrier. Its two length-\(\ell\) owner chunks

\[
 P=\{X(\omega_0),\ldots,X(\omega_{\ell-1})\},
\]

\[
 P'=\{X(\omega_1),\ldots,X(\omega_\ell)\}
\]

satisfy

\[
 |P\cap P'|=\ell-1.                                   \tag{6.1}
\]

Assigning them to two labelled copies of the same carrier makes two valid
hyperedges with distinct tag vertices and an owner intersection of size
\(\ell-1=r-2\).

Equation (6.1) does not show that such pairs have large *relative
frequency*. Indeed their frequency may be factorially small. It does show
that no deterministic intersection cap \(j(e,f)=O(1)\) is available, and
that the \(k=\Theta(r)\) term in (4.5) is physically real rather than an
abstract worst case.

Determining their frequency is exactly the next calculation.

## 7. The sufficient weighted-overlap target

For a chunk \(P\) and a different tag \(b\), define the normalized overlap
enumerator

\[
 \Psi_j(P)
 =
 \frac1{D_L}
 \sum_{F\in\mathcal P_b\text{ over all }b\ne\operatorname{tag}(P)}
 \binom{|P\cap F|}{j}.                                \tag{7.1}
\]

The pair-codegree calculation gives only

\[
 \Psi_2(P)=O(r^2/m^2)=o(1).                           \tag{7.2}
\]

The wasteful nibble at residual owner density \(z\) naturally sees the
weighted series

\[
 \boxed{
 \mathcal K_z(P)
 =
 \sum_{j=2}^{r}
 \Psi_j(P)\left(\frac{c}{z}\right)^{j-2}}             \tag{7.3}
\]

for an absolute constant \(c>1\). The powers \(z^{-(j-2)}\) are the
common-core covariance factors from (4.2)--(4.5).

A self-contained iteration to density \(\eta\) would follow from the
uniform gate

\[
 \boxed{
 \log(1/\eta)\,
 \sup_{\eta\le z\le1}\sup_P
 r\,\mathcal K_z(P)=o(1),}                            \tag{7.4}
\]

together with the already verified near-regular degrees and the residual
degree lower bound

\[
 D_L\eta^{O(r)}\longrightarrow\infty.                 \tag{7.5}
\]

Under (7.4), choose \(h=o(1/\log(1/\eta))\). The residual
pair-energy recurrence has a summable multiplier. Summing the one-bite
waste over \(O((r/h)\log(1/\eta))\) rounds gives the quantitative leaves

\[
 L_O
 =O\left(
 \eta+
 h\log(1/\eta)+
 \log(1/\eta)
   \sup_{\eta\le z\le1}\sup_P r\mathcal K_z(P)
 \right)W,                                             \tag{7.6}
\]

\[
 L_C\le L_O/\ell,                                     \tag{7.7}
\]

where \(L_O\) and \(L_C\) are the owner and carrier-copy leaves.

Equations (7.6)--(7.7) are the correct quantitative target. They are
conditional because (7.4) has not been proved for rotor chunks.

For example, taking \(\eta=1/\log m\) would give the desired

\[
 L_O=o(W),\qquad L_C=o(W/\ell),                        \tag{7.8}
\]

if

\[
 \sup_P r\mathcal K_{1/\log m}(P)
 =o(1/\log\log m).                                     \tag{7.9}
\]

The scalar degree condition (7.5) is automatic: since

\[
 \log D_L=(3/2+o(1))\ell\log m,
\]

one has

\[
 \log\bigl(D_L(\log m)^{-C\ell}\bigr)
 =\ell\bigl((3/2+o(1))\log m-C\log\log m\bigr)
 \longrightarrow+\infty                              \tag{7.10}
\]

for every fixed \(C\). The only missing input is therefore the weighted
overlap hierarchy, not degree exhaustion.

## 8. Coefficient-one ledger if the hierarchy is proved

The reset and remainder calculations remain favorable independently of
the matching issue:

\[
 O(QKN_H)=O(QW/\ell)=o(W),                            \tag{8.1}
\]

\[
 O(\ell N_H)=O(\ell W/m)=o(W).                        \tag{8.2}
\]

If (7.9) gives (7.8), then concatenating the selected literal rotor chunks
and appending owner holes has total owner-level length

\[
 W+o(W).                                               \tag{8.3}
\]

Thus short chunks solve the reset and scalar-degree barriers. They do not
yet solve the common-core propagation barrier.

## 9. Audit ledger

### Proved

1. Exact two-type near-regularity and rank \(r=\ell+1\).
2. Maximum relative pair codegree \(O(m^{-2})\), hence
   \(r^2\delta=o(1)\).
3. The grouped one-bite matching bound (2.1).
4. The exact residual pair-link formula (4.2).
5. The third-overlap counterterm (5.5), which invalidates a
   pair-energy-only \(1+O(h/r)\) recurrence.
6. Physical length-\(\Theta(r)\) common cores via shifted chunks.
7. Residual scalar degree remains enormous down to density \(1/\log m\).
8. Conditional leave bounds (7.6)--(7.7) under the weighted hierarchy
   (7.4).

### Open

1. A direct count of every \(\Psi_j(P)\) for stationary rotor chunks.
2. The weighted bound (7.9).
3. Therefore the owner near-factor itself.
4. Simultaneous flag-compatible chunk selection.

The correct next step is not another appeal to a fixed-rank nibble. It is
an exact factorial count of long common rotor subchunks strong enough to
sum (7.3).
