# Short-chunk TRP nibble: the exact one-bite theorem and the higher-link obstruction

Date: 2026-07-25

Method: pure mathematics only. No solver, computation, web search, or
fixed-uniformity matching theorem is used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad N=N_H=\binom{2m}{m-H},\qquad
 M=m+H,
\]

and use the calibrated \(H\) and truncated radius \(Q\). Split every
carrier into labelled, independently initialized chunks of length
\(\ell\), where

\[
 Q\ll\ell\ll m.
\tag{0.1}
\]

After deleting the exponentially rare chunks with repeated owners, the
tagged owner hypergraph has rank

\[
 r=\ell+1,
\]

is \(1-o(1)\) regular, and has

\[
 {\Delta_2\over D}=O(m^{-2}),\qquad
 r^2{\Delta_2\over D}=O(\ell^2/m^2)=o(1).
\tag{0.2}
\]

This note obtains two rigorous new facts.

1. A complete direct one-bite nibble calculation works. Marking each
   chunk edge with probability \(\theta/(rD)\) and retaining isolated
   marked edges produces

   \[
   \left(\theta e^{-\theta}+o(1)\right){n\over r^2}
   \tag{0.3}
   \]

   disjoint chunks, where \(n=(1+o(1))W\) is the total tagged-owner
   vertex count. Conditional on an owner surviving this bite, its new
   degree has relative variance

   \[
   O\left(D^{-1}+\theta r\,{\Delta_2\over D}
           +{H+\ell\over m}\right)
   =O\left(D^{-1}+\theta\ell/m^2+{H+\ell\over m}\right).
   \tag{0.4}
   \]

   Thus vertex degrees are stable for one bite by an elementary
   second-moment proof.

2. The pair estimate does not propagate itself. For a Johnson-distance-two
   pair prescribed two rotor times apart, any prescribed geodesic midpoint
   has exact conditional codegree \(1/4\) before repetition pruning and
   \(1/4+o(1)\) afterwards. Consequently the second moment
   of the *residual pair degree* contains an uncontrolled triple-link term.
   Over the required \(\Theta(\ell\log\log m)\) owner bites this term is not
   forced to vanish by (0.2).

Therefore no near-perfect owner theorem is proved from the pair codegree
alone. The precise additional input is a weighted hierarchy of conditional
TRP links which distinguishes the dominant distance-one pairs from the
much smaller distance-two and higher pairs. Replacing this hierarchy by the
sentence “apply a growing-rank nibble” would be a black-box handwave.

The flag audit is sharper. Nested priorities put

\[
 k_\ell
 =(\sqrt\pi+o(1))\ell\sqrt m
\tag{0.5}
\]

protected targets in a mean decorated chunk, and the exact vertical
owner--facet relative codegree is

\[
 {1+o(1)\over m}.
\tag{0.6}
\]

Hence the augmented pair parameter is at least

\[
 k_\ell^2{\Delta_2^{\rm aug}\over D}
 \ge (1-o(1))\ell^2\longrightarrow\infty.
\tag{0.7}
\]

Even an owner-scale bite has mean flag-conflict load
\(\Theta(\sqrt m)\) per marked chunk. Thus the short-chunk reduction
improves the owner geometry but does not make the flag rows a conventional
growing-rank matching instance. Coefficient one remains open.

## 1. The short-chunk owner hypergraph

Let

\[
 K=\lfloor M/\ell\rfloor.
\]

For every carrier \(U\in\binom{[2m]}M\), introduce \(K\) labelled copies.
Above a copy put every repetition-free stationary rotor chunk

\[
 P=(\omega_0,\ldots,\omega_{\ell-1}).
\]

The associated edge consists of the copy tag and the \(\ell\) distinct
middle owners of the chunk.

Let \(D_L\) be the tag degree after repetition-free pruning. The calculation
in TRP_OWNER_PATH_CODEGREE_AUDIT_20260725.md gives

\[
 d(\tau)=D_L
\tag{1.1}
\]

for every copy tag and

\[
 d(X)=\rho_\ell D_L,\qquad
 \rho_\ell={K\ell N\over W}
 =1-O((H+\ell)/m)
\tag{1.2}
\]

for every owner \(X\). Put

\[
 D:=D_L,\qquad
 a:=1-\rho_\ell=o(1).
\]

There are

\[
 n_L=KN=(1+o(1)){W\over\ell}
\tag{1.3}
\]

left vertices and \(W\) owner vertices, so

\[
 n:=n_L+W=(1+o(1))W.
\tag{1.4}
\]

Every edge has rank \(r=\ell+1\). Two left vertices have codegree zero,
a left--owner codegree is negligible, and two distinct owners have

