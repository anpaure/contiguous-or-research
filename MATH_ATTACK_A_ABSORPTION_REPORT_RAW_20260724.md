# Raw lead report: weighted wreath absorption

## Verdict

This route does **not** prove ABS, labelled synchronization, or the contiguous-OR width conjecture.

It does produce a genuine absorber theorem: every rooted four-label window of a wreath has factorially many profile-\(3\) balanced \(C_8\) partners. The decisive negative result is that these absorbers are too seam-local: any \(o(W/n)\)-sized family changes the fixed-window weighted overload by only \(o(W)\). Thus a standard sparse absorber cannot perform the missing global balancing; it can only preserve or clean a factor already within \(o(W)\) of the target.

Write
\[
B=\frac Wn,\qquad K_A=\lceil A\sqrt m\rceil,\qquad
a_q=\frac W{N_q}.
\]

## 1. Fixed-window estimates

Uniformly for fixed \(A\) and \(q\le K_A\),
\[
\log a_q=\frac{q(q+1)}m+O_A(m^{-1})
=\frac{q^2}{m}+O_A(m^{-1/2}).
\]
This follows by expanding
\[
\sum_{i<q}\left[
\log\left(1+\frac{i+2}{m}\right)
-\log\left(1-\frac{i}{m}\right)\right].
\]

Consequently \(1\le c_q\le C_A\), and
\[
\sum_{q\le K_A}\frac1{c_q}
=(\kappa_A+o_A(1))\sqrt m,
\qquad
\kappa_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor},
\tag{1}
\]
while
\[
\sum_{q\le K_A}\frac q{c_q}
=(\lambda_A+o_A(1))m,
\qquad
\lambda_A=\int_0^A\frac{x\,dx}{\lfloor e^{x^2}\rfloor}.
\tag{2}
\]
Both are ordinary Riemann sums; the floor has only finitely many discontinuities on a fixed window.

For
\[
Q^2/m=\tfrac12\log m-\tfrac12\log\log m+\omega(1),
\]
Gaussian summation gives
\[
\sum_{q\ge Q}\frac1{c_q}
=O\!\left(\frac mQe^{-Q^2/m+o(1)}\right)=o(1).
\tag{3}
\]
Thus
\[
\sum_{q\ge Q}\frac{O_q(F)}{c_q}=o(W)
\]
for every exact factor. Any fixed \(Q=\alpha\sqrt{m\log m}\) with \(\alpha>1/\sqrt2\) is safely above this threshold.

Also,
\[
\sum_{q<Q}\frac1{c_q}
=(\kappa_\infty+o(1))\sqrt m,
\]
where
\[
\kappa_\infty
=\int_0^\infty\frac{dx}{\lfloor e^{x^2}\rfloor}
=\sum_{j\ge1}
\frac{\sqrt{\log(j+1)}-\sqrt{\log j}}j,
\quad
\frac{\sqrt\pi}{2}\le\kappa_\infty\le\sqrt\pi.
\tag{4}
\]

## 2. Exact absorption algebra

Let \(F=M\sqcup C\), \(R=|C|\), and let \(M\) be safe for quotas \(b_q\). Put
\[
s_q=b_q-\mu_q^M.
\]
Then, pointwise,
\[
\boxed{
(\mu_q^C-s_q)_+=(\mu_q^F-b_q)_+.
}
\tag{5}
\]

Thus ABS is algebraically a statement about the final factor \(F\); the role of \(M\) is only to certify it through \(s_q\ge0\) and a small or well-aligned completion.

Moreover,
\[
\sum_Ss_q(S)=\sum_S\mu_q^C(S)=nR,
\]
so
\[
\sum_S(\mu_q^C(S)-s_q(S))_+
=\frac12\|\mu_q^C-s_q\|_1\le nR.
\tag{6}
\]
Using (4),
\[
R=o\!\left(\frac{W}{n\sqrt m}\right)
\quad\Longrightarrow\quad
\mathrm{ABS}=o(W).
\tag{7}
\]
An \(O(W/(n\sqrt m))\) leave yields only \(O(W)\), so the little-\(o\) is essential.

### Completion-support obstruction

Let \(U\) be the \(nR\) middle sets covered by \(C\), and define
\[
d_U(S)=|\{X\in U:S\subset X\}|.
\]
If \(\mu_q^C(S)>0\), then
\[
\boxed{d_U(S)\ge q+1.}
\tag{8}
\]
Indeed, if \(S=I_\pi(j,m-q)\), the sets
\[
I_\pi(j-t,m),\qquad 0\le t\le q,
\]
are \(q+1\) distinct middle intervals in the same completion wreath containing \(S\).

