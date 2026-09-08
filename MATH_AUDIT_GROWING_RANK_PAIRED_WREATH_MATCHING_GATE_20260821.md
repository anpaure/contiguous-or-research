# Growing-rank matching audit for the paired-wreath auxiliary hypergraph

## 1. Exact scale and the endpoint-capacity obstruction

Put
\[
 b=2r+1,\qquad n_0=\binom{2r+1}{r},
\]
and let \(G=KG(2r+1,r)\).  Let \({\cal J}_r\) be the paired-wreath
auxiliary hypergraph whose vertices are the edges of \(G\) and whose
hyperedges are the \(r\) Kneser pairs in a punctured wreath.  The exact
profile proved separately is
\[
 \begin{split}
 N_r:=|V({\cal J}_r)|&=|E(G)|=\frac{r+1}{2}n_0,\\
 D_r:=\Delta({\cal J}_r)&=r(r!)^2,\\
 C_r:=\Delta_2({\cal J}_r)&=(r-1)((r-1)!)^2,\\
 \frac{C_r}{D_r}&=\frac{r-1}{r^3},\\
 \Delta_t({\cal J}_r)&=(r-t+1)((r-t+1)!)^2\quad(2\le t\le r).
 \end{split}                                                   \tag{1.1}
\]

Calling two \({\cal J}_r\)-edges endpoint-conflicting when their
underlying Kneser pairs use a common target does **not** turn an
almost-perfect matching theorem for \({\cal J}_r\) into the desired
physical result.  Indeed, an endpoint-conflict-free matching \({\cal M}\)
uses \(2r\) distinct targets per selected hyperedge.  Consequently
\[
       |{\cal M}|\le \frac{n_0}{2r},\qquad
       |V({\cal M})|=r|{\cal M}|\le \frac{n_0}{2}
       =\frac{N_r}{r+1}.                                     \tag{1.2}
\]
Thus such a matching necessarily leaves at least
\(rN_r/(r+1)\) vertices of the full auxiliary hypergraph.  No
conflict-free theorem whose conclusion is an almost-perfect matching in
\({\cal J}_r\) can apply.  This is a scale obstruction, not merely a
failure to verify a technical conflict-degree estimate.

The correct order of operations is therefore:

1. choose a Kneser matching \(P\subseteq E(G)\) with
   \(|P|=(1-o(1))n_0/2\);
2. form the induced \(r\)-graph
   \[
             {\cal H}_P={\cal J}_r[P];                       \tag{1.3}
   \]
3. find a matching of \({\cal H}_P\) covering all but \(o(|P|)\)
   vertices.

At the first step, existence of a sufficiently large \(P\) is elementary:
\(G\) is \((r+1)\)-regular, so Vizing's theorem gives an edge-colouring
with at most \(r+2\) colours.  Its largest colour class has size at least
\[
 \frac{|E(G)|}{r+2}
   =\frac{r+1}{r+2}\frac{n_0}{2},                            \tag{1.4}
\]
and hence misses only an \(O(1/r)\) fraction of the target vertices.
This argument does not, however, control the profile of \({\cal H}_P\).

## 2. What symmetry gives after restricting to \(P\)

Let \(P\) be a random maximum Kneser matching with an
\(S_{2r+1}\)-invariant law.  Write
\[
 Q=|E(G)|,\qquad m=|P|=\left\lfloor n_0/2\right\rfloor,
 \qquad q_1=\Pr(e\in P)=m/Q,                                 \tag{2.1}
\]
and let \(q_r=\Pr(F\subseteq P)\) for a fixed
\(F\in E({\cal J}_r)\).  For a compatible pair of type \(d\), write
\(q_{2,d}=\Pr(e,f\in P)\).  Orbit counting gives exactly
\[
 \begin{split}
 \mathbb E|E({\cal H}_P)|&=\frac{(2r+1)!}{2}q_r,\\
 \mathbb E[d_{{\cal H}_P}(e)\mid e\in P]
   &=D_r\frac{q_r}{q_1},\\
 \mathbb E[d_{{\cal H}_P}(e,f)\mid e,f\in P]
   &=\lambda_{r,d}\frac{q_r}{q_{2,d}}.
 \end{split}                                                  \tag{2.2}
\]
In particular, the conditional expected codegree-to-degree ratio is
\[
 \frac{\lambda_{r,d}}{D_r}\frac{q_1}{q_{2,d}}.              \tag{2.3}
\]
Neither \(q_r\), nor \(q_{2,d}\), nor uniform concentration of the
degrees in (2.2) follows from invariance.  A random conjugate of any
fixed maximum matching is invariant, and different matching orbits can
have different values of all these quantities.

