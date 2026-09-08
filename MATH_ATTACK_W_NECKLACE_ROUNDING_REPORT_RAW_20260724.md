Lane W remains open. The strongest outcome is a sharp reduction to one support-feasible packet-gain lemma, plus an exact two-block necklace switching primitive. Independent or base-only nibbles provably retain Poisson-scale collision excess.

This lane is the direct even-dimensional construction with
\[
W=\binom{2m}{m},
\]
not the odd exact-factor synchronization problem. If completed, it constructs a literal OR word and bypasses MWB/SYNC; it does not prove labelled common-owner synchronization.

## 1. Radius and slot balance are automatic

Assume
\[
\frac h{\sqrt m}\to\infty,\qquad h=o(m^{2/3}),\qquad
h=o(\ell),\qquad \ell=o(m),\qquad R=2\ell,
\]
and put
\[
N_q=\binom{2m}{m-q},\qquad \rho_q=N_q/W.
\]

Use the radius law
\[
p_0=1-\rho_1,\qquad
p_d=\rho_d-\rho_{d+1}\ (1\le d<h),\qquad
p_h=\rho_h.
\]
Choose integers \(k_d\) with
\[
\left|k_d-\frac{Wp_d}{R}\right|\le1.
\]
Then
\[
\left|R\sum_{d=0}^h k_d-W\right|\le R(h+1)=o(W)
\]
and, writing
\[
V_h=W+2\sum_{q=1}^hN_q,
\]
\[
\left|R\sum_{d=0}^h(2d+1)k_d-V_h\right|
\le R(h+1)^2=o(W).
\]
This follows from
\[
\sum_dp_d=1,\qquad
\sum_d(2d+1)p_d=1+2\sum_{q=1}^h\rho_q.
\]

Thus the lane reduces to selecting exactly \(k_d\) physical blocks of each type with small collision excess.

There is also an exact rigidity inequality. For any selected multiset, let \(T_j,V_j,E_j,U_j\) be the slot count, class size, collision excess, and holes in the middle or one rank/sign class. Then
\[
T_j-V_j=E_j-U_j.
\]
Consequently
\[
\boxed{
|R|\mathcal M|-W|
+2\sum_{q=1}^h|Rn_{\ge q}-N_q|
\le 2E(\mathcal M)+|T(\mathcal M)-V_h|.
}
\]
Hence small total collision plus the single scalar ledger automatically forces aggregate rank-by-rank balance. A nibble cannot reduce collisions by moving a macroscopic number of slots between depths.

The basic coverage identity is
\[
\boxed{U(\mathcal M)=V_h-T(\mathcal M)+E(\mathcal M).}
\]
Therefore, on the rounded type fiber,
\[
E(\mathcal M)=o(W)
\quad\Longleftrightarrow\quad
U(\mathcal M)=o(W).
\]

## 2. Independent and base-only nibbles fail sharply

Let \(x_e\) be the canonical exact fractional typed cover, with
\[
\sum_{e\ni S}x_e=1,\qquad \varepsilon_m=\max_e x_e=o(1).
\]
Select blocks independently with probabilities \(x_e\). For the load \(C_S\),
\[
\mathbb E(C_S-1)_+
=\mathbb EC_S-\Pr(C_S>0)
=\Pr(C_S=0),
\]
and uniformly in \(S\),
\[
\Pr(C_S=0)=\prod_{e\ni S}(1-x_e)
=e^{-1+O(\varepsilon_m)}.
\]
Since
\[
V_h=(\sqrt\pi+o(1))W\sqrt m,
\]
this gives
\[
\boxed{
\mathbb EE
=\left(\frac{\sqrt\pi}{e}+o(1)\right)W\sqrt m.
}
\]

This concentration is genuine. If \(K_e=R(2d(e)+1)\), Efron–Stein gives
\[
\operatorname{Var}E
\le\sum_ex_eK_e^2
=WR\sum_dp_d(2d+1)^2
=O(WRm).
\]
Thus
\[
\frac{\operatorname{Var}E}{(\mathbb EE)^2}
=O(R/W)=o(1),
\]
so independent rounding has \(\Theta(W\sqrt m)\) collisions with high probability.

Imposing only projected-middle matching does not produce the missing correlation. In the degree-\(\Delta\) projected reservoir, for a nonmiddle target \(S\) and \(e\in\mathcal F_S\),
\[
\#\{f\in\mathcal F_S:\bar f\cap\bar e\ne\varnothing\}
\le
\left(2+o(1)\right)\frac{R\Delta}{m-h}
=o(\Delta).
\]
Hence \(1-o(1)\) of the pairs in every shadow clique remain compatible with the middle matching. Any base-matching nibble that factorizes asymptotically on compatible fixed tuples still produces Poisson-one shadow loads.

A successful color-balanced law must instead force
\[
\frac1{V_h}\sum_S\Pr(C_S=0)=o(m^{-1/2}),
\]
an improvement by a factor \(\omega(\sqrt m)\) over independent rounding.

## 3. Exact one-block descent is too weak

For same-type blocks \(A,B\), internal simplicity gives
\[
\boxed{
E(\mathcal M-A+B)-E(\mathcal M)
=
|(A\setminus B)\cap\{c=1\}|
-
|(B\setminus A)\cap\{c=0\}|.
}
\]
Thus a replacement descends exactly when it fills more current holes than the number of unique masks it destroys.