\[
 d(X,Y)\le \delta D,\qquad
 \delta=O(m^{-2}).
\tag{1.5}
\]

The reset and omitted-remainder tolls are

\[
 O((Q/\ell)W)+O((\ell/m)W)=o(W).
\tag{1.6}
\]

Thus an owner matching leaving \(o(W)\) owners and \(o(W/\ell)\) copy tags
would preserve the coefficient-one ledger.

## 2. Conflict-neighbourhood size

For an edge \(e\), let

\[
 \Gamma[e]=\{f:f\cap e\ne\varnothing\}.
\]

### Lemma 2.1

Uniformly over all chunk edges,

\[
 \boxed{|\Gamma[e]|=(1+o(1))rD.}
\tag{2.1}
\]

#### Proof

The union bound gives

\[
 |\Gamma[e]|
 \le\sum_{v\in e}d(v)
 \le rD.
\tag{2.2}
\]

Bonferroni gives

\[
 |\Gamma[e]|
 \ge\sum_{v\in e}d(v)
   -\sum_{\{u,v\}\subset e}d(u,v).
\tag{2.3}
\]

The first sum is at least \(r(1-a)D\). The second is at most
\(\binom r2\delta D\). Therefore

\[
 |\Gamma[e]|
 \ge rD\left(1-a-O(r\delta)\right).
\tag{2.4}
\]

Here \(a=o(1)\) and

\[
 r\delta=O(\ell/m^2)=o(1).
\]

Equations (2.2)--(2.4) prove (2.1). \(\square\)

Notice that the conflict-neighbourhood calculation needs only
\(r\Delta_2/D=o(1)\), which is much weaker than the parameter in (0.2).

## 3. A complete one-bite theorem

Fix \(0<\theta\le1\). Mark every edge independently with probability

\[
 p={\theta\over rD}.
\tag{3.1}
\]

Retain a marked edge precisely when no other marked edge meets it.
The retained edges form a matching.

### Theorem 3.1

The expected number of retained chunks is

\[
 \boxed{
 \mathbb E|\mathcal M_1|
 =\left(\theta e^{-\theta}+o(1)\right){n\over r^2}.}
\tag{3.2}
\]

Consequently some bite covers

\[
 \left(\theta e^{-\theta}+o(1)\right){n\over r}
\tag{3.3}
\]

vertices.

#### Proof

The degree sum gives

\[
 |E(\mathcal H)|
 ={(1+o(1))nD\over r}.
\tag{3.4}
\]

For a fixed edge \(e\),

\[
 \Pr(e\hbox{ is retained})
 =p(1-p)^{|\Gamma[e]|-1}.
\tag{3.5}
\]

By Lemma 2.1,

\[
 p|\Gamma[e]|=\theta+o(1),
\qquad p^2|\Gamma[e]|=o(1),
\]

and hence

\[
 (1-p)^{|\Gamma[e]|-1}=e^{-\theta}+o(1)
\tag{3.6}
\]

uniformly in \(e\). Sum (3.5) over the edges and use (3.1), (3.4), and
(3.6). This proves (3.2). Multiplication by \(r\) proves (3.3).
\(\square\)

For the carrier-path parameters, one bite therefore selects

\[
 \left(\theta e^{-\theta}+o(1)\right){W\over\ell^2}
\tag{3.7}
\]

chunks and covers

\[
 \left(\theta e^{-\theta}+o(1)\right){W\over\ell}
\tag{3.8}
\]

owners. A constant fraction of owners requires \(\Theta(\ell)\) stable
bites; an owner residual \(1/\log m\) requires
\(\Theta(\ell\log\log m)\) stable bites.

## 4. Exact one-bite degree stability

The next calculation explains why the first iteration looks promising.
Delete every vertex which lies in a marked edge, whether or not that marked
edge is retained. This “wasteful” deletion only makes the residual smaller,
and it makes survival an exact product event.

Fix a vertex \(v\), and condition on \(v\) being untouched, i.e. on no edge
through \(v\) being marked. Let \(Z_v\) be its degree in the induced
untouched hypergraph.

For \(e\ni v\), put

\[
 I_e=\mathbf 1\{\hbox{no marked edge in }
                 \Gamma[e]\setminus E(v)\},
\qquad
 Z_v=\sum_{e\ni v}I_e,
\tag{4.1}
\]

where \(E(v)\) is the family of edges through \(v\).

### Lemma 4.1

Uniformly in \(v\),

\[
 \mathbb E(Z_v\mid v\hbox{ untouched})
 =(1+o(1))d(v)e^{-\theta(1-1/r)}
\tag{4.2}
\]

