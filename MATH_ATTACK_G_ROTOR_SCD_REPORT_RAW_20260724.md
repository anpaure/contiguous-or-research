# Mathematical attack G: rotor/SCD report

Date: 2026-07-24

## Verdict

The rotor/SCD route does **not** yet prove the contiguous-OR width conjecture. It does, however, resolve the flow/Euler/coloring part completely and reduces the route to one precise integral lemma about a single full SCD. The canonical Greene–Kleitman SCD and independent randomized recoloring both fail by a factor \(\Theta(\sqrt m)\).

### 1. Exact fixed-window rotor–SCD resolution theorem

Put

\[
W=\binom{2m}{m},\qquad N_d=\binom{2m}{m-d},\qquad
H=\lceil A\sqrt m\rceil
\]

for fixed \(A>0\), and define

\[
\gamma_d=
\begin{cases}
N_d-N_{d+1},&0\le d<H,\\
N_H,&d=H.
\end{cases}
\]

Clipping every chain of one full SCD \(\mathcal D\) to ranks \(m-H,\ldots,m+H\) gives

\[
\sum_{d=0}^H\gamma_d=W,\qquad
\sum_{d=q}^H\gamma_d=N_q.
\]

Here \(\gamma_H=N_H\) includes all original chains of radius at least \(H\), clipped to radius \(H\).

For a radius-\(d\) chain write

\[
\omega=(L;z_1,\ldots,z_{2d};R),\qquad |L|=|R|=r=m-d.
\]

Its rotor successors are

\[
(L-x+y;x,z_1,\ldots,z_{2d-1};R-y+z_{2d}),
\qquad x\in L,\ y\in R.
\]

Let \(F_d\) be a spanning vertex-disjoint directed path forest on the radius-\(d\) clipped chains of \(\mathcal D\), with \(p_d\) components, and put

\[
\Phi_H(\mathcal D)=\sum_{d=0}^H(2d+1)p_d.
\]

**Theorem.** With

\[
Q=(2m-1)(2m)!,
\]

there is an exact band rotor circulation colored with \(Q\) actual full-SCD colors—coordinate copies of \(\mathcal D\)—having at most

\[
Q\Phi_H(\mathcal D)
\]

weighted monochromatic run starts. Conversely, every such coloring of toll \(R\), with all circuit cuts and resets charged as hard run starts, contains a color satisfying

\[
\Phi_H(\mathcal D)\le \frac RQ.
\]

#### Proof of the integral orbit step

Let \(G=(2m)!\), \(s=2m-1\), and \(r=m-d\). The radius-\(d\) state set and rotor degrees are

\[
|\Omega_d|=\frac{G}{r!^2},\qquad \deg^+=\deg^-=r^2.
\]

Give every directed rotor arc multiplicity

\[
A_d=s\gamma_d(r-1)!^2.
\]

Then the number of transition heads is

\[
A_d|\Omega_d|r^2=Q\gamma_d,
\]

and every state occurs as a head \(s\gamma_dr!^2\) times. A fixed rank-\(m\pm q\) mask lies in \(|\Omega_d|/N_q\) radius-\(d\) states, so its designated multiplicity is

\[
\sum_{d=q}^H
\frac{|\Omega_d|}{N_q}\frac{Q\gamma_d}{|\Omega_d|}
=\frac Q{N_q}\sum_{d=q}^H\gamma_d=Q.
\]

Index colors by \((a,\sigma)\in[s]\times S_{2m}\), with color \((a,\sigma)\) carrying \(\sigma\mathcal D\). State and directed-arc stabilizers have sizes \(r!^2\) and \((r-1)!^2\). Since \(F_d\) has \(\gamma_d-p_d\) edges, its complete colored coordinate orbit uses every rotor arc exactly

\[
s(\gamma_d-p_d)(r-1)!^2
\]

times. The residual multiplicity is therefore

\[
sp_d(r-1)!^2
\]

per arc, giving \(sp_dr!^2\) residual incoming and outgoing arcs at every state.

The coordinate orbit has exactly the same \(sp_dr!^2\) path starts and path ends at every state. Pair residual arcs entering \(v\) bijectively with colored paths starting at \(v\), and prepend each connector to its path. Contracting these connector-plus-path trails gives a balanced directed macrograph. Eulerizing every nonempty weak component and expanding the macroedges partitions every master-arc copy. Each colored path is consecutive, yielding at most \(Qp_d\) runs.

The refined-prefix MTF lemma realizes each finite expanded circuit literally. Abstract return need not restore the complete MTF state, so each circuit is initialized separately. Its extra initialization is at most

\[
Q\sum_d(2d+2)p_d\le 2Q\Phi_H,
\]

hence negligible whenever \(\Phi_H=o(W)\).

This proves the theorem. It constructs the chronology; it does not color an arbitrarily frozen Euler tour.

### 2. Exact smallest unproved lemma

The route is now equivalent to the following statement.

