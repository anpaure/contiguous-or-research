# Connector audit for the truncated static cube

## 0. Verdict

The flush-and-reload routing theorem in
`TRUNCATED_ROTOR_STATIC_CUBE_COMPILATION_20260725.md` is correct, as are its
path-length and static marked-cell counts.  The connector incidences do not,
however, telescope inside one routed transition.

Let two source collars differ by swapping adjacent labels \(u,v\) in
positions \(r,r+1\), with \(1\le r\le Q\).  Couple the two routes using the
same buffers and the correspondingly swapped target collars.  If
\(\Delta_h\) denotes the aggregate incidence difference of the entire
\(4Q+1\)-update route at prefix length \(h\), then
\[
\boxed{
\sum_{h=r+1}^{2Q-1}\|\Delta_h\|_2^2
\ge4(2Q-r-1).
}
\tag{0.1}
\]
Every term in this sum comes from connector states, not from the marked
rank-isolated rectangle.  Since the cube row pairs lie in the lower half of
the collar, \(r\le Q\), and the lower bound is \(\Omega(Q)\).

In particular the connector contribution includes a nonzero middle-owner
difference whenever \(r<Q\).  Thus the marked owner invariance does not
extend to the physical path.

The connector trace for a bit exchanging labels \(u,v\) lies in the direct
sum of transposition-edge spaces
\[
\operatorname{im}(I-(uv))
\]
over the hard ranks.  At rank \(s\), this space has dimension
\(\binom{M-2}{s-1}\), so it is not a bounded-dimensional boundary error.