and

\[
 \boxed{
 {\operatorname {Var}(Z_v\mid v\hbox{ untouched})\over D^2}
 =O\left({1\over D}+\theta r\delta+a\right).}
\tag{4.3}
\]

For short TRP chunks the right side is

\[
 O\left(D^{-1}+\theta\ell/m^2+(H+\ell)/m\right)=o(1).
\tag{4.4}
\]

#### Proof

For \(e\ni v\), Bonferroni as in Lemma 2.1 gives

\[
 |\Gamma[e]\setminus E(v)|
 =(r-1)D\bigl(1+O(a+r\delta)\bigr).
\tag{4.5}
\]

The marks outside \(E(v)\) remain independent after conditioning that
\(v\) is untouched. Thus

\[
 \mathbb EI_e
 =(1-p)^{|\Gamma[e]\setminus E(v)|}
 =e^{-\theta(1-1/r)}(1+o(1)),
\tag{4.6}
\]

which proves (4.2).

It remains to sum the covariances. For \(e,f\ni v\), define

\[
 J_{e,f}
 =(\Gamma[e]\cap\Gamma[f])\setminus E(v).
\]

Since \(p|\Gamma[e]|=O(1)\), the exact product formulas imply

\[
 0\le\operatorname {Cov}(I_e,I_f)
 \le C p|J_{e,f}|
\tag{4.7}
\]

for an absolute \(C\). For an edge \(g\not\ni v\), put

\[
 A_g=\#\{e\ni v:e\cap g\ne\varnothing\}.
\]

Then

\[
 \sum_{e,f\ni v}|J_{e,f}|
 =\sum_{g\not\ni v}A_g^2.
\tag{4.8}
\]

The pair-codegree bound gives

\[
 A_g\le\sum_{u\in g}d(u,v)\le r\Delta_2\le r\delta D.
\tag{4.9}
\]

On the other hand,

\[
 \sum_{g\not\ni v}A_g
 \le \sum_{e\ni v}\sum_{u\in e-\{v\}}d(u)
 \le rD^2.
\tag{4.10}
\]

Therefore

\[
 \sum_{g\not\ni v}A_g^2
 \le(\max_gA_g)\sum_gA_g
 \le r^2\delta D^3.
\tag{4.11}
\]

Multiply (4.11) by \(p=\theta/(rD)\) in (4.7). The off-diagonal covariance
sum is \(O(\theta r\delta D^2)\). The diagonal variance contributes at most
\(d(v)\le D\). The \(aD^2\) term records the harmless degree imbalance in
(4.5). This proves (4.3). \(\square\)

Lemma 4.1 is a genuine growing-rank stability estimate proved directly from
the exact owner codegree. It says that one bite preserves almost all vertex
degrees in mean square. It does **not** say that the pair-codegree hypothesis
needed for the next bite has been preserved.

## 5. Why the pair bound does not iterate itself

Fix two vertices \(u,v\), let

\[
 \mathcal C(u,v)=\{e:u,v\in e\},
\qquad c(u,v)=|\mathcal C(u,v)|,
\]

and condition on both \(u\) and \(v\) being untouched. The residual
codegree is

\[
 Z_{u,v}=\sum_{e\in\mathcal C(u,v)}
 \mathbf 1\{\Gamma[e]\setminus(E(u)\cup E(v))
             \hbox{ contains no mark}\}.
\tag{5.1}
\]

Repeating the proof of Lemma 4.1 now introduces, for \(g\) avoiding
\(u,v\),

\[
 A_g(u,v)
 =\#\{e\in\mathcal C(u,v):e\cap g\ne\varnothing\}.
\tag{5.2}
\]

The covariance term is

\[
 p\sum_g A_g(u,v)^2.
\tag{5.3}
\]

Pair codegrees give only the useless bound

\[
 A_g(u,v)
 \le\sum_{w\in g}d(u,v,w)
 \le r\,c(u,v).
\tag{5.4}
\]

Thus (5.3) depends on triple codegrees \(d(u,v,w)\), which are invisible in
\(\Delta_2/D\). This is not merely a weakness of the inequality.

### Proposition 5.1 (exact geodesic triple concentration)

Let \(t+2<\ell\). Choose owners

\[
 X_2=X_0-\{a_1,a_2\}+\{b_1,b_2\}
\]

at Johnson distance two, and let

\[
 X_1=X_0-a_i+b_j
\]

be any one of the four geodesic midpoints. In the unpruned time-labelled
stationary chunk catalogue,