Averaging this inequality at a one-block local minimum over the transitive full type-\(d\) block family yields only
\[
\#\{c=1\}\ge(1-o(1))\#\{c=0\}.
\]
That permits macroscopic collision. For example, the abstract exact-ledger profile
\[
n_0=\frac25V_h,\qquad n_1=\frac25V_h,\qquad n_3=\frac15V_h
\]
satisfies \(n_1=n_0\) but has \(E=2n_3=2V_h/5\).

So transitivity plus one-block averaging cannot prove the theorem.

## 4. A genuine physical two-block switching primitive

There is an exact local move.

For one standard \(2\ell\)-block with direction word \(\pi\pi\), swapping adjacent directions:

- changes exactly two middle occurrences;
- for every \(1\le q\le\min(d,\ell-2)\), removes and adds exactly four lower and four upper masks;
- has zero signed effect at \(q=\ell-1\);
- preserves physical length, type, and every rank-slot total.

Its old-only mass is
\[
2+8\min(d,\ell-2).
\]

More importantly, two such switches can be coupled to preserve the middle layer. On \(Q=\{a,b,c,d\}\), take the old local paths
\[
ac\to bc\to bd,\qquad
ab\to ad\to cd,
\]
with pairings \(ab|cd\) and \(bd|ac\). Switch both to
\[
ac\to ad\to bd,\qquad
ab\to bc\to cd.
\]
If the two blocks have aligned outside active pairs, order, and marked state, then:

- the full middle multiplicity vector is unchanged;
- the two blocks are middle-disjoint;
- both depth-one lower and upper multiplicity vectors are unchanged;
- for every \(2\le q\le\min(d,\ell-2)\), each sign has exactly four removed and four added masks.

The total old-only mass is therefore
\[
8\max\{0,\min(d,\ell-2)-1\}.
\]

At depth \(q\), its lower effect has the exact rectangular form
\[
\Delta_q^-=
\sum_{\sigma=0}^1
\left[
(\mathbf1_{L_{\sigma,q}+b}-\mathbf1_{L_{\sigma,q}+c})
-
(\mathbf1_{R_{\sigma,q}+b}-\mathbf1_{R_{\sigma,q}+c})
\right],
\]
with the complementary formula upstairs. Thus it preserves context-row and local-colour column margins.

This is a real higher-depth, ledger-exact trade, but it does not close the lane:

- it cannot change depth-one excess;
- aligned partner blocks need not be present in the selected integral family;
- a fully occupied rectangle is collision-neutral;
- invariant margins can separate overload from holes;
- one switching bit simultaneously controls both signs, both halves, and every depth, whose preferred directions may conflict.

A global expansion/Hall theorem for these available rectangles is still missing.

There is also exact support rigidity: the middle support of one block induces \(C_R\) in the Johnson graph and determines its cyclic order up to dihedral symmetry. Hence a same-type one-block replacement preserving that middle support changes no certified shadow set. Useful switching must exchange ownership across multiple blocks.

## 5. Low excess is still structurally strong

Decompose the selected blocks into their \(R\) native typed chain segments. Call a chain bad if one of its certified masks occurs in another chain. A target of multiplicity \(c\ge2\) contaminates at most
\[
c\le2(c-1)
\]
chain occurrences. Therefore
\[
\boxed{\#\{\text{bad native chains}\}\le2E(\mathcal M).}
\]
Thus \(E=o(W)\) forces \(W-o(W)\) native chains to be individually collision-free. Low-excess rounding is weaker than conflict-free block matching—it may place one bad chain in every block—but it still demands an almost-everywhere clean, reservoir-adapted chain system.

## 6. Exact missing theorem

A noncircular sufficient statement is the following.

> **UNPROVED Packet-Gain Lemma.**  
> For the rounded type counts \(k_d\), there exist
> \[
> \eta_m\to0,\qquad s_m=o(W/R),
> \]
> such that every physical typed multiset \(\mathcal M\) with those counts and
> \(E(\mathcal M)>\eta_mW\) contains a removable packet \(\mathcal A\subseteq\mathcal M\) and a physical replacement packet \(\mathcal B\), both of size at most \(s_m\) and with the same type multiset, satisfying:
>
> 1. the net certified incidence change \(z\) lies in
>    \(\{-1,0,1\}^{\mathcal U_h}\);
> 2. more original holes are added than original unique masks are removed:
> \[
> \#\{S:z_S=1,\ c_S=0\}
> >
> \#\{S:z_S=-1,\ c_S=1\}.
> \]

For such a packet,
\[
\Delta E
=
\#\{z=-1,c=1\}-\#\{z=1,c=0\}\le-1.
\]
Finite integer descent therefore terminates with
\[
E\le\eta_mW=o(W).
\]

The rounded ledger then gives \(U=o(W)\). Using the already-audited typed-block realization, linearizing the cycles costs
\[
O(h|\mathcal M|)
=O(hW/R)=o(W),
\]
the uncovered band masks cost \(o(W)\), and the outer-tail word costs \(o(W)\). Hence the Packet-Gain Lemma would prove
\[
\nu(2m)\le W+o(W),
\]
followed by the standard parity lift.

The packet implication and ledger inequality were independently audited. The missing assertion is existence of the physical packets. Neither projected codegree, conflict-clique codegree, signed rectangle generation, nor the two-block diamond proves their support availability or multidepth gain.

So the genuinely exhausted boundary is:

\[
\boxed{
\text{prove a depth-one-capable, support-feasible packet expansion theorem;}
}
\]
the exact higher-depth diamond is available, but ordinary nibbling and uncoordinated switching provably do not reach it.