A whole row-sign update has an exact equivariance description: with
equivariant buffer and padding choices, toggling row pair \(i\) sends the
entire compiled path to its image under the coordinate transposition
\(\alpha_i\).  Hence its full physical difference is
\[
\boxed{
\widetilde I(E')-\widetilde I(E)
=(\alpha_i-I)\widetilde I(E).
}
\tag{0.2}
\]
This is not automatically small and is not a low-dimensional correction.

Exact cancellation is possible by pairing a route with the same route in
the opposite transposition orientation, but that pairing cancels the marked
rectangle contribution as well.  No pairing which cancels all connector
terms while retaining the marked drift is supplied by the current
construction.

Therefore the static cube has been compiled literally, but the marked
\(O(1)\)-step kernel has not been converted into a full physical-load
kernel.  A successful successor must prove a cross-route telescoping
identity using the complete column chronology, or a multi-carrier pairing
whose connector map has a kernel not shared by the marked rectangle map.

## 1. Prefix notation

Put
\[
n=2Q,
\qquad a_0=m-Q.
\]
For a quotient rotor state
\[
\omega=(A;z_1,\ldots,z_n;B),
\]
write
\[
F_h(\omega)=A\cup\{z_1,\ldots,z_h\},
\qquad0\le h\le n.
\tag{1.1}
\]
This is the flag of rank \(a_0+h\).  In particular \(h=Q\) is the middle
owner.

The flush-and-reload route chooses distinct buffers
\[
x_1,\ldots,x_n,a\in A
\]
and a tail element \(b\in B\).  Its first \(n+1\) updates have core choices
\[
x_1,\ldots,x_n,a
\]
and tail choices
\[
b,z_n,z_{n-1},\ldots,z_1.
\]
The final \(n\) updates remove the target collar labels in reverse order
and return \(x_1,\ldots,x_n\) from the tail.

## 2. Exact effect of a source-collar transposition

Let
\[
z_r=u,qquad z_{r+1}=v,
\]
and compare the flush routes from the collars
\[
(z_1,\ldots,u,v,\ldots,z_n)
\quad\hbox{and}\quad
(z_1,\ldots,v,u,\ldots,z_n).
\]
All unordered blocks and all buffer choices are the same.

After \(s\le n\) flush updates, the collar is
\[
(x_s,x_{s-1},\ldots,x_1,z_1,\ldots,z_{n-s}).
\tag{2.1}
\]
For \(0\le s\le n-r\), both routes have the same core.  Their flag columns
differ at exactly one prefix length,
\[
h=s+r.
\tag{2.2}
\]
At that prefix the difference is
\[
e_{K_h+u}-e_{K_h+v}
\tag{2.3}
\]
for a common base \(K_h\) containing neither \(u\) nor \(v\).

At the next state
\[
s_*=n-r+1,
\]
the label which dropped first has entered the core, while the other has
dropped into the tail.  Hence **every** prefix length differs, with the
opposite orientation:
\[
e_{J_h+v}-e_{J_h+u},
\qquad0\le h\le n.
\tag{2.4}
\]
After the following update both labels have entered the core and the source
transposition is no longer visible.

The bases in (2.3)--(2.4) can be written explicitly.  For
\(h=r+s\), the boundary base is
\[
K_h=
\begin{cases}
A+\{z_1,\ldots,z_{r-1}\},&s=0,\\
A+b+\{z_1,\ldots,z_{r-1}\}
 +\{z_{n-s+2},\ldots,z_n\},&s\ge1,
\end{cases}
\tag{2.5}
\]
where the buffer deletions cancel against the buffer prefix in (2.1).
At the special state,
\[
J_h=A-\{x_1,\ldots,x_{s_*}\}+b
 +\{z_{r+2},\ldots,z_n\}
 +\operatorname{pref}_h(x_{s_*},\ldots,x_1,z_1,\ldots,z_{r-1}).
\tag{2.6}
\]

At \(h=n\), one has \(K_n=J_n\), so the two opposite terms cancel.
For every
\[
r+1\le h\le n-1,
\]
the bases are different.  Indeed \(z_{r+2}\in J_h\), whereas
\(z_{r+2}\notin K_h\); the latter enters the suffix in (2.5) only at
\(h=n\).  Since neither base contains \(u,v\), the four masks
\[
K_h+u,\quad K_h+v,\quad J_h+u,\quad J_h+v
\]
are distinct.  Therefore the source-flush difference at rank \(a_0+h\)
has squared norm exactly four throughout this range.

## 3. Exact target-reload support

Now compare two target collar orders which differ by the same adjacent
transposition in positions \(r,r+1\).  At the beginning of the reload both
labels lie in the core.  The label in target position \(r+1\) is removed
first and inserted at collar position one.  At that state only prefix
length \(h=0\) differs: every positive prefix contains both labels.  The
next insertion moves the transposition boundary to prefix length one, and
each subsequent reload step moves it one position to the right.

Consequently the complete target-order contribution is supported only at
\[
h=0,1,\ldots,r.
\tag{3.1}
\]
It has no contribution at any \(h>r\).  Combining this with Section 2 proves
(0.1): at every \(r+1\le h\le n-1\), the two noncancelling source-flush
pairs are the entire route difference.

The conclusion is already aggregate in time.  It does not merely count
time-resolved discrepancies.

## 4. Owner and flag consequences

In the rectangular cube,
\[
q_{ij}=4t+2i-2j+1,
\]
and the active adjacent pair occurs at collar boundary
\[
r_{ij}=Q-q_{ij}
\tag{4.1}
\]
up to the harmless choice of whether positions are indexed from zero or
one.  Since \(q_{ij}\ge1\), one has \(r_{ij}<Q\).  Therefore the range in
(0.1) includes \(h=Q\), the middle owner.  At that rank the connector
difference has two disjoint transposition pairs and squared norm four.

Thus a single routed marked bit is not an owner-preserving physical
exchange.  Its static marked endpoints have owner multiset independent of
the bit, but the flush connector creates a real owner difference.

At all ranks \(h=r+1,\ldots,n-1\), the difference lies in
\[
\operatorname{im}(I-(uv))
\subseteq\mathbb R^{\binom U{a_0+h}}.
\tag{4.2}
\]
The transposition orbits of size two are indexed by the
\((a_0+h-1)\)-subsets of \(U-\{u,v\}\).  Hence
\[
\dim\operatorname{im}(I-(uv))
=\binom{M-2}{a_0+h-1}.
\tag{4.3}
\]
The connector is therefore structured, but not low-dimensional on the
Boolean scale.

## 5. Whole row and column updates

Fix a row pair \(\alpha_i=(uv)\) and toggle the complete row
\[
E_{ij}\longmapsto1-E_{ij}
\qquad(0\le j<t).
\]
Every marked state is sent to its coordinate-transposed state:
\[
A_j(E')=\alpha_iA_j(E),
\qquad
B_j(E')=\alpha_iB_j(E).
\tag{5.1}
\]
The two cyclic steps between ports are equivariant as well.  If buffer
choices, flush routes, and final padding are selected equivariantly, the
whole physical path obeys
\[
P(E')=\alpha_iP(E).
\tag{5.2}
\]
Taking complete rank incidences gives (0.2).

Thus a row update does not turn the connectors into a scalar boundary term.
It applies a full coordinate transposition to their aggregate load.  At
rank \(s\), its possible differences fill the space (4.3).

A column update toggles several disjoint row pairs at one port.  Its
connector difference is the sum of the corresponding transposition-edge
traces.  The static marked rectangles are support-disjoint, but the
connector bases (2.5)--(2.6) are not the static rectangle bases, so static
support-disjointness does not prove orthogonality or cancellation of the
connector terms.

## 6. Pairing possibilities and their limitation

Let \(R^+\) and \(R^-\) be the two coupled routes in Sections 2--3.  Reversing
which route is called positive negates the complete difference
\[
I(R^+)-I(R^-),
\]
including both its connector part and its marked endpoint part.  Likewise,
pairing a carrier route with its image under \((uv)\) gives exact
antisymmetric cancellation, but it also cancels the desired marked
rectangle.

Therefore the obvious equivariant route pairing has zero net correction.
To retain the marked rectangle while canceling connectors, one needs two
different routing templates \(R_1,R_2\) satisfying
\[
C(R_1)+C(R_2)=0,
\qquad
J(R_1)+J(R_2)\ne0,
\tag{6.1}
\]
where \(C\) and \(J\) are respectively the connector and marked-incidence
maps.  The current flush-and-reload family supplies no such identity.

Equation (0.1) also shows that any candidate identity must cancel
\(\Omega(Q)\) explicitly different rank-mask pairs per bit.  This is much
stronger than canceling one endpoint defect.

## 7. Variance calibration

The statement
\[
\max_S\operatorname{Var}(J(E)_S)\le1/4
\]
for the designated marked projection is correct.  It is not the AD22 trace
variance bound.  Fairly resampling all \(pt=\Theta(M)\) marked bits has
\[
\operatorname{tr}\operatorname{Cov}(J(E))=\Theta(M),
\]
the independent-packet scale.  Resampling one marked bit has designated
squared increment four, but the full routed increment has squared norm at
least \(\Omega(Q)\) by (0.1).

Thus the compiler does not currently yield either of the two desired
objects:

1. a full physical one-bit exchange of \(O(1)\) squared norm; or
2. a coefficient-scale fair resampling with total variance \(o(M)\).

The literal bit capacity theorem remains valuable, but its covariance claim
must remain explicitly restricted to the marked projection.

## 8. Exact remaining question

The only plausible escape visible from the connector formula is a global
coboundary construction.  One must choose the buffers and route ordering so
that successive source-flush traces cancel across ports, while the static
endpoint rectangles add.  Formally, for each row pair \(i\), seek routing
templates with
\[
\sum_j C_{ij}=O(1)
\quad\text{in squared norm},
\qquad
\sum_j J_{ij}=\sum_j\rho_{ij}.
\tag{8.1}
\]
No such identity follows from the one-route flush/reload theorem.  The
explicit bases (2.5)--(2.6) reduce the problem to exact equality of Boolean
masks, so it can now be attacked as a concrete route-pairing problem rather
than an unspecified variance estimate.

## 9. Equal adjacent-port pairing: exact cap-drift obstruction

The proposed constraint

\[
 E_{i,2s}=E_{i,2s+1}
\]

retains the marked drift

\[
 \rho_{i,2s}+\rho_{i,2s+1},
\]

but it does not telescope the complete connector incidence to \(O(1)\)
seam ranks.  The detailed proof is in
MATH_ATTACK_RECTANGULAR_COMPILED_CUBE_VERTICAL_BRAID_20260725.md,
Section 7.

The exact counterterm is the cyclic cap drift.  Two cyclic steps move the
active collar boundary from \(r\) to \(r+2\), but they also replace the two
far-collar labels \(z_{2Q-1},z_{2Q}\) by two new right-boundary labels in
the extended cap \(A+\{z_1,\ldots,z_{2Q}\}+\{b\}\).  At every prefix length

\[
 r+3\le h\le2Q-1,
\]

the two oppositely oriented source traces consequently have disjoint mask
supports and combined squared norm eight.  Target reloads live only at
prefix lengths at most \(r+2\) and cannot cancel this residue.

After all pieces incident with a two-port block are included, the two
same-phase middle source traces can be coupled to cancel.  What remains is
a phase-four cap derivative, still of squared norm eight throughout

\[
 r+5\le h\le2Q-1.
\]

Thus equal adjacent ports preserve the two marked rectangles but leave
\(\Omega(Q)\) connector ranks.  Exact cancellation would require explicit
transport of the fallen far-collar labels or a nonlocal multi-carrier
identity.
