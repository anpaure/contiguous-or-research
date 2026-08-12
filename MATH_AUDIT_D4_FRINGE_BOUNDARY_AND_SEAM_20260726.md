# The D4 fringe bank does not fragment the endpoint block

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

There are two distinct uses of the certified noncanonical D4 factor and
they must not be conflated.

1. A D4 factor substituted in a **fringe subtree strictly inside** a
   size-\(s\) child fixes both exported child endpoints. It is invisible
   to the serviced endpoint window. Consequently the dense fourteen-row
   fringe partition does not change any of the four Boolean cells of the
   no-interior-return block \(\mathcal B_s\).
2. The same D4 factor used in a **parent-aligned one-node lift** is a
   legal exact substitution and can change an endpoint of the serviced
   child window. At the first singleton parent its six-start signal is
   exactly repaid by the three attachment starts. At a further lift the
   sectors can acquire different fixed carriers, and the nonzero
   length-two and length-three profiles survive.

Thus the abstract bounded-block two-partition discrepancy lemma cannot be
applied to the standard dense fringe bank. Its row packets have size
fourteen, but their Boolean-cell action is zero. A new theorem would have
to partition almost all of \(\mathcal B_s\) into **parent-aligned**,
not fringe-internal, packets.

The audit also resolves an apparent seam contradiction. The exact gluing
interface is the pair of endpoint ports together with the complete
state/adjacent-union ledgers. The tokens \(a_1,b_4\) are internal edge
tokens and are not additional seam data.

## 1. The exact seam interface

For a rooted size-four row write

\[
 X_0=P,\ X_1,\ldots,X_4=J\setminus P,
 \qquad Y_i=X_i\cup X_{i+1}\quad(0\le i<4).             \tag{1.1}
\]

Let \(F\) and \(G\) be two D4-port factors such that

\[
\begin{aligned}
 &\{X_i^F(P):P\in\mathcal D_4,\ 0\le i\le4\}
  =\{X_i^G(P):P\in\mathcal D_4,\ 0\le i\le4\},\\
 &\{Y_i^F(P):P\in\mathcal D_4,\ 0\le i<4\}
  =\{Y_i^G(P):P\in\mathcal D_4,\ 0\le i<4\},
                                                               \tag{1.2}\\
 &X_0^F(P)=X_0^G(P)=P,\qquad
 X_4^F(P)=X_4^G(P)=J\setminus P .
\end{aligned}
\]

These are exactly the two certified \(X/Y\) ledgers and the port
condition.

### Theorem 1.1 (aligned gluing)

Under (1.2), replacing \(F\) by \(G\) in any recursively aligned common
Dyck context preserves exact middle ownership and every seam incidence.
In particular, changing

\[
 a_1=X_0\setminus X_1,\qquad b_4=X_4\setminus X_3       \tag{1.3}
\]

does not create a new gluing condition.

#### Proof

Inside the local slab, middle-state ownership is the \(X\)-ledger and
ownership of the alternating odd-graph states is, after the fixed
complement/adjoined-coordinate identification, the \(Y\)-ledger.
Equation (1.2) preserves both.

At the left external seam the neighbouring outside state meets the fixed
endpoint \(X_0=P\); at the right external seam it meets the fixed endpoint
\(X_4=J\setminus P\). Hence the two seam unions depend on \(P\) and
\(J\setminus P\), not on which internal neighbour \(X_1\) or \(X_3\) was
chosen. The quantities in (1.3) describe the first and last **internal**
edges.

The three generating one-node contexts \(x10,10x,1x0\) make this
functoriality explicit: adjoining fixed coordinates sends the old
\(X\)-ledger to an injected \(X\)-ledger and the old \(Y\)-ledger to an
injected or complemented \(Y\)-ledger, plus fixed collar states.
Iteration proves the assertion for every recursively aligned context.
\(\square\)

Disjoint aligned contexts therefore commute. Overlapping contexts may
have to be treated as one joint profile atom, but that is a dependence of
their **lower target profiles**, not a failure of exact gluing.

### Corollary 1.2 (status of the six-open-start signal)

Let \(u_F,u_G\) be the six open-parent singleton histograms and
\(v_F,v_G\) the three attachment histograms. For the certified factor,

\[
 u_G-u_F=d,\qquad v_G-v_F=-d.                          \tag{1.4}
\]

At the literal matched singleton parent all nine starts have one common
physical carrier, so the complete effect is zero. This is exact
repayment, not a seam obstruction.