Hence, with \(T_q(U)=\{S:d_U(S)\ge q+1\}\),
\[
\sum_S(\mu_q^C(S)-s_q(S))_+
\ge
\left[nR-\sum_{S\in T_q(U)}s_q(S)\right]_+.
\tag{9}
\]
Total slack \(nR\) is therefore insufficient: it must be concentrated on shadows supported by the same cyclically decomposable leave.

The leave is point-regular,
\[
|\{X\in U:x\in X\}|=mR,
\]
but point-regularity does not imply (8) or the required higher-order Hall expansion.

## 3. Exact common-owner extension criterion

Let \(M\) be a partial wreath matching, \(U\) its uncovered roots, and
\[
\ell_q(S)=\max(0,c_q-\mu_q^M(S)),
\qquad
u_q(S)=c_q+1-\mu_q^M(S).
\]
The actual flags of \(M\) extend to one balanced nested resolution iff there are integer residual loads \(g_q\) satisfying
\[
\ell_q\le g_q\le u_q,\qquad \sum_Sg_q(S)=|U|,
\tag{10}
\]
and, for every adjacent layer and every upper family \(\mathcal A\),
\[
\boxed{
g_{q-1}(\mathcal A)\le g_q(\partial\mathcal A).
}
\tag{11}
\]

Proof: clone every node according to \(g_q(S)\). Equation (11) is precisely Hall’s condition for a perfect matching between consecutive clone layers. Integral matchings at all adjacent layers concatenate into \(|U|\) nested paths.

Thus rankwise quota safety is not enough. The residual loads must satisfy a global Hall system at every adjacent pair of ranks.

## 4. Factorially many short-profile \(C_8\) absorbers

Represent a wreath by its cyclic omitted-label word \(z\), with
\[
A_i(z)=\{z_{i+1},z_{i+3},\ldots,z_{i+2m-1}\}.
\]

Fix a rooted four-label window of an oriented wreath \(e\), and write
\[
z^e=(a,c,b,d,x_1,y_1,\ldots,x_{m-2},y_{m-2},x_{m-1}),
\]
where \(X=\{x_i\}\), \(|X|=m-1\), and \(Y=\{y_i\}\), \(|Y|=m-2\).

For every \(\sigma\in\operatorname{Sym}(X)\) and
\(\tau\in\operatorname{Sym}(Y)\), define
\[
z^{f_{\sigma,\tau}}
=(c,d,a,b,\sigma_1,\tau_1,\ldots,
  \sigma_{m-2},\tau_{m-2},\sigma_{m-1}).
\tag{12}
\]

### Rooted partner theorem

Every \(f_{\sigma,\tau}\):

1. is middle-disjoint from \(e\);
2. participates with \(e\) in a balanced alternating \(C_8\);
3. has cut profile \(\{3,n-3\}\) on both old wreaths; and
4. yields, after toggling, two disjoint \(n\)-cycles \(g,h\) satisfying
   \[
   V(e)\dot\cup V(f_{\sigma,\tau})
   =V(g)\dot\cup V(h).
   \]

There are exactly
\[
\boxed{(m-1)!(m-2)!}
\tag{13}
\]
distinct unoriented partner wreaths for the rooted window.

### Proof

The possible traces on \(Q=\{a,b,c,d\}\) of vertices of \(e\) are
\[
\{cd,b,ad,c,ab\},
\]
whereas those of \(f_{\sigma,\tau}\) are
\[
\{bd,a,bc,d,ac\}.
\]
These disjoint families partition all four singleton and all six two-element subsets of \(Q\); hence the two wreath supports are disjoint.

The eight vertices
\[
E_1,E_0,F_1,F_0,E_3,E_4,F_3,F_4
\]
form the universal alternating cycle with omitted-label word
\[
a,b,c,a,d,c,b,d.
\]
The two removed edges in each wreath cut off its three-vertex path
\[
E_1,E_2,E_3
\quad\text{or}\quad
F_1,F_2,F_3.
\]
Each new component joins one such path to an \((n-3)\)-vertex path, so both have length \(n\).

Finally the fixed directed label block \(c,d,a,b\) recovers the root and orientation of \(f\), after which its remaining word recovers \((\sigma,\tau)\). Hence all partners in (13) are distinct.

As a middle-hypergraph gadget,
\[
\{f\}\longleftrightarrow\{g,h\}
\]
is a genuine absorber for the target block \(V(e)\).

## 5. Sparse-\(C_8\) invariance theorem

A profile-\(3\) switch changes the orientation-independent depth-\(q\) histogram on exactly
\[
r_1=8,\qquad r_q=4q+6\quad(q\ge2)
\tag{14}
\]
removal/addition slots.

