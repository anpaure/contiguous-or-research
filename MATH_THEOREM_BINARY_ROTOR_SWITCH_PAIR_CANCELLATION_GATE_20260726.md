# Binary rotors: every exact two-switch cancellation pair is forbidden

Date: 2026-07-26

## 0. Outcome

The global adjacent-swap toll forces \(\Theta(W)\) nonlinear \(A\)-switches
in every few-component rotor factor, so the scalar repair bound
\((H+1)a\) is unusable.  There is nevertheless a local involution which
cancels an \(A\)-switch at **every protected depth simultaneously**.

For an injective de Bruijn arc

\[
 e=(x_1,x_2,\ldots,x_{n-1})
\]

with missing coordinate \(x_n\), define

\[
 \iota(e)=(x_n,x_2,\ldots,x_{n-1}),
\tag{0.1}
\]

whose missing coordinate is \(x_1\).

Then \(\iota\) is an involution, and the complete nested Johnson-divergence
flag of an \(A\)-switch at \(\iota(e)\) is the negative of the flag at
\(e\).  However, \(e\) and \(\iota(e)\) have the same de Bruijn head.
They can never both occur in a Boolean cycle cover.  Therefore exact
two-switch cancellation is a **fractional null direction only**:

\[
 \boxed{
 z_e^A=z_{\iota(e)}^A\ \forall e
 \quad\Longrightarrow\quad z^A\equiv0
 \quad\text{for every integral rotor circulation}.}
\tag{0.2}
\]

Since few components require \(a=\Omega(W)\), this closes the canonical
same-head pairing.  Reordering the middle block yields \(m!-1\)
opposite-flag candidates with different heads, but their forced
\(A\)-successors have the same middle owner.  Owner transversality
therefore forbids those pairs as well.  Exact cancellation cannot occur
in two switches.

## 1. Exact cancellation

For \(1\le r\le m\), put

\[
 K_r(e)=\{x_{n-r+1},\ldots,x_{n-1}\}.
\tag{1.1}
\]

The \(A\)-switch divergence vector at rank \(r\) is

\[
 \partial_r(e)
 =
 \mathbf e_{K_r(e)\cup\{x_n\}}
 -
 \mathbf e_{K_r(e)\cup\{x_1\}}.
\tag{1.2}
\]

### Lemma 1.1

For every \(e\) and every \(r\le m\),

\[
 \boxed{\partial_r(\iota(e))=-\partial_r(e).}
\tag{1.3}
\]

#### Proof

The involution changes only the first and missing coordinates.  Hence
\(K_r(\iota(e))=K_r(e)\).  Its first coordinate is \(x_n\) and its
missing coordinate is \(x_1\).  Substitute these into (1.2). \(\square\)

### Theorem 1.2

Let \(z\) be an integral owner-transversal rotor circulation and assume

\[
 z^A_e=z^A_{\iota(e)}
 \qquad(e\in\mathcal E).
\tag{1.4}
\]

Then for every \(r\le m\),

\[
 R_r=L_r.
\tag{1.5}
\]

Consequently lower-prefix coverage through depth \(H\) implies the paired
upper-prefix coverage with exactly the same load profile.

#### Proof

The exact rotor divergence identity gives

\[
 R_r-L_r=\sum_e z^A_e\,\partial_r(e).
\]

Partition the selected \(A\)-arcs into the two-element \(\iota\)-orbits.
Lemma 1.1 cancels every pair. \(\square\)

### Theorem 1.3 (integral incompatibility)

In a Boolean rotor circulation, (1.4) forces \(z^A\equiv0\).

#### Proof

The arcs

\[
 e=(x_1,x_2,\ldots,x_{n-1}),\qquad
 \iota(e)=(x_n,x_2,\ldots,x_{n-1})
\]

have the same de Bruijn head \((x_2,\ldots,x_{n-1})\).  A Boolean cycle
cover has selected indegree at most one at every vertex.  Hence it cannot
select both arcs.  Equation (1.4) can therefore hold only with both
variables zero, for every \(\iota\)-orbit. \(\square\)

## 2. Shuffled reverse partners

The owner colours of an \(\iota\)-pair are

\[
 \kappa(e)=\{x_1,x_2,\ldots,x_m\},
\qquad
 \kappa(\iota(e))=\{x_n,x_2,\ldots,x_m\}.
\tag{2.1}
\]