\[
 \boxed{
 {\deg((t,X_0),(t+1,X_1),(t+2,X_2))
  \over
  \deg((t,X_0),(t+2,X_2))}
 ={1\over4}.}
\tag{5.5}
\]

#### Proof

The first \(Q\) rotor steps are geodesic. Conditional on the two-step
endpoint \(X_2\), the two departing elements \(a_1,a_2\) may leave in
either order and the two arriving elements \(b_1,b_2\) may enter in either
order. The uniform state fibre and uniform rotor choices give the four
ordered possibilities equal weight. Each pair of first choices produces
one of the four sets \(X_0-a_i+b_j\), and no two choices produce the same
midpoint. Hence each midpoint has conditional probability \(1/4\).
\(\square\)

Equivalently, a quarter of the chunks counted by the endpoint pair contain
one fixed third owner. If that midpoint is removed in a bite, a quarter of
the endpoint codegree disappears simultaneously. The pair bound

\[
 {\deg((t,X_0),(t+2,X_2))\over\deg(t,X_0)}
 ={1\over\binom m2^2}=O(m^{-4})
\tag{5.6}
\]

does not record this conditional concentration.

Conditioning the catalogue on owner-repetition-free chunks changes (5.5)
by only \(e^{-\Omega(Q)}\). Indeed the discarded probability is
\(e^{-\Omega(Q)}\), whereas either fixed endpoint event in (5.5) has only
polynomially small probability \(\binom m2^{-2}\); division still leaves
\(e^{-\Omega(Q)}\). Thus the conditional ratio in the simple support
hypergraph is \(1/4+o(1)\), still bounded away from zero.

This example does not prove that an owner near-factor is false. The
distance-two pair in (5.6) is much smaller than the dominant distance-one
pair. It proves the narrower and exact point needed here:

> a multi-round proof must track the distance-sensitive triple and higher
> owner links; the scalar estimate \(\Delta_2/D=O(m^{-2})\) cannot propagate
> its own hypotheses.

A plausible sufficient hierarchy would separate:

* distance-one pairs, for which one needs a small conditional extension
  sum over third owners;
* distance-\(d\) geodesic pairs, whose absolute degree already carries the
  factor \(\binom md^{-2}\); and
* late-lag pairs, controlled by the \(e^{-\Omega(Q)}\) return estimates.

No such full adaptive hierarchy is proved in the available TRP notes.
Consequently Theorem 3.1 and Lemma 4.1 cannot rigorously be iterated
\(\Theta(\ell\log\log m)\) times.

## 6. Nested-priority claims on a short chunk

Now decorate the state times by the calibrated common priority system. Put

\[
 p_q={1\over M}\min\left(M,{\lambda_H\over\lambda_q}\right),
\qquad 1\le q\le Q.
\tag{6.1}
\]

A time claims its lower and upper depth-\(q\) flags with probability
\(p_q\), coupled monotonically in \(q\). The exact mean number of protected
targets in an \(\ell\)-chunk is

\[
 k_\ell
 =\ell\left(1+2\sum_{q=1}^{Q}p_q\right).
\tag{6.2}
\]

The Gaussian calculation gives

\[
 \sum_{q=1}^{Q}p_q
 =\left({\sqrt\pi\over2}+o(1)\right)\sqrt m,
\]

and therefore

\[
 \boxed{k_\ell=(\sqrt\pi+o(1))\ell\sqrt m.}
\tag{6.3}
\]

Truncation at \(Q\) again saves only \(o(\ell\sqrt m)\) claims because
\(Q/\sqrt m\to\infty\).

The total number of protected mask targets is

\[
 V_Q=W+2\sum_{q=1}^{Q}N_q
 =(\sqrt\pi+o(1))W\sqrt m.
\tag{6.4}
\]

Thus coefficient one requires an augmented unmatched fraction

\[
 \varepsilon_{\rm aug}=o(m^{-1/2}),
\tag{6.5}
\]

not merely an unspecified \(o(1)\).

## 7. Exact flag-row obstruction to the pair nibble

Condition on a uniform state column with middle owner \(X\). For a
prescribed facet \(S\subset X\) and cofacet \(T\supset X\),

\[
 \Pr(L_1=S\mid X)={1\over m},\qquad
 \Pr(U_1=T\mid X)={1\over m}.
\tag{7.1}
\]

Since \(p_1=1-o(1)\), the decorated hypergraph has vertical pair
codegrees

\[
 {\deg(X,S)\over\deg(X)}
 ={1+o(1)\over m},
\qquad
 {\deg(X,T)\over\deg(X)}
 ={1+o(1)\over m},
\tag{7.2}
\]

at the same-column occurrence level. Hence

