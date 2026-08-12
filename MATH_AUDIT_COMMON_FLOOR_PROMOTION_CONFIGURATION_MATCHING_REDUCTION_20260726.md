# Common-floor promotion configurations: exact matching reduction and its global gate

Date: 2026-07-26

Method: pure mathematics only. No computation, search, or external
matching theorem is used.

## 0. Verdict

Let

\[
 H=\left\lfloor\sqrt{m\log m}\right\rfloor,\qquad
 M=m+H,\qquad
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad N=N_H.
\tag{0.1}
\]

For \(1\le q\le H\), put

\[
 k_q=\left\lfloor\frac{N_q}{N}\right\rfloor,\qquad
 r_q=N_q-k_qN.
\tag{0.2}
\]

The proposed common-floor reduction is correct after three conventions
are made explicit:

1. every cyclic frame has a distinguished phase, because the aligned
   prefixes \(\{0,\ldots,k_q-1\}\) are otherwise undefined;
2. configurations are retained as parallel labelled hyperedges when
   distinct rooted frames have the same physical cell set; and
3. root selectors and physical rank-\((m-H)\) cells are typed copies
   (or else the redundant root/lower-\(H\) copy is identified and the
   edge rank drops by one).

There is an edge-transitive physical configuration multihypergraph
\(\mathcal C_{m,H}\) with exactly

\[
                         K=k_1+2\sum_{q=1}^H k_q
                         =O(m^{3/2})
\tag{0.3}
\]

physical cells in every edge, in addition to one typed root selector.
Its uniform point is a fractional matching of value exactly \(N\).

If

\[
 \boxed{\nu(\mathcal C_{m,H})
       =N-o(N/\sqrt m),}
\tag{0.4}
\]

then the selected configuration paths and literal singleton repairs give
a central-through-\(H\) Boolean-OR word of length

\[
 \boxed{
 W+2HN+2\sum_{q=1}^H r_q
   +2L\sum_{q=1}^H k_q,}
\qquad L=N-\nu(\mathcal C_{m,H}),
\tag{0.5}
\]

which is \(W+o(W)\). Appending the already audited economical exterior
word preserves this bound and yields the coefficient-one conclusion.

Thus (0.4) is a valid sufficient theorem. It is not proved by
edge-transitivity: averaging a maximum matching only says that its
incidence vector is the factor \(\nu/N\) times the uniform fractional
point. Nor is (0.5) an exact SCD/fcpath completion; it is a direct literal
word with appended holes. This distinction does not weaken its
coefficient-one implication.

The block-factor hole theorem applies at this new profile as well. Any
product-block proof of (0.4) would need blocks of order
\(\binom mH\). Hence (0.4) remains a fibre-dense global matching theorem,
not a local nibble or absorption consequence.

## 1. The common nested floor profile

The sequence \(N_q\) is decreasing in \(q\), so

\[
                         k_1\ge k_2\ge\cdots\ge k_H=1.
\tag{1.1}
\]

For a root \(A\in\binom{[2m]}{m-H}\), put \(U=A^c\), so \(|U|=M\).
Choose a directed cyclic order \(\pi\) of \(U\) and distinguish phase
zero. For a phase \(j\in\mathbb Z_M\), its middle owner and signed
depth-\(q\) traces are, up to the fixed harmless phase convention,

\[
 X_j=A\cup I_\pi(j,H),
\tag{1.2}
\]

\[
 X_{j,q}^-=A\cup I_\pi(j+q,H-q),\qquad
 X_{j,q}^+=A\cup I_\pi(j-q,H+q).
\tag{1.3}
\]

At depth \(q\), activate precisely the phases

\[
                         P_q=\{0,1,\ldots,k_q-1\}.
\tag{1.4}
\]

Equation (1.1) makes these activation sets nested. Equivalently phase
\(j<k_1\) receives the radius

\[
                         d_j=\max\{q:j<k_q\}.
\tag{1.5}
\]

There is exactly one radius-\(H\) phase because \(k_H=1\). The active
middle phases form one cyclic interval \(P_1\), and hence one promotion
path after the cyclic edge at its boundary is cut.

For each fixed phase \(j\), the masks in (1.2)--(1.3) form one literal
saturated symmetric chain through its assigned radius. Indeed, increasing
\(q\) by one removes the first label from the lower interval and adds the
preceding label to the upper interval:

\[
 X^-_{j,q+1}\subset X^-_{j,q}\subset X_j
 \subset X^+_{j,q}\subset X^+_{j,q+1},
\tag{1.6}
\]

and every displayed inclusion changes cardinality by one. Thus the floor
profile is not merely a marginal table; it is one nested flag assignment
inside every configuration.

### Lemma 1.1 (exact intraconfiguration cell count)

For a fixed rooted frame:

1. the \(k_1\) middle cells in (1.2) are distinct;
2. for each \(q<H\), the \(k_q\) lower cells and the \(k_q\) upper cells
   in (1.3) are separately distinct; and
3. at \(q=H\), the sole lower cell is \(A\), while the sole upper cell
   is well defined.

Consequently the number of typed physical cells is exactly (0.3).

#### Proof

For \(q<H\), the interval lengths \(H-q\), \(H\), and \(H+q\) all lie
strictly between zero and \(M\), since \(2H<M\). In a cyclic order of
distinct labels, equal proper intervals of one fixed length have equal
starting phase. Thus different active phases give different cells at
the same typed rank. At \(q=H\), all lower traces would equal \(A\), but
\(k_H=1\), so no repetition occurs. Different signed depths have
different cardinalities and are typed separately. \(\square\)

## 2. The physical configuration hypergraph

Let \(\mathcal C_{m,H}\) have:

* a typed selector vertex for every root
  \(A\in\binom{[2m]}{m-H}\);
* a typed middle vertex for every \(m\)-set;
* for each \(1\le q\le H\), typed lower and upper vertices for every
  set of ranks \(m-q\) and \(m+q\), respectively; and
* one labelled edge for every rooted directed frame, consisting of its
  root selector and all cells in Lemma 1.1.

Retaining rooted frames as labelled parallel edges avoids an irrelevant
injectivity question about the map from frames to cell sets. Let
\(\Delta\) be the number of rooted directed frames at one root
(\(\Delta=M!\) under the usual directed-cycle-modulo-rotation
convention followed by a choice of origin).

### Theorem 2.1 (edge transitivity and exact fractional matching)

The symmetric group on \([2m]\) is transitive on the labelled edges of
\(\mathcal C_{m,H}\). Giving every edge weight \(1/\Delta\) is a
fractional matching of total value \(N\), and therefore

\[
                         \nu^*(\mathcal C_{m,H})=N.
\tag{2.1}
\]

#### Proof

A coordinate permutation can map any root to any other root and then
map the ordered labels in one rooted cyclic frame, position by position,
to those in the other. This proves edge transitivity.

Every root selector has degree \(\Delta\), hence fractional load one.
The action on each typed physical rank is transitive. Double-counting
incidences gives middle degree \(d_0\) and signed depth-\(q\) degree
\(d_q^\pm\) satisfying

\[
 Wd_0=N\Delta k_1,\qquad
 N_qd_q^\pm=N\Delta k_q.
\tag{2.2}
\]

Thus their fractional loads are

\[
 \frac{d_0}{\Delta}=\frac{Nk_1}{W}\le1,\qquad
 \frac{d_q^\pm}{\Delta}=\frac{Nk_q}{N_q}\le1.
\tag{2.3}
\]

The uniform point is feasible and has total edge weight
\((N\Delta)/\Delta=N\). Root-selector capacity bounds every fractional
matching by \(N\), proving (2.1). \(\square\)

### Proposition 2.2 (what edge transitivity does and does not give)

Let \(\nu=\nu(\mathcal C_{m,H})\). Averaging one maximum matching under
the symmetric-group action produces a distribution for which every
labelled edge is selected with probability

\[
                         \frac{\nu}{N\Delta}
 =\frac{\nu}{N}\frac1\Delta.
\tag{2.4}
\]

Hence its expected incidence vector is exactly \(\nu/N\) times the
uniform fractional incidence vector. This is the claimed weighted
representative constant. It is an identity conditional on \(\nu\);
it gives no lower bound on \(\nu\).

#### Proof

There are \(N\Delta\) labelled edges. Transitivity makes their inclusion
probabilities equal after averaging, and their sum is the matching size
\(\nu\). Equation (2.4) follows. \(\square\)

## 3. All asymptotic counts

By definition,

\[
                         0\le r_q<N,
\qquad
                         \sum_{q=1}^H r_q<HN.
\tag{3.1}
\]

The critical binomial ratio satisfies

\[
 \lambda_H:=\frac WN=(1+o(1))m,
\tag{3.2}
\]

and therefore

\[
 N=(1+o(1))\frac Wm,\qquad HN=o(W).
\tag{3.3}
\]

It remains to control the edge size. Uniformly for \(q\le H\),

\[
 \log\lambda_q
 =\frac{q^2}{m}
  +O\!\left(\frac{q^2}{m^2}+\frac{q^4}{m^3}\right),
\qquad
 \lambda_q=\frac W{N_q}.
\tag{3.4}
\]

At the present \(H\), the error in (3.4) is \(o(1)\) and
\(\lambda_H=O(m)\). Hence

\[
 k_q\le\frac{N_q}{N}=\frac{\lambda_H}{\lambda_q}
 \le Cm e^{-q^2/m},
\tag{3.5}
\]