They are adjacent in \(J(n,m)\).  Thus owner transversality alone does not
exclude the pair; de Bruijn indegree does.  This distinction is exactly
why the fractional cancellation does not round.

Write an arc more structurally as

\[
 e=(a,p_1,\ldots,p_m,u_1,\ldots,u_{m-1}),
\tag{2.2}
\]

with missing coordinate \(b\).  Here \(P=\{p_1,\ldots,p_m\}\) is forced
by \(a,b\) and the ordered suffix \(u=(u_1,\ldots,u_{m-1})\).
For any permutation \(P'=(p'_1,\ldots,p'_m)\) of the same set, put

\[
 e'=(b,p'_1,\ldots,p'_m,u_1,\ldots,u_{m-1}),
\tag{2.3}
\]

whose missing coordinate is \(a\).

### Theorem 2.1 (shuffled reverse cancellation)

For every \(r\le m\),

\[
 \partial_r(e')=-\partial_r(e).
\tag{2.4}
\]

If \(P'\ne P\), then \(e\) and \(e'\) have different de Bruijn heads and
are not excluded by local indegree one.

#### Proof

The nested suffix \(K_r\) depends only on the final ordered block \(u\),
which is identical in (2.2)--(2.3).  The first and missing coordinates
are exchanged, proving (2.4).  The head records the entire middle block
followed by \(u\), so distinct permutations \(P,P'\) give distinct heads.
\(\square\)

### Theorem 2.2 (successor-owner obstruction)

No owner-transversal integral rotor circulation can select both \(e\) and
\(e'\) from Theorem 2.1 as \(A\)-switches.

#### Proof

The selected \(A\)-successor arcs forced by flow are

\[
 (p_1,\ldots,p_m,u_1,\ldots,u_{m-1},a)
\]

and

\[
 (p'_1,\ldots,p'_m,u_1,\ldots,u_{m-1},b).
\]

The first \(m\) coordinates of both successors have underlying set
\(P\), since \(P'\) is merely a permutation of \(P\).  Hence the two
successor arcs have the same middle-owner colour, contradicting the owner
equation. \(\square\)

Combining Theorems 1.3 and 2.2, every two-switch pair whose complete
nested divergence flags are exact opposites is forbidden, either at
de Bruijn indegree or at the successor owner.

The uniform fractional rotor circulation with \(A\)-mass \(1/2\) contains
both orientations fractionally and cancels them.  Thus the obstruction is
purely integral.

## 3. Formal conditional theorem and its vacuity

Suppose that for

\[
 H=\sqrt m\,\omega(m),\qquad
 \omega(m)\to\infty,\qquad H=o(m),
\]

there is an integral rotor circulation satisfying:

1. one selected de Bruijn arc per middle owner and flow balance;
2. \(C=o(W/m)\) support cycles;
3. the selected \(A\)-arcs can be partitioned into shuffled reverse
   pairs of Theorem 2.1; and
4. aggregate lower-prefix holes \(o(W)\) through depth \(H\).

Then the rotor linearization would have length \(W+o(W)\) after singleton repair
and covers the paired central band.  The audited product-SCD exterior then
finishes the constant-one upper bound.

Indeed Theorem 2.1 would cancel the complete nested divergence of every
pair.  But Theorem 2.2 shows that no nonempty shuffled reverse pair is
integrally realizable.  The condition forces \(a=0\), leaving \(W/n\)
pure wreath components, so the few-cycle hypothesis fails.

## 4. Exact remaining question

Both canonical and shuffled exact reverse pairs are integrally
incompatible.  The surviving problem is to find a larger signed
cancellation circuit.  Such a circulation must:

1. respect de Bruijn indegree and outdegree one;
2. preserve one selected arc per owner;
3. contain \(\Theta(W)\) \(A\)-switches;
4. make the aggregate nested divergence \(o(W)\); and
5. retain lower-prefix coverage and \(o(W/m)\) components.

The smallest possible cancellation object has at least three distinct
switch flags and, after rotor-cycle parity, at least four switches in the
relevant component.  Finding a legal four-switch commutator with zero
nested divergence, or proving a positive cost for every such commutator,
is the next finite structural gate.