The independence heuristic \(q_r\approx q_1^r\) and
\(q_{2,d}\approx q_1^2\), with \(q_1\sim1/(r+1)\), predicts
\[
 D_P\approx \frac{D_r}{(r+1)^{r-1}},\qquad
 \frac{C_P}{D_P}\asymp\frac1r.                              \tag{2.4}
\]
This heuristic is not used as a theorem.  It only warns that restriction
to a generic Kneser matching may spend the extra factor of \(r\) in
\(C_r/D_r\): one must prove the restricted profile rather than inherit
the full-\({\cal J}_r\) profile formally.

## 3. Published matching and edge-colouring black boxes

### 3.1 Fixed-uniformity theorems do not give a diagonal statement

The Pippenger--Spencer chromatic-index theorem explicitly assumes a
fixed uniformity \(k\).  Modern Pippenger-type and conflict-free
statements have the same quantifier order.  For example:

- Delcourt--Postle, Theorem 1.16, first fixes the rank and a positive
  power \(\beta\), then chooses the degree threshold; its base
  codegree hypothesis is \(\Delta_2\le D^{1-\beta}\).
- Glock--Joos--Kim--Kuehn--Lichev, Theorem 1.3, first fixes
  \(k,\ell\), then chooses \(\varepsilon_0,d_0\); its base hypothesis
  is \(\Delta_2\le d^{1-\varepsilon}\), and its leave is
  \(d^{-\varepsilon^3}|V|\).

For the full \({\cal J}_r\), a power-codegree exponent must satisfy
\[
 \varepsilon\le
 \frac{\log(D_r/C_r)}{\log D_r}
   =(1+o(1))\frac1r.                                         \tag{3.1}
\]
Even if one ignored the fixed-rank quantifier and inserted this largest
possible exponent into the Glock et al. conclusion,
\[
 \varepsilon^3\log D_r=O(\log r/r^2)=o(1),                  \tag{3.2}
\]
so the advertised leave factor tends to one, not zero.  Moreover their
order condition \(|V|\le\exp(d^{\varepsilon^3})\) also fails: its
right-hand side is \(O(1)\) on the logarithmic scale while
\(\log N_r=\Theta(r)\).  Thus this is not merely an untracked-threshold
issue.

### 3.2 The older explicit logarithmic-codegree threshold

The Grable bound quoted and sharpened by Kostochka--Rodl requires, in
its notation,
\[
             \frac{kC\log |V|}{D}=o(1).                     \tag{3.3}
\]
The full paired-wreath profile lands exactly at, rather than below, this
threshold:
\[
 \frac{rC_r\log N_r}{D_r}
   =\frac{r-1}{r^2}\log N_r
   \longrightarrow \log 4.                                  \tag{3.4}
\]
Thus this result does not apply even before considering whether its
constants are uniform in growing \(k\).  The earlier Frankl--Rodl
hypothesis \(C\le D/(\log |V|)^a\), \(a>3\), also fails, since here
\(C_r/D_r=\Theta(r^{-2})\) while
\((\log N_r)^{-a}=\Theta(r^{-a})\).

### 3.3 The quantitative growing-uniformity theorem

Alon--Bollobas--Kim--Vu, Corollary 1.5, is an explicit theorem in which
the uniformity may grow.  For a regular \(k\)-graph of degree \(D\) and
maximum codegree \(C\), it requires
\[
        e^{2k}C=o(D/\log D)                                  \tag{3.5}
\]
and gives a matching leaving
\[
 O\!\left(k\left(\frac{C\log(1+C)}D\right)^{1/(k-1)}|V|\right)
                                                                  \tag{3.6}
\]
vertices.

For the full \({\cal J}_r\), (3.5) fails because
\[
 e^{2r}\frac{C_r\log D_r}{D_r}
   =(2+o(1))\frac{e^{2r}\log r}{r}\longrightarrow\infty.    \tag{3.7}
\]
Even disregarding (3.5), the coefficient in (3.6) is
\[
 r\left(\frac{C_r\log(1+C_r)}{D_r}\right)^{1/(r-1)}
   =r\exp\!\left(-(1+o(1))\frac{\log r}{r}\right)
   \sim r,                                                    \tag{3.8}
\]
so the leave bound is vacuous.

For a restricted hypergraph \({\cal H}_P\) that is regular of degree
\(D_P\) and has maximum codegree \(C_P\), the same published theorem
would apply if
\[
 e^{2r}C_P=o(D_P/\log D_P),                                  \tag{3.9}
\]
and its displayed leave bound would be \(o(|P|)\) provided its explicit
coefficient obeys
\[
 r\left(\frac{C_P\log(1+C_P)}{D_P}\right)^{1/(r-1)}=o(1).   \tag{3.10}
\]
Equations (3.9)--(3.10), together with uniform near-regularity, are the
cleanest currently published sufficient gate.  Condition (3.10) asks for
roughly an \(r^{\,r}\)-scale degree/codegree separation, far stronger
than any polynomial separation suggested by (1.1) or (2.4).

### 3.4 Higher-codegree theorems still give no nontrivial bound here