After a further aligned lift, different starts can receive different
fixed exterior carriers. The complete lifted factors remain exact by
Theorem 1.1, while their aggregate local profiles satisfy

\[
 \Delta_2\ne0,\qquad\Delta_3\ne0,\qquad
 \frac12\|\Delta_2\|_1=19,\quad
 \frac12\|\Delta_3\|_1=22.                            \tag{1.5}
\]

Thus a legal higher-context signal is realizable without changing exterior
ownership. Its sign against cap overload still depends on the actual
residual background.

## 2. Strict-fringe erasure

Let \(W\) be the serviced size-\(s\) child window inside its
size-\((s+1)\) parent. A size-four fringe replacement is supported in a
local slab with complementary ports

\[
                              Q,\qquad J_4\setminus Q.  \tag{2.1}
\]

### Lemma 2.1 (no endpoint bit from a strict fringe)

If the local slab lies strictly inside \(W\), then replacing its canonical
factor by \(G\) does not change either endpoint state of \(W\), and does
not change the target of \(W\).

#### Proof

Port transversality fixes the two local boundary states in (2.1).
Because the complete slab lies inside \(W\), the local part of the
intersection defining the target of \(W\) is contained in

\[
                         Q\cap(J_4\setminus Q)=\varnothing.       \tag{2.2}
\]

All local open states are therefore erased. The two endpoints of \(W\)
belong to its parent interface and are outside the strict fringe slab, so
they are fixed as well. \(\square\)

This applies to every shape installed at the selected fringe root. The
fact that \(G\) has a nonzero first-insertion statistic relative to its
*own* local path does not turn that statistic into an endpoint bit of the
larger serviced window.

## 3. Exact census on the no-interior-return block

Recall

\[
\begin{aligned}
 \mathcal B_s={}&
 \{1u0:u\in\mathcal D_s\}
 \mathbin{\dot\cup}
 \{10\,1v0:v\in\mathcal D_{s-1}\}\\
 &\mathbin{\dot\cup}
 \{1v0\,10:v\in\mathcal D_{s-1}\}
 \mathbin{\dot\cup}
 \{10\,1w0\,10:w\in\mathcal D_{s-2}\}.                \tag{3.1}
\end{aligned}
\]

Its four endpoint-cell populations are

\[
                 (C_s,C_{s-1},C_{s-1},C_{s-2}),       \tag{3.2}
\]

with total \(M_s=C_s+2C_{s-1}+C_{s-2}\).

Let \(a_t\) be the number of size-\(t\) binary trees with no size-four
fringe subtree. The stable first-fringe rule partitions the nonavoiding
trees into

\[
                         P_t=\frac{C_t-a_t}{14}        \tag{3.3}
\]

fourteen-row packets, and \(a_t/C_t=o(1)\) exponentially. Applied to the
four central fillings in (3.1), this gives exactly

\[
                  P_s+2P_{s-1}+P_{s-2}
 =\frac{M_s-(a_s+2a_{s-1}+a_{s-2})}{14}               \tag{3.4}
\]

pairwise row-disjoint fringe packets. They cover \(M_s-o(M_s)\)
occurrences.

### Theorem 3.1 (dense but endpoint-inert)

For \(s\ge7\), every packet counted in (3.4) is strict-interior with
respect to the serviced endpoint window. Hence its two legal states have
the same Boolean-cell incidence. The subset of \(\mathcal B_s\) carrying
a boundary-active state from this fringe bank is empty.

#### Proof

The central filling sizes in (3.1) are \(s,s-1,s-1,s-2\), all strictly
larger than four when \(s\ge7\). A size-four fringe subtree is therefore
a proper descendant of the corresponding central filling. Its aligned
factor slab lies strictly between the exported endpoints of the serviced
child. Lemma 2.1 applies to every packet state. \(\square\)

There are only finite small-scale exceptions. A size-four fringe can be
the whole central filling in the first family only at \(s=4\), in either
one-leaf family only at \(s=5\), and in the two-leaf family only at
\(s=6\). These are precisely one-node parent-aligned uses of the local
factor, not an asymptotic fringe bank. Their packet size is fourteen.

Thus the exact asymptotic comparison is:

\[
\begin{array}{c|c|c}
 \text{object}&\text{row packet size}&
       \text{endpoint-active occurrences}\\ \hline
 \text{standard size-four fringe packet}&14&0\\
 \text{certified one-node parent lift}&14&14
       \text{ on its displayed local block}.
\end{array}                                             \tag{3.5}
\]