\[
 {\Delta_2^{\rm aug}\over D}\ge {1-o(1)\over m}.
\tag{7.3}
\]

If the protected targets and the copy tag are encoded as ordinary vertices,
the decorated edge has mean rank \(k_\ell+1\), and

\[
 (k_\ell+1)^2{\Delta_2^{\rm aug}\over D}
 \ge(1-o(1)){k_\ell^2\over m}
 =(\pi+o(1))\ell^2.
\tag{7.4}
\]

This diverges for every admissible \(\ell\), rather than tending to zero.
Thus even the favorable owner parameter (0.2) is destroyed by the first
flag row.

There is a corresponding independent-neighbourhood benchmark. Suppose for
the moment that
all claimed target degrees have been normalized to \(D\) and that
Bonferroni overlaps are negligible. A decorated chunk has approximately
\(k_\ell D\) conflicting candidate edges. The owner bite (3.1) uses

\[
 p_{\rm own}\asymp {1\over\ell D}.
\]

Its mean number of marked flag-conflicting neighbours is therefore

\[
 p_{\rm own}k_\ell D
 ={k_\ell\over\ell}
 =(\sqrt\pi+o(1))\sqrt m.
\tag{7.5}
\]

Under this noncollapsed-neighbourhood hypothesis the isolation probability
is on the scale

\[
 \exp(-\Theta(\sqrt m)),
\tag{7.6}
\]

not a positive constant. The nondegenerate benchmark scale is instead

\[
 p_{\rm aug}\asymp {1\over k_\ell D}.
\tag{7.7}
\]

At this scale one requires \(\Theta(k_\ell\log m)\) stable rounds to reach
(6.5). A
larger safe marking probability could only come from a new theorem proving
that the \(k_\ell\) conflict neighbourhoods collapse coherently; the
available owner codegrees do not prove such a collapse. In the ordinary
augmented encoding,
the vertical codegree (7.3) lies far outside the pair-stability range
throughout.

Nested priorities do not remove this calculation. They are precisely what
produces the value \(k_\ell\) in (6.3), and \(p_1=1-o(1)\) leaves the
depth-one vertical pair untouched.

## 8. The local upper-star obstruction also survives chunking

The difficulty is not only the large numerical value in (7.4). At a rotor
transition, the arrival \(y\) determines the next owner and every upper
flag:

\[
 X'=A_0+y,\qquad U_q'=A_q^++y.
\tag{8.1}
\]

The delayed choice \(x\) is invisible to these targets. The common-upper-
star construction in DYNAMIC_TRP_ROUND_HALL_AND_FLAG_OBSTRUCTION_20260725.md
produces legitimate collections of states for which owner candidate sets
are pairwise disjoint while all depth-\(Q\) upper candidates occupy one
common \(H-Q\) target family.

Chunking changes neither (8.1) nor that one-step obstruction. It only
reinitializes the rotor after \(\ell\) states. Therefore any adaptive
flag nibble needs a maintained upper-star congestion invariant; owner
near-regularity and owner codegrees do not imply it.

This is not a counterexample to a globally selected chunk family. A global
selection may avoid the bad state fibres. It is an exact obstruction to
proving flag stability by conditioning only on the owner residual.

## 9. Exact frontier

The short-chunk machinery now has the following audited status.

1. The literal ledger is valid for every \(Q\ll\ell\ll m\).
2. The tagged owner hypergraph is nearly regular and has exact relative
   pair codegree \(O(m^{-2})\).
3. The direct isolated-edge bite, including its constant and its
   one-step conditional degree variance, is proved in Sections 3--4.
4. Iterating the owner bite requires a distance-sensitive triple/higher-link
   theorem. Proposition 5.1 proves that this requirement cannot be deleted
   from the proof.
5. Adding calibrated flag claims raises the mean edge size to
   \((\sqrt\pi+o(1))\ell\sqrt m\) and introduces relative vertical
   codegree \(1/m\).
6. An owner-scale bite then has \(\Theta(\sqrt m)\) flag-conflict load,
   while an augmented-scale bite lies outside the pair-stability regime and
   must also control the upper-star fibres.

The next coefficient-one lemma would therefore have to be genuinely
column-correlated:

> **Short-chunk column nibble gate.** Prove a multi-round nibble for
> repetition-free rotor chunks which tracks the complete distance-sensitive
> owner link hierarchy and treats every nested flag column as one correlated
> object, while leaving \(o(W)\) total flag holes and \(o(W/\ell)\) unused
> chunk tags.

Neither the exact \(O(m^{-2})\) owner codegree nor a conventional augmented
hypergraph encoding proves this gate.