Gould--Kelly, Theorems 1.4 and 1.7, use the full codegree sequence.  In
the notation of an \(r\)-uniform input, their parameter satisfies
\[
 B\le \min\left\{
   \sqrt{D/D_2},
   \min_{4\le t\le r}(D/D_t)^{1/(t-1)},
   1/\eta
 \right\},                                                   \tag{3.11}
\]
where \(\eta\) is the degree error.  Their matching leave and relative
edge-colouring error have the form
\[
              B^{-1+\gamma}\log^A D,                        \tag{3.12}
\]
under a hierarchy which fixes \(k\) before \(D\).  In the proof they
take \(A=10/\gamma^4\), and explicitly declare the theorem trivial when
\(B\le\log^{10/\gamma^4}D\).

Already the pair term in (1.1) forces, for the full auxiliary graph,
\[
       B\le\sqrt{D_r/C_r}sim r,qquad
       \log D_r\sim2r\log r.                                \tag{3.13}
\]
Hence it lies in that trivial range.  For \({\cal H}_P\), (3.9) is a
useful checklist only after its restricted degree and every restricted
higher codegree have been controlled; it is not presently an applicable
theorem.  Under the independence heuristic (2.4), its pair term is only
\(B=O(\sqrt r)\), again much smaller than \(\log D_P\).

## 4. Exact remaining gates

There are two logically separate missing results.

**Selection/concentration gate.**  Construct a Kneser matching
\(P_r\) of size \((1-o(1))n_0/2\) for which \({\cal H}_{P_r}\) has a
uniformly controlled degree and overlap profile.  At minimum this must
include
\[
 \begin{split}
 d_{{\cal H}_{P_r}}(e)&=(1\pm\eta_r)D'_r
     &&\text{for every }e\in P_r,\\
 \Delta_2({\cal H}_{P_r})&\le C'_r,\\
 \max_{F\in E({\cal H}_{P_r})}
   \sum_{\{e,f\}\in\binom F2}d_{{\cal H}_{P_r}}(e,f)&\le L'_rD'_r.
                                                               \tag{4.1}
 \end{split}
\]
The exact identities (2.2) are only first-moment identities and do not
prove (4.1).

**Growing-rank paired-profile nibble gate.**  Prove a specialized
matching lemma which turns a profile of the natural strength
\[
       r\eta_r=o(1),\qquad
       rC'_r/D'_r=o(1),\qquad
       L'_r=o(1)                                              \tag{4.2}
\]
(with whatever explicit degree-versus-order lower bound its
concentration argument needs) into a matching covering
\((1-o(1))|P_r|\) vertices.  This is deliberately recorded as an open
lemma, not as a consequence of Pippenger--Spencer.  The internal-overlap
condition in (4.2) is needed because a maximum pair codegree alone loses
the highly nonuniform distance profile in (1.4).

Alternatively, proving the much stronger published gate
(3.9)--(3.10) for some \(P_r\) would close the matching step without a
new nibble theorem.  No currently verified profile of \({\cal H}_{P_r}\)
comes close to that gate.

## 5. Scope verdict

The exact full-\({\cal J}_r\) profile is promising but does not itself
cross a published growing-rank theorem.  The full endpoint-conflict
formulation is impossible at the almost-perfect-\({\cal J}_r\) scale by
(1.2).  Restricting first to a near-perfect Kneser matching \(P\) fixes
the physical scale, but creates a new and currently unproved
selection/concentration problem, followed by a genuinely growing-rank
nibble problem.  This is not an affine or Boolean no-go; it is the exact
remaining physical matching gate.

## 6. Primary sources

1. N. Pippenger and J. Spencer, *Asymptotic behavior of the chromatic
   index for hypergraphs*, JCTA 51 (1989), 24--42:
   https://doi.org/10.1016/0097-3165(89)90074-5
2. N. Alon, B. Bollobas, J. H. Kim and V. H. Vu, *Economical covers
   with geometric applications*, PLMS 86 (2003), 273--308:
   https://web.math.princeton.edu/~nalon/PDFS/abkv4.pdf
3. S. Glock, F. Joos, J. Kim, M. Kuehn and L. Lichev,
   *Conflict-free hypergraph matchings*, JLMS 109 (2024):
   https://arxiv.org/pdf/2205.05564
4. M. Delcourt and L. Postle, *Finding an almost perfect matching in a
   hypergraph avoiding forbidden submatchings*:
   https://arxiv.org/pdf/2204.08981
5. S. Gould and T. Kelly, *Advancing the Rodl Nibble: New bounds on
   matchings and the list chromatic index of hypergraphs* (2025):
   https://arxiv.org/pdf/2511.11375
6. A. V. Kostochka and V. Rodl, *Partial Steiner systems and matchings
   in hypergraphs*, Random Structures & Algorithms 13 (1998), 335--347:
   https://doi.org/10.1002/(SICI)1098-2418(199810/12)13:3/4%3C335::AID-RSA8%3E3.0.CO;2-W