The second line is only a local packet. No theorem currently partitions
all but \(o(M_s)\) of \(\mathcal B_s\) into such parent-aligned blocks.

## 4. Failure of the abstract two-partition input

The bounded-contingency lemma assumes that a left block sign and a right
block sign really are the two Boolean target bits of every nonexceptional
occurrence. The partitions must cover all but \(R\) occurrences with
blocks of size at most \(B\).

For the fringe bank (3.4), changing a block sign changes the internal
factor but neither endpoint bit. Hence these packets do not define either
of the two required partitions. Treating unsupported occurrences as
exceptions gives

\[
                              B=14,\qquad R=M_s,        \tag{4.1}
\]

not \(R=a_s+2a_{s-1}+a_{s-2}=o(M_s)\). The abstract bound then becomes

\[
 \max n_{\epsilon,\eta}
 \le\frac{M_s}{4}+\frac{5\cdot14+3M_s}{4}
 =M_s+\frac{35}{2},                                   \tag{4.2}
\]

which is vacuous.

Consequently the finite D4 factor does not yet fragment the canonical
\(\mathcal B_s\) ownership component in the sense needed by Boolean-cell
balancing. The precise missing construction is:

> Partition all but \(o(M_s)\) endpoint occurrences into bounded
> **parent-aligned** packets, independently at the left and right
> boundary, prove that their complete two-boundary choices are jointly
> legal, and retain separated carrier profiles.

Only after that theorem would the constant-error two-partition discrepancy
lemma apply with \(B=14\) and \(R=o(M_s)\).

## 5. The exact successor: a root-aligned skeleton packet

There is one natural construction which is not covered by the no-go.
Choose a four-node **operadic skeleton** at the serviced parent boundary,
attach five fixed spectator subtrees in its input slots, and vary the
four-node skeleton over all fourteen members of \(\mathcal D_4\).
Such a packet is root-aligned and can touch an exported endpoint even when
the total tree has size \(s\gg4\). It is not a size-four fringe subtree.

The unresolved finite/combinatorial question is whether this prescription
gives a stable partition of almost all size-\(s\) trees into fourteen-row
classes. Two issues must be checked simultaneously:

1. changing the skeleton must leave the ordered spectator tuple in the
   same five input slots, rather than reorder or absorb spectator
   material; and
2. after the spectators are substituted, the fourteen rows must retain
   one common port and \(X/Y\) interface so that the local factor
   replacement is exact.

If both hold at the left and right boundary, these skeleton classes are
precisely bounded parent-aligned blocks with \(B=14\), and the
two-partition discrepancy theorem becomes applicable. If either fails,
the dense fringe census (3.4) supplies no substitute.

For one fixed ordered spectator tuple
\((A_0,\ldots,A_4)\), the fourteen bracketings are genuinely distinct and
the spectators remain in the same inorder slots: binary trees form the
free nonsymmetric binary operad, so changing the skeleton neither reorders
nor algebraically absorbs an input. The difficulty begins when the
spectators are unmarked. One large tree can admit several different
four-node top-skeleton decompositions, so the fourteen-element fibres
overlap.

The overlap census is exact. If \(C(z)=\sum C_tz^t\), the number of
ordered spectator tuples of total size \(s-4\) is

\[
 E_s=[z^{s-4}]C(z)^5
 =\frac5{2s-3}\binom{2s-3}{s-4}.                      \tag{5.1}
\]

Thus the fourteen-uniform skeleton hypergraph on \(\mathcal D_s\) has

\[
 \frac{14E_s}{C_s}\longrightarrow\frac{35}{8}          \tag{5.2}
\]

as its average vertex degree. Every vertex degree is bounded by fourteen:
for each of the fourteen four-node skeleton shapes, its rooted
ancestor-closed embedding in a fixed tree is unique if it exists.
Consequently this is a bounded-degree exact-matching problem, not a
high-degree nibble. Equation (5.2) neither supplies nor rules out a
matching covering \(1-o(1)\) of \(\mathcal D_s\).

There is a second, independent gate. The current context theorem lifts a
factor through one common one-hole context. A five-input skeleton
substitution is row-dependent when the skeleton changes; equality of the
small \(X/Y\) ledgers does not by itself prove equality after inserting
five nontrivial spectator factors. One needs a genuine five-input
operadic \(X/Y\)-composition theorem. Therefore even a near-perfect
matching in the skeleton hypergraph would not, by itself, certify the
required expanded port factors.