> **Rotor path-forest lemma \(\mathrm{RSCD}_A\) — UNPROVED.**  
> For every fixed \(A>0\), there exists one full SCD \(\mathcal D_{m,A}\) of \(B_{2m}\) such that, after clipping at \(H=\lceil A\sqrt m\rceil\), its radius classes have spanning directed rotor path forests satisfying
> \[
> \boxed{\sum_{d=0}^H(2d+1)p_d=o(W).}
> \]

Equivalently, if \(\ell_d(\mathcal D)\) is the maximum number of edges in a spanning directed linear forest,

\[
\min_{\mathcal D\text{ full SCD}}
\sum_{d=0}^H(2d+1)
\bigl(\gamma_d-\ell_d(\mathcal D)\bigr)=o(W).
\]

This requires one full integral SCD simultaneously at every depth. A fractional SCD mixture, separate depthwise SCDs, or an unextendible band decomposition does not qualify.

A rotor path through \(t\) radius-\(d\) chains has literal length

\[
(2d+2)+(t-1)=t+2d+1.
\]

Thus \(\mathrm{RSCD}_A\) gives a central-band word of length

\[
W+\Phi_H=W+o(W).
\]

The audited outer-tail word has length

\[
O\!\left((1+A^2)e^{-A^2+o(1)}W\right).
\]

Hence

\[
\limsup_{m\to\infty}\frac{\nu(2m)}W
\le 1+O((1+A^2)e^{-A^2}).
\]

Letting \(A\to\infty\) would prove coefficient one in even dimension. The lift

\[
\nu(2m+1)\le 2\nu(2m)+1
\]

then gives the odd case because

\[
\binom{2m+1}{m}
=\frac{2m+1}{m+1}\binom{2m}{m}.
\]

### 3. Canonical BTK/GK obstruction

**Theorem.** No two positive-radius chains in the Greene–Kleitman/BTK SCD are joined by a directed same-radius rotor edge.

Encode a BTK chain by a ballot word. Match every \(D\) to the most recent unmatched \(U\). For a word ending at height \(2d\), let \(L\) be its \(D\)-positions, \(R\) its matched \(U\)-positions, and

\[
z_1<\cdots<z_{2d}
\]

its persistent unmatched \(U\)-positions.

A rotor successor using \(x\in L\), \(y\in R\) would change only

\[
q_x:D\to U,\qquad q_y:U\to D
\]

and would require its persistent \(U\)-sequence to be

\[
x,z_1,\ldots,z_{2d-1}.
\]

Thus \(x<z_1\).

- If \(x<y\), the old stack immediately before \(x\) is nonempty. If the new \(U\) at \(x\) survived, everything below it would survive, producing a persistent \(U\) before \(x\), contradiction.

- If \(y<x\), the two words have identical heights and letters from time \(x\) onward. The new \(x\) occupies the same stack depth as an old pre-\(x\) \(U\). Since \(z_1>x\), that old stack item is eventually popped; the identical future height descent also pops \(x\), contradiction.

Therefore the BTK positive-radius induced rotor graph is empty. Coordinate relabeling preserves this fact.

For the fixed window, all radius-\(d\) pieces with \(1\le d<H\) are unchanged BTK chains. Consequently every permuted-BTK color has toll at least

\[
L_{m,H}=\sum_{d=1}^{H-1}(2d+1)(N_d-N_{d+1}).
\]

Uniformly for \(d\le A\sqrt m\),

\[
\frac{N_d}{W}
=\exp\!\left(-\frac{d^2}{m}+O_A(m^{-1})\right),
\]

so

\[
\frac{L_{m,H}}{W\sqrt m}
\longrightarrow
4\int_0^A x^2e^{-x^2}\,dx
=\sqrt\pi\,\operatorname{erf}(A)-2Ae^{-A^2}>0.
\]

Thus the canonical BTK orbit misses the target by \(\Theta(\sqrt m)\). This theorem does not cover the clipped radius-\(H\) class, but the lower radii already suffice for the obstruction.

### 4. Independent randomized recoloring also fails

For the coordinate-orbit resolution, a labelled radius-\(d\) chain belongs to

\[
M_d=(2m-1)\gamma_d(m-d)!^2
\]

admissible SCD colors and has the same number of rotor occurrences. Assigning occurrences to admissible colors by independent uniform typewise bijections preserves exact integral SCDs.

The all-start weight is

\[
\begin{aligned}
U_H
&=Q\left(\sum_{d<H}(2d+1)(N_d-N_{d+1})
 +(2H+1)N_H\right)\\
&=Q\left(W+2\sum_{q=1}^H N_q\right).
\end{aligned}
\]

For adjacent distinct chain types, independent color assignments agree with probability at most \(1/(2m-1)\). Hence expected saved weight is at most \(U_H/(2m-1)=o(QW)\). Meanwhile

\[
\frac{U_H}{QW}
=\sqrt\pi\,\operatorname{erf}(A)\sqrt m+O_A(1).
\]

Markov’s inequality therefore gives, with high probability,

\[
R_H=U_H-o(QW)
=\bigl(\sqrt\pi\,\operatorname{erf}(A)+o(1)\bigr)QW\sqrt m.
\]

So independent recoloring is essentially maximally switched.