For the original pointed flags, orient each new cycle to preserve its long inherited path. Only one three-vertex path must reverse, giving at most
\[
\widetilde r_1=9,\qquad
\widetilde r_q=4q+6\quad(q\ge2)
\tag{15}
\]
changed owners.

Let
\[
\Phi_A(F)=\sum_{q\le K_A}\frac{O_q(F)}{c_q},
\qquad
\mathcal E_A(F)=
\min_P\sum_{q\le K_A}\frac{e_q(F,P)}{c_q},
\]
where the second minimum is over common balanced nested resolutions.

For one rooted switch,
\[
|\Phi_A(F')-\Phi_A(F)|
\le4T_A+6S_A-2=O_A(m),
\tag{16}
\]
and
\[
|\mathcal E_A(F')-\mathcal E_A(F)|
\le4T_A+6S_A-1=O_A(m).
\tag{17}
\]
The overload bound follows because moving one occurrence changes optimal overload by at most one. The labelled bound holds for every fixed \(P\), hence also after minimizing over \(P\) in both directions.

After \(t\) such trades, telescoping gives \(O_A(tm)\). Since
\[
W=nB=(2m+1)B,
\]
we obtain:

\[
\boxed{
t=o(B)
\Longrightarrow
|\Phi_A(F')-\Phi_A(F)|+
|\mathcal E_A(F')-\mathcal E_A(F)|
=o(W).
}
\tag{18}
\]

In particular, a conventional square-root absorber with
\[
t=O(B/\sqrt m)
\]
has total repair capacity only
\[
O_A(W/\sqrt m)=o(W).
\tag{19}
\]

Therefore a sparse \(C_8\) absorber cannot turn a \(\Theta(W)\) spill or owner defect into \(o(W)\). It can only preserve or clean a coarse construction that is already \(o(W)\)-close. Correcting a linear defect requires \(\Omega(B)\) trade uses, or a reservoir whose wreaths are reused mesoscopically.

## 6. Test against the exact owner-flow cut condition

At depth \(q\), let \(G_q\) be the sibling multigraph in which each owner edge joins its two possible intermediate \(q\)-sets. A prescribed indegree vector \(b_q\) is feasible iff, for every \(U\subseteq V(G_q)\),
\[
\boxed{
e_{G_q}(U)\le b_q(U)
\le e_{G_q}(U)+|\delta_{G_q}(U)|.
}
\tag{20}
\]

For a rooted profile-\(3\) switch, only \(O(q)\) owner edges change. Thus every cut expression in (20) changes by \(O(q)\). More exactly, if
\[
I_G(U)=e_G(U)+|\delta_G(U)|,
\]
state \(1\) is feasible relative to a feasible state \(0\) iff
\[
b(U)-e_0(U)\ge(e_1(U)-e_0(U))_+,
\tag{21}
\]
\[
I_0(U)-b(U)\ge(I_0(U)-I_1(U))_+
\tag{22}
\]
for every \(U\).

This still does not make the absorber a common-flow gadget:

- all owner edges of one \(C_8\) form one binary bundle;
- the same bundle bit must be used at every depth;
- different middle-disjoint absorbers may attack the same cut;
- rankwise feasible orientations need not form one nested resolution.

Most importantly, minimum labelled-toggle cost is not Lipschitz under sparse graph edits. Take a clockwise \(C_N\) with indegree quota one, and replace \(\{N,1\}\) by \(\{N,k\}\), \(k\sim N/2\). Both graphs satisfy (20), but the attached path
\[
k\to k-1\to\cdots\to1
\]
is forced, reversing \(\Theta(N)\) unchanged edges. One changed option edge can therefore cause a global toggle cascade.

## 7. Exact remaining lemma

For overload MWB, the minimal missing statement remains the fixed-window weighted spill theorem:

> For every fixed \(A\), construct one exact factor \(F=M\sqcup C\), quota-safe \(M\), and quotas \(b_q\) such that
> \[
> \sum_{q\le A\sqrt m}\frac1{c_q}
> \sum_S(\mu_q^C(S)-s_q(S))_+=o(W).
> \tag{\(\mathrm{EABS}_A\)}
> \]

For the stronger common-owner theorem, a genuine absorber must additionally prove a bundled short-correction-flow estimate. In the adjacent-swap formulation this is
\[
\sum_{q\le K_A}\frac{
\operatorname{dist}_{\rm toggle}
\left(
\mathcal O_{q,0},
\{\mathcal O:\operatorname{indeg}\mathcal O=b_q
\text{ in the required absorber state}\}
\right)}
{c_q}
=o(W),
\tag{23}
\]
with the selected orientations coupled across depths into one nested resolution and the same absorber state bits used at every rank.

Equivalently, the missing object is a mesoscopic decorated cover-down theorem, not another local \(C_8\) count:

- the coarse leave must already be partitioned into cyclically extendible target packets;
- its slack must satisfy the support condition (9);
- all residual Hall cuts must survive the bundled absorber states;
- and global orientation corrections must have weighted cost \(o(W)\).

No such theorem is proved.

## 8. Conditional implication to the conjecture

If \((\mathrm{EABS}_A)\) holds for every fixed \(A\), choose thresholds \(M_j\ge j^4\) so its normalized error is at most \(1/j\) for \(m\ge M_j\), and put
\[
A(m)=\max\{j:M_j\le m\}.
\]
Then \(A(m)\to\infty\), \(A(m)\le m^{1/4}\), and
\[
H=A(m)\sqrt m=o(m).
\]
The resulting single exact factor has weighted overload \(o(W)\) through \(H\). Hence
\[
\sum_{q\le H}M_q=o(W),
\qquad
\frac{HW}{m}=o(W),
\]
while the symmetric-chain product covers both outer tails in \(o(W)\) because \(H/\sqrt m\to\infty\). Therefore
\[
\nu(2m+1)\le W+o(W),
\]
and the trimmed one-bit lift gives
\[
\nu(k)=(1+o(1))
\binom{k}{\lfloor k/2\rfloor}.
\]

The analogous labelled fixed-window theorem also implies this, but it is strictly stronger.

## Adversarial audit

The strongest claims survive the following checks:

- ABS is only overload control; it does not produce a nearby common nested owner flow.
- Fixed-window overload diagonalization is equivalent to overload MWB, not labelled SYNC.
- Histogram seam cancellation does not automatically control pointed flags; the profile-\(3\) orientation audit accounts for the forced short-path reversal.
- A \(C_8\) is a real absorber, but only for a leave already equal to a wreath block.
- Factorial ambient abundance does not give a disjoint decorated absorber reservoir.
- Sparse cut perturbation does not imply sparse minimum-toggle cost.
- Bounded fixed-window capacities do not make generic matching theorems applicable: the base wreath size is still \(2m+1\), and every \(d\)-regular wreath family has
  \[
  \frac{\Delta_2}{d}\ge\frac2{m+1}.
  \]
- The cardinal leave threshold requires little-\(o\), not big-\(O\).
- The sharp deep-tail cutoff must approach the \(1/\sqrt2\) constant from the correct second-order side.

So the route is genuinely exhausted at a new global lemma: a linear/mesoscopic, bundled, cyclic cover-down and correction-flow theorem. Local or sparse wreath absorption cannot by itself close the conjecture.

## Independent audit corrections

The rooted profile-3 partner construction is valid for (mge2), and the
normalized rooted template has exactly ((m-1)!(m-2)!) unoriented partners.
For exhaustivity, after normalizing
(f=(c,d,a,b,w_4,ldots)), the condition (E_0cap F_1=arnothing)
forces the even tail positions to be exactly (X), hence the odd tail
positions exactly (Y); the fixed directed four-letter block prevents
dihedral collisions.

The quantities
[
r_1=8,qquad r_q=4q+6quad(2le qle m-1)
]
are exact seam removal/addition masses
(sum_{ellin{3,n-3,3,n-3}}min(ell,2q)).  They are not, in
general, the number of nonzero histogram changes or the half-(ell_1)
distance.  At (q=m) the histogram change is zero.  Likewise, the pointed
counts (9) and (4q+6) are upper bounds, not exact counts.  These weaker
statements are all that the fixed-(A) Lipschitz argument needs.

Equations (5)--(7) assume that every balanced quota vector has total (W)
and that (C) is the whole-wreath complement in an exact factor.  The
cardinality leave condition is sufficient, not necessary: aligned slack can
make a larger leave cheaper.  The support condition (d_U(S)ge q+1) is
only a necessary coarse test and is not sufficient for cyclic completion.
The common-owner Hall criterion is an iff statement only for nonnegative
integer residual loads across all relevant levels; it extends flags after
their middle roots are fixed and does not itself cyclically complete (U).

All sparse-switch estimates are fixed-window statements; their constants
are not uniform for (A=A(m)	oinfty).  Finally,
((mathrm{EABS}_A)) is an equivalent rewriting of fixed-window overload
MWB, not a separate stronger absorber theorem: equation (5) identifies its
objective with the final overload, and (M=arnothing) is always
quota-safe.