for an absolute \(C\) and all sufficiently large \(m\). The elementary
Gaussian sum bound now gives

\[
                         \sum_{q=1}^H k_q=O(m^{3/2}),
\tag{3.6}
\]

which proves (0.3).

If \(L=o(N/\sqrt m)\), then (3.2) and (3.6) give

\[
 L\sum_{q=1}^H k_q
 =o\!\left(\frac N{\sqrt m}m^{3/2}\right)
 =o(Nm)=o(W).
\tag{3.7}
\]

Together, (3.1), (3.3), and (3.7) show that every term after \(W\) in
(0.5) is \(o(W)\).

## 4. Literal-word ledger

Take a matching \(\mathcal M\) of size \(\nu=N-L\).
Each selected edge supplies one contiguous promotion path on its \(k_1\)
active middle states. The standard bridge-one compilation of a path on
\(s\) radius-\(H\) states has length \(s+2H\). Thus the selected paths
have total length

\[
                         \nu k_1+2H\nu.
\tag{4.1}
\]

The middle cells of different selected configurations are distinct by
the matching property. Append once each of the other \(W-\nu k_1\)
middle masks. The length becomes

\[
                         W+2H\nu\le W+2HN.
\tag{4.2}
\]

At either signed depth \(q\), the matching owns exactly \(\nu k_q\)
distinct targets. Therefore the number of holes on that shore is

\[
 N_q-\nu k_q
 =(N_q-Nk_q)+(N-\nu)k_q
 =r_q+Lk_q.
\tag{4.3}
\]

Append every such hole as a singleton word entry. Summing (4.3) over the
two signs and all \(q\) gives

\[
 W+2H\nu+2\sum_{q=1}^H(r_q+Lk_q),
\tag{4.4}
\]

which is bounded by (0.5). Every appended entry witnesses itself as a
length-one interval. Extra witnesses accidentally supplied by inactive
collars only help, so no disjointness assertion about collars is needed.
This proves the literal-word implication.

The construction in this section does not fill the holes by symmetric
chains and therefore does not, by itself, prove an exact SCD or the
literal fcpath statement. It proves the coefficient-one OR bound directly
once (0.4) and the audited exterior compiler are supplied.

## 5. The global-support audit

For a fixed middle target \(Y\), there are

\[
                         R_0=\binom mH
\tag{5.1}
\]

roots capable of owning it. A uniform rooted configuration at such a
root includes \(Y\) among its \(k_1\) active middle cells with probability

\[
                         p_1=\frac{k_1}{\binom MH}.
\tag{5.2}
\]

Its full-root mean load is

\[
 R_0p_1=\frac{Nk_1}{W}=1-o(1).
\tag{5.3}
\]

To cover the partial-matching formulation exactly, allow a null option at
every root. In a symmetrized matching of size \(\nu=N-L\), a root is
selected with probability

\[
                         \rho=\nu/N=1-o(m^{-1/2}),
\tag{5.4}
\]

and, conditional on selection, its rooted configuration marginal is
uniform. Thus the target-selection probability at one capable root is
\(p_*=\rho p_1\), and

\[
                         R_0p_*=\rho\,\frac{Nk_1}{W}=1-o(1).
\tag{5.5}
\]

The proof of the block-factor hole theorem uses only these one-root
means and independence between blocks, so it applies verbatim with
\(p_*\). Any such null-or-configuration law which factors over root
blocks of size \(b\) and is supported on \(o(W)\)-hole partial selections
must satisfy

\[
 b\ge(1-o(1))p_*^{-1}
 =(1-o(1))R_0.
\tag{5.6}
\]

Thus neither independent rooted configurations nor local
\(o(\binom mH)\)-root absorbers can prove (0.4). A matching itself creates
the required root-star-wide negative dependence through its shared
physical target vertices, so (5.6) is not a nonexistence theorem for
\(\mathcal C_{m,H}\).

## 6. Exact remaining boundary

Verified:

1. the common floor profile is nested and has exact shortfalls \(r_q<N\);
2. every configuration has exactly the physical cell count (0.3);
3. the labelled multihypergraph is edge-transitive;
4. the uniform \(1/\Delta\) point is a fractional matching of value \(N\);
5. averaging a maximum matching gives exactly the scale \(\nu/N\);
6. the quantitative word ledger (0.5) is correct; and
7. the leave hypothesis \(L=o(N/\sqrt m)\) makes every added term \(o(W)\).

Not proved:

1. the integral estimate (0.4);
2. any hereditary nibble or absorption theorem implying (0.4); or
3. an exact SCD completion of the unmatched configurations.

The surviving theorem is precisely the fibre-dense global matching
estimate (0.4). Edge transitivity closes the fractional and weighted
bookkeeping, but not the integrality gap.