A deterministic necessary pair-capacity test is also available. If \(a_d\) is the multiplicity of a rotor arc \(e=(\sigma,\tau)\) and

\[
B_e=|A_\sigma\cap A_\tau|,
\]

then at most \(B_e\) copies of \(e\) can be monochromatic. Therefore

\[
R_d\ge(2d+1)\sum_e(a_d-B_e)_+.
\]

For the orbit of one SCD \(\mathcal D\), this implies

\[
R_d\ge Q(2d+1)
\bigl(\gamma_d-e_d(\mathcal D)\bigr)_+,
\]

where \(e_d(\mathcal D)\) is the number of induced directed rotor arcs. This is necessary but weaker than the path-forest lemma because it does not enforce consistent routing.

### 5. Relation to the new fixed-window \(CA_A\) reduction

The fixed-window diagonalization is fully compatible with the rotor result: one should prove the theorem for every fixed \(A\), then let \(A\to\infty\) slowly. Bounded odd-wreath capacities do not, however, identify the two problems.

A clipped even SCD has only \(N_q\) middle chains reaching depth \(q\), each with unit ownership. Odd \(CA_A\) requires all \(W\) exact-wreath owners to participate in one common nested map with \(c_q/c_q+1\) fibres. Therefore \(\mathrm{RSCD}_A\) would bypass \(CA_A\) by proving the OR bound directly; it would not prove the exact odd synchronization theorem or construct its factor/resolution pair.

Likewise, the new adjacent-swap owner operation is a promising rank-isolated way to alter a common nested resolution, but it does not yet supply the simultaneous ordered-label overlap and whole-chain disjointness required by a rotor path forest. Its remaining Hall/toggle lemma and \(\mathrm{RSCD}_A\) remain distinct unproved correlation problems.

The safe overload tail beginning at any fixed \(\alpha\sqrt{m\log m}\), \(\alpha>1/\sqrt2\), is orthogonal to this obstruction: the rotor difficulty already occurs inside every fixed \(A\sqrt m\) band.

### Adversarial audit

The orbit theorem passed independent counting and logic audits. The required qualifications are:

- chronology is constructed, not frozen;
- macrograph balance gives several Euler circuits, not necessarily one;
- every circuit cut/reset counts as a run start;
- occurrences are designated post-transition occurrences; initialization may add incidental witnesses;
- abstract rotor closure is not physical MTF-state closure;
- the forest must be spanning, directed, and vertex-disjoint;
- the radius-\(H\) class consists of clipped longer chains;
- the full SCD must exist before clipping;
- no implication to odd \(CA_A\) is claimed.

With these corrections, the flow/Euler theorem is rigorous. The conjecture remains open exactly at \(\mathrm{RSCD}_A\).

## Later logical correction

The fixed-window **overload** statement

\[
\min_F\sum_{q\le A\sqrt m}\frac{O_q(F)}{c_q}=o(W)
\quad\text{for every fixed }A
\]

is equivalent by diagonalization to overload MWB.

The labelled common-owner statement

\[
\exists(F,P):\quad
\sum_{q\le A\sqrt m}\frac{e_q(F,P)}{c_q}=o(W)
\]

is only a stronger sufficient theorem, since \(O_q(F)\le e_q(F,P)\). The converse is unproved: close unlabelled histograms need not admit a nearby common nested labelled flow.

The rotor path-forest lemma would bypass both by directly constructing an even-dimensional OR word. It proves neither overload MWB nor the stronger labelled synchronization theorem. The adjacent-swap owner operation belongs specifically to the stronger labelled route.

## Independent audit corrections

The orbit counts, stabilizers, residual connector pairing, macrograph
balance, and initialization accounting are correct after two formulation
repairs. First, the displayed positive-radius rotor successor does not apply
at d=0; there the legal transition is the ordinary swap

\[
(L;\,;R)\longmapsto(L-x+y;\,;R-y+x).
\]

Also assume H<=m-1 (automatic for every fixed-A window and sufficiently
large m).

Second, the converse statement is false for an arbitrarily preselected
spanning forest. Define instead

\[
\Phi_{\min}(\mathcal D)=
\min_{(F_d)}\sum_{d=0}^H(2d+1)p_d,
\]

where the minimum ranges over spanning directed vertex-disjoint rotor path
forests in every clipped radius class of the fixed full SCD. The orbit/Euler
construction gives toll at most Q times the toll of any chosen forests, and
the optimized coordinate-color construction is governed by
Q Phi_min. A bad preselected forest need not reflect the best coloring: at
m=2,H=1 one SCD admits both a singleton forest of toll 14 and a forest using
one rotor edge of toll 11.

The independent-recoloring probability argument additionally fixes the
Euler routing/linear chronology before the random typewise color bijections
are sampled. If routing is optimized adaptively after seeing the colors,
the adjacent pairs are selected color-dependently and the 1/(2m-1)
calculation does not apply. The routing-independent pair-capacity lower
bound remains valid. With these qualifications, the BTK obstruction and the
positive orbit construction survive; RSCD_A remains a sufficient direct OR
route, not a necessary gate for the conjecture.
