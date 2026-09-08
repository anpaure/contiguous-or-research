# Annular packets: exact common-interval energy, shared-floor reduction, and the pair-gadget gate

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad r=m-q_0,\qquad
 W=\binom{2m}{m},\qquad
 q_0=a\sqrt m+O(1),\qquad H=b\sqrt m+O(1),
\tag{0.1}
\]

where \(0<a<b\) are fixed, and put

\[
 J=H-q_0=(b-a)\sqrt m+O(1),
 \qquad N_d=\binom n{r-d}\quad(0\le d\le J).
\tag{0.2}
\]

Let \(\mathcal M\) be a matching of ordinary cyclic \(r\)-interval
packets. Write

\[
 s=|\mathcal M|,\qquad G=ns=N_0-L,
\tag{0.3}
\]

so \(L\) is the rank-\(r\) leave. At depth \(d\), let
\(\mu_d(R)\) be the number of selected packets in which \(R\) is a
cyclic \((r-d)\)-interval, and define the repeat excess above the forced
layer-size floor by

\[
 \widetilde E_d
 =\sum_R(\mu_d(R)-1)_+-(G-N_d)_+.
\tag{0.4}
\]

The exact conclusions are as follows.

1. For two packets \(e,f\), let

   \[
    C_d(e,f)
    =|\mathcal I_{r-d}(e)\cap\mathcal I_{r-d}(f)|.
   \tag{0.5}
   \]

   Then the complete depth-\(d\) pair energy is exactly

   \[
    \boxed{
    P_d:=\sum_R\binom{\mu_d(R)}2
        =\sum_{\{e,f\}\subseteq\mathcal M}C_d(e,f).}
   \tag{0.6}
   \]

   The entrance matching condition is precisely

   \[
                         C_0(e,f)=0
                         \quad(e\ne f\in\mathcal M).
   \tag{0.7}
   \]

2. Write \(G=u_dN_d+v_d\), \(0\le v_d<N_d\), and define

   \[
    P_d^{\min}=N_d\binom{u_d}{2}+u_dv_d,
    \qquad \Phi_d=P_d-P_d^{\min}\ge0,
   \tag{0.8}
   \]

   \[
    \kappa_d=
    \begin{cases}
      1,&u_d=0,\\[1mm]
      \binom{u_d+1}{2},&u_d\ge1.
    \end{cases}
   \tag{0.9}
   \]

   Then

   \[
    \boxed{
    \widetilde E_d\le\frac{\Phi_d}{\kappa_d},
    \qquad
    \sum_{d=0}^{J}\widetilde E_d
    \le\sum_{d=0}^{J}\frac{\Phi_d}{\kappa_d}.}
   \tag{0.10}
   \]

   Thus the synchronized annulus gate is an \(o(W)\) error theorem for
   the common-interval pair energy around its exact
   \(\Theta(W\sqrt m)\) floor. Raw pair energy cannot be used.

3. Complete-catalogue incidence counting gives, for every fixed packet
   \(e\),

   \[
    \boxed{
    \sum_{f\ne e}C_d(e,f)
      =n(\mathscr D_d-1),
    \qquad
    \mathscr D_d=\frac{(r-d)!(n-r+d)!}{2}.}
   \tag{0.11}
   \]

   Globally,

   \[
    \boxed{
    \sum_{\{e,f\}}C_d(e,f)
      =N_d\binom{\mathscr D_d}{2}.}
   \tag{0.12}
   \]

   These identities determine the complete-orbit average, but they do
   not bound the energy of a selected entrance matching: deleting all
   pairs with \(C_0>0\) has no sign on their shorter-interval profile.
   In fact the exact conditional calculation (3.7) shows that, given one
   common depth-\(d\) interval, two uniform packets are entrance-compatible
   with probability \(1-O(m^{-1})\). Consequently the compatible-pair
   catalogue retains \(1-O(m^{-1})\) of the full lower-interval incidence.

4. The exact extension cap is

   \[
    \boxed{
    (d+1)\mu_d(R)
       \le\binom{n-r+d}{d}.}
   \tag{0.13}
   \]

   At \(d=1\), each occurrence of an \((r-1)\)-target \(R\) is encoded
   by its unordered pair of immediate exterior neighbours, and these
   endpoint pairs form a matching in the \((n-r+1)\)-set outside \(R\).
   Hence

   \[
    \mu_1(R)\le\left\lfloor\frac{n-r+1}{2}\right\rfloor.
   \tag{0.14}
   \]

   The cap is of order \(m\), while the mean load is \(1+O(m^{-1/2})\).
   It therefore permits, rather than excludes, linear repeat excess.

5. On every parameter subsequence on which \(r\) is odd, the domino-twin
   pair \(P,P^\tau\) is a literal entrance matching with the exact common-
   interval profile

   \[
    \boxed{
    C_d(P,P^\tau)=
    \begin{cases}
      n/2,&d\text{ odd},\\
      0,&d\text{ even}.
    \end{cases}}
   \tag{0.15}
   \]

   Consequently this two-packet matching has

   \[
    \boxed{
    \sum_{d=1}^{J}\widetilde E_d
      =\frac n2\left\lceil\frac J2\right\rceil
      =\Theta_{a,b}(m^{3/2}).}
   \tag{0.16}
   \]

   An all-parity four-block pair also has \(C_d\ge2d\) and aggregate
   excess \(\Theta(m)\).

6. Let the domino-twin superpacket have entrance edge
   \(E_r(P)\mathbin{\dot\cup}E_r(P^\tau)\). If this \(2n\)-uniform,
   vertex-transitive catalogue has a matching with leave
   \(O(N_0/\sqrt m)\), its constituent ordinary packets form a critical-
   leave matching satisfying

   \[
    \widetilde E_1=\Omega(W),
    \qquad
    \sum_{d=1}^{J}\widetilde E_d=\Omega(W\sqrt m).
   \tag{0.17}
   \]

   Thus a near-factor of this exact paired catalogue would refute the
   requested implication decisively. The catalogue has an exact uniform
   fractional perfect matching, but its integral critical-leave near-
   factor is not proved here. Conversely, proving

   \[
                         \sum_d\Phi_d/\kappa_d=o(W)
   \tag{0.18}
   \]

   for every critical-leave matching requires a genuinely global
   packet-pair dispersion theorem; it does not follow from common-
   interval pair profiles, complete-orbit incidence counts, or the
   extension caps.

Hence the requested automatic implication

\[
 L=O(N_0/\sqrt m)
 \quad\Longrightarrow\quad
 \sum_d\widetilde E_d=o(W)
\tag{0.19}
\]

is not proved by the proposed local data: the displayed identities and
caps leave the domino-superpacket integral question undecided. The
exact floor-correct *sufficient certificate* is (0.18), while an exact
negative integral gate is the domino-superpacket near-factor. The local literal
counterexample (0.16) shows why a hereditary path-colour hypothesis is
substantive rather than a hidden consequence of entrance matching.

## 1. Packet notation and the exact pair identity

A packet is an unoriented cyclic order \(e\) of \([n]\). For
\(1\le\ell<n\), let

\[
 \mathcal I_\ell(e)
 =\{I_e(j,\ell):j\in\mathbb Z_n\}
\tag{1.1}
\]

be its \(n\) distinct cyclic \(\ell\)-intervals. At depth \(d\), put

\[
                         \ell_d=r-d.
\tag{1.2}
\]

For a selected family \(\mathcal M\),

\[
 \mu_d(R)=|\{e\in\mathcal M:R\in\mathcal I_{\ell_d}(e)\}|.
\tag{1.3}
\]

Every packet contributes \(n\) occurrences, so

\[
                         \sum_R\mu_d(R)=G
\tag{1.4}
\]

at every depth.

### Theorem 1.1 (common-interval pair identity)

For every selected packet family,

\[
 \boxed{
 \sum_R\binom{\mu_d(R)}2
 =\sum_{\{e,f\}\subseteq\mathcal M}
   |\mathcal I_{\ell_d}(e)\cap\mathcal I_{\ell_d}(f)|.}
\tag{1.5}
\]

#### Proof

Both sides count triples \((R,\{e,f\})\) in which \(e\ne f\) are
selected packets and \(R\) is a cyclic \(\ell_d\)-interval in both.
\(\square\)

At \(d=0\), the selected family is an entrance matching precisely when
every rank-\(r\) target has load at most one. By (1.5), this is equivalent
to

\[
                         C_0(e,f)=0
                         \quad(e\ne f\in\mathcal M).
\tag{1.6}
\]

There is no term involving three packets in (1.5). Higher target loads
are already counted with the correct multiplicity \(\binom{\mu}{2}\).

## 2. Floor correction and the synchronized sufficient bound

We record the elementary integer calculation because subtracting the
forced floor is essential here.

### Lemma 2.1 (floor pair energy)

Let \(z_1,\ldots,z_N\) be nonnegative integers with
\(\sum_i z_i=G=uN+v\), where \(0\le v<N\). Then

\[
 \sum_i\binom{z_i}{2}
 -\left(N\binom u2+uv\right)
 =\frac12\sum_i(z_i-u)(z_i-u-1)\ge0.
\tag{2.1}
\]

If \(u\ge1\) and \(h=|\{i:z_i=0\}|\), then

\[
                         h\binom{u+1}{2}
 \le
 \sum_i\binom{z_i}{2}
 -\left(N\binom u2+uv\right).
\tag{2.2}
\]

If \(u=0\), then

\[
                         \sum_i(z_i-1)_+
 \le\sum_i\binom{z_i}{2}.
\tag{2.3}
\]

#### Proof

The identity

\[
 \binom z2-uz+\binom{u+1}{2}
 =\frac12(z-u)(z-u-1)
\tag{2.4}
\]

and \(G=uN+v\) prove (2.1). A zero cell contributes
\(\binom{u+1}{2}\) to the right side, proving (2.2). For \(u=0\), use
\((z-1)_+\le\binom z2\). \(\square\)

### Theorem 2.2 (exact common-interval sufficient criterion)

At depth \(d\), define \(u_d,v_d,P_d^{\min},\Phi_d,\kappa_d\) by
(0.8)--(0.9). Then

\[
                         \widetilde E_d
 \le\frac{\Phi_d}{\kappa_d}.
\tag{2.5}
\]

Consequently (0.18) implies

\[
                         \sum_{d=0}^{J}\widetilde E_d=o(W).
\tag{2.6}
\]

#### Proof

If \(u_d=0\), then \(G<N_d\), the forced repeat floor is zero, and
Lemma 2.1 gives

\[
 \widetilde E_d
 =\sum_R(\mu_d(R)-1)_+
 \le P_d=\Phi_d.
\tag{2.7}
\]

If \(u_d\ge1\), then \(G\ge N_d\). The exact occurrence identity gives

\[
 \widetilde E_d
 =\sum_R(\mu_d(R)-1)_+-(G-N_d)
 =|\{R:\mu_d(R)=0\}|.
\tag{2.8}
\]

Apply (2.2). This proves (2.5), and summation proves (2.6).
\(\square\)

When \(L=O(N_0/\sqrt m)\), the separate scalar-floor sum is \(o(W)\)
by the shared-leave calculation. Therefore (2.6), rather than raw
pair-smallness, is the exact pair-energy route to the annulus theorem.

## 3. Complete-catalogue common-interval incidence

Let \(\mathscr P\) be the simple catalogue of unoriented cyclic orders.
A fixed \(\ell\)-target belongs to exactly

\[
                         \mathscr D_\ell
 =\frac{\ell!(n-\ell)!}{2}
\tag{3.1}
\]

packets.

### Theorem 3.1 (global row and total pair profiles)

For every fixed packet \(e\),

\[
 \boxed{
 \sum_{f\in\mathscr P\setminus\{e\}}
 |\mathcal I_\ell(e)\cap\mathcal I_\ell(f)|
 =n(\mathscr D_\ell-1).}
\tag{3.2}
\]

Also

\[
 \boxed{
 \sum_{\{e,f\}\subseteq\mathscr P}
 |\mathcal I_\ell(e)\cap\mathcal I_\ell(f)|
 =\binom n\ell\binom{\mathscr D_\ell}{2}.}
\tag{3.3}
\]

#### Proof

The packet \(e\) contains \(n\) distinct \(\ell\)-targets. Each belongs
to \(\mathscr D_\ell-1\) other packets. Summing over its targets proves
(3.2), with a packet sharing several targets counted with that
multiplicity. For (3.3), fix the common target first and choose two of
its \(\mathscr D_\ell\) packets. \(\square\)

Equations (3.2)--(3.3) are all that transitivity and global incidence
counting provide. The entrance matching removes from consideration every
selected pair with a common \(r\)-target. It does not sample the
remaining pairs uniformly, and no inequality compares

\[
 C_d(e,f)\quad\text{with}\quad C_0(e,f)
\tag{3.4}
\]

in the needed direction. Section 5 gives a literal failure of such a
comparison.

## 3A. Exact entrance-overlap profile conditional on a lower collision

The preceding total incidence can be sharpened in exactly the direction
relevant to entrance compatibility. Fix

\[
 \ell=r-d,\qquad M=n-\ell=n-r+d,
 \qquad c=M-r=n-2r+d,
\tag{3.4a}
\]

and fix an \(\ell\)-target \(R\). Choose a packet \(P\) uniformly
conditional on \(R\in\mathcal I_\ell(P)\). For an entrance target
\(A\in\binom{[n]}r\), direct contraction of the interval atoms gives

\[
 \Pr(A\in\mathcal I_r(P)\mid R\in\mathcal I_\ell(P))
 =
 \begin{cases}
 \displaystyle {d+1\over\binom Md},&R\subset A,\\[3mm]
 \displaystyle {2\over\binom\ell k\binom M{d+k}},
       &|R\setminus A|=k,\ 1\le k\le\ell-1,\\[3mm]
 \displaystyle {c+1\over\binom Mr},&R\cap A=\varnothing.
 \end{cases}
\tag{3.5}
\]

Indeed, in the three cases the corresponding directed packet counts,
divided by \(\ell!M!\), are respectively

\[
 {\ell!(d+1)!(n-r)!\over\ell!M!},\qquad
 {2(d+k)!(\ell-k)!k!(M-d-k)!\over\ell!M!},\qquad
 {r!(c+1)!\over M!}.
\tag{3.6}
\]

The same ratios hold for unoriented packets. Hence, for independent
\(P,P'\) conditioned to contain \(R\), their expected number of common
entrance targets is exactly

\[
 \boxed{
 \Xi_d
 ={(d+1)^2\over\binom Md}
 +4\sum_{k=1}^{\ell-1}
      {1\over\binom\ell k\binom M{d+k}}
 +{(c+1)^2\over\binom Mr}.}
\tag{3.7}
\]

The first term is \(4/M\) at \(d=1\). A ratio estimate in the middle
binomial sum, with the two endpoints separated, gives uniformly for
\(1\le d\le J\)

\[
 \Xi_1={4+o(1)\over m},
 \qquad
 \Xi_d=O(m^{-2})\quad(d\ge2).
\tag{3.8}
\]

This yields a global compatible-pair census. Since
\(\mathbf 1_{\{C_0(P,P')>0\}}\le C_0(P,P')\), Markov's inequality and
(3.7) give

\[
 \boxed{
 \sum_{R\in\binom{[n]}\ell}
 \#\{(P,P'):R\in\mathcal I_\ell(P)\cap\mathcal I_\ell(P'),\
                  C_0(P,P')=0\}
 \ge (1-O(m^{-1}))N_d\mathscr D_d^2.}
\tag{3.9}
\]

Thus deleting all entrance-incompatible packet pairs leaves
\(1-O(m^{-1})\) of the unrestricted common-lower-interval incidence.
This is a global incidence statement, not an independent-rank heuristic:
the conditioning and the entrance-overlap random variable are both exact.
It shows that the compatible catalogue itself has no negative covariance
of the required size. What remains undecided is whether a *near-factor*
can select an exceptionally floor-balanced subset of those pairs.

## 4. The exact extension cap

Fix \(R\in\binom{[n]}{r-d}\). If \(R\) occurs in a selected packet
\(e\), the rank-\(r\) intervals of \(e\) containing that occurrence are
exactly

\[
                         d+1
\tag{4.1}
\]

distinct extensions: add \(i\) labels at the left endpoint and
\(d-i\) labels at the right endpoint, for \(0\le i\le d\).

If two selected packets contain \(R\), all their displayed rank-\(r\)
extensions are distinct because \(\mathcal M\) is an entrance matching.
There are only

\[
                         \binom{n-r+d}{d}
\tag{4.2}
\]

rank-\(r\) supersets of \(R\). Hence

\[
                         (d+1)\mu_d(R)
 \le\binom{n-r+d}{d},
\tag{4.3}
\]

proving (0.13).

For \(d=1\), an occurrence has the form

\[
                         x,R,y
\tag{4.4}
\]

in its cyclic order. Its two entrance extensions are
\(R\cup\{x\}\) and \(R\cup\{y\}\). Thus different selected packets
through \(R\) use disjoint unordered endpoint pairs in
\([n]\setminus R\), proving (0.14).

These are genuine matching consequences, but they are quantitatively far
too weak. Already at \(d=1\), the maximum permitted load is
\((1/2+o(1))m\), whereas

\[
                         \frac{G}{N_1}=1+O_a(m^{-1/2})
\tag{4.5}
\]

at a critical leave. Thus the exact endpoint constraint allows almost
all occurrence mass to be concentrated on \(O(N_1/m)\) targets. Neither
the pointwise cap nor its first moment rules out \(\Theta(W)\) holes.

## 5. The exact domino twin and its global integral gate

Give a directed cyclic order \(P=(x_0,\ldots,x_{n-1})\) a marked even
phase, partition its positions into dominoes

\[
 \{0,1\},\{2,3\},\ldots,\{n-2,n-1\},
\tag{5.1}
\]

and let \(\tau\) exchange the two positions of every domino. Write
\(P^\tau=(x_{\tau(0)},\ldots,x_{\tau(n-1)})\). The mark is auxiliary;
after forming the pair, both cyclic orders are ordinary packets.

### Theorem 5.1 (full common-interval profile of the domino twin)

For every \(2\le\ell\le n-2\),

\[
 \boxed{
 |\mathcal I_\ell(P)\cap\mathcal I_\ell(P^\tau)|
 =
 \begin{cases}
 n/2,&\ell\text{ even},\\
 0,&\ell\text{ odd}.
 \end{cases}}
\tag{5.2}
\]

#### Proof

Identify position sets with subsets of \(\mathbb Z_n\). A
\(P^\tau\)-interval supported on a cyclic position interval \(J\) has,
in the \(P\)-labelling, position set \(\tau(J)\). Thus it is common
exactly when \(\tau(J)\) is also a cyclic interval.

If \(|J|\) is even and the first position of \(J\) is even, then \(J\)
is a union of whole dominoes and \(\tau(J)=J\). There are \(n/2\) such
starts. For the other parity of start, the two boundary dominoes are cut;
their singleton positions move to the opposite sides of those dominoes,
creating two separated boundary defects. Hence \(\tau(J)\) is not an
interval. If \(|J|\) is odd, exactly one boundary parity is mismatched,
and the same endpoint check leaves a gap at one boundary. Again
\(\tau(J)\) is not an interval. The exclusions \(\ell=1,n-1\) are the
singleton/complement exceptions. This proves (5.2). \(\square\)

Assume now that \(r\) is odd. Taking \(\ell=r-d\) in (5.2) gives

\[
 C_0(P,P^\tau)=0,
 \qquad
 C_d(P,P^\tau)=\frac n2\mathbf 1_{\{d\ {m odd}\}}.
\tag{5.3}
\]

The pair is therefore an entrance matching. Since its occurrence mass is
only \(2n\), every forced floor in the Gaussian annulus is zero, and

\[
 \boxed{
 \sum_{d=1}^{J}\widetilde E_d
 =\frac n2\left\lceil\frac J2\right\rceil
 =\Theta_{a,b}(m^{3/2}).}
\tag{5.4}
\]

This is the strongest local refutation of any attempted hereditary bound
from \(C_0=0\) alone.

Now form the domino-superpacket catalogue whose edge associated with a
marked \(P\) is

\[
 Q(P)=\mathcal I_r(P)\mathbin{\dot\cup}\mathcal I_r(P^\tau).
\tag{5.5}
\]

It is a \(2n\)-uniform multihypergraph on the \(N_0\) entrance targets.
Relabelling coordinates is transitive on its vertices, so constant weight
on all catalogue edges, normalized by the common vertex degree, is an
exact fractional perfect matching.

### Theorem 5.2 (a critical domino near-factor is a global counterexample)

Suppose the domino-superpacket catalogue has a matching of \(T\) edges
with

\[
 G=2nT=N_0-L,
 \qquad L=O(N_0/\sqrt m).
\tag{5.6}
\]

Then its \(2T\) constituent packets form an ordinary rank-\(r\) packet
matching and

\[
 \widetilde E_1\ge(1/4-o(1))N_0=\Theta_a(W).
\tag{5.7}
\]

Moreover, for some constant \(c=c(a,b)>0\),

\[
 \boxed{
 \sum_{1\le d\le c\sqrt m}\widetilde E_d
 =\Omega_{a,b}(W\sqrt m).}
\tag{5.8}
\]

#### Proof

Entrance disjointness inside a twin is (5.3), and disjointness between
different twins is the superpacket matching condition. At every odd
depth, one twin contributes two decks of size \(n\) whose union has size
\(3n/2\). Adding the twins one at a time therefore raises ordinary repeat
mass by at least \(n/2\) per twin, regardless of cross-twin collisions.
Thus

\[
 E_d\ge\frac{nT}{2}=\frac G4
 \qquad(d\text{ odd}).
\tag{5.9}
\]

At \(d=1\), the Gaussian ratio gives
\(N_0-N_1=O_a(W/\sqrt m)\). Hence the forced floor is
\(F_1=(G-N_1)_+=O_a(W/\sqrt m)\), and (5.7) follows.

Choose \(c>0\) so small that \(c<b-a\) and

\[
                         e^{-2ac-c^2}>\frac34.
\tag{5.10}
\]

Uniformly for \(d\le c\sqrt m\),
\(N_d/N_0\ge e^{-2ac-c^2}+o(1)\). Also

\[
 (G-N_d)_+\le N_0-N_d.
\tag{5.11}
\]

Equations (5.9)--(5.11) show that every odd such \(d\) has
\[
 \widetilde E_d
 \ge N_d-\frac34N_0-\frac14L
 \ge\eta_{a,b}W
\]
for a fixed \(\eta_{a,b}>0\).
There are \(\Theta_{a,b}(\sqrt m)\) odd depths, proving (5.8).
\(\square\)

The unproved statement in Theorem 5.2 is purely integral: does the
fractionally perfect domino-superpacket catalogue have a matching with
leave \(O(N_0/\sqrt m)\)? A positive answer gives a literal negative
answer to the synchronized annulus gate. A proof of the desired universal
\(o(W)\) bound must, at minimum, prove that this paired catalogue has no
such near-factor. Marginal incidence and local codegree data cannot do
that, because the uniform fractional point is exact.

## 5A. An all-parity coherent pair

We now construct the promised local obstruction. Put

\[
                         h=q_0+1.
\tag{5A.1}
\]

Partition \([n]\) into four ordered blocks

\[
 A=(a_1,\ldots,a_{r-1}),\qquad
 C=(c_1,\ldots,c_{r-1}),
\tag{5A.2}
\]

\[
 X=(x_1,\ldots,x_h),\qquad
 Y=(y_1,\ldots,y_h).
\tag{5A.3}
\]

The sizes add correctly because

\[
                         2(r-1)+2h=2m=n.
\tag{5A.4}
\]

Define two directed cyclic orders

\[
                         \pi=AXCY,
 \qquad                  \sigma=AYCX,
\tag{5A.5}
\]

using the displayed forward order inside every block. Reversal does not
affect any interval deck, so these define simple unoriented packets.

### Lemma 5A.1 (entrance decks are disjoint)

\[
                         \mathcal I_r(\pi)
 \cap\mathcal I_r(\sigma)=\varnothing.
\tag{5A.6}
\]

#### Proof

At block level, \(AXCY\) and \(AYCX\) traverse the same four-cycle in
opposite directions, while the order *inside* each block is kept forward
in both words.

An \(r\)-interval cannot lie inside one block: the two large blocks have
size \(r-1\), and the two small blocks have size \(h<r\). It cannot meet
all four blocks either. Indeed, an arc meeting all four contains two
whole adjacent middle blocks and at least one label from each endpoint
block. Those middle blocks have total size \((r-1)+h=m\), so the arc has
length at least \(m+2>r\).

Thus the nonempty block support is a proper path in the common
undirected four-cycle. The interval also cannot be a union of all the
blocks on that path. The one- and two-block sums are

\[
 r-1,\quad h,\quad (r-1)+h=m,
\tag{5A.7}
\]

and every three-block sum exceeds \(r\); none equals
\(r=m-q_0\).

Therefore every \(r\)-interval has a nonempty proper intersection with
at least one endpoint block of its support. If the same target were an
interval in both cycles, equality of the target sets would force the same
intersection with every named block, hence the same block support. The
two cycles traverse that proper support in opposite directions. In an
endpoint block, a forward traversal uses a prefix at one end of the path
and a suffix at the other. Consequently, in at least one endpoint block
the common intersection would have to be both a proper prefix and a
proper suffix of the same displayed injective word, with the same
cardinality. Those sets are unequal. Hence no common \(r\)-target exists.
\(\square\)

### Lemma 5A.2 (coherent annular profile)

For every \(1\le d\le J\),

\[
                         C_d(\pi,\sigma)\ge2d.
\tag{5A.8}
\]

#### Proof

The length \(r-d\) intervals lying completely inside \(A\) occur in both
cyclic orders, because \(A\) is a common forward block. Their number is

\[
                         (r-1)-(r-d)+1=d.
\tag{5A.9}
\]

The common block \(C\) supplies another \(d\) such intervals. The two
families use disjoint coordinate sets, proving (5A.8). \(\square\)

### Theorem 5A.3 (linear-size synchronized local counterexample)

The two packets \(\{\pi,\sigma\}\) form a rank-\(r\) cyclic-packet
matching, and

\[
 \boxed{
 \sum_{d=1}^{J}\widetilde E_d
 \ge2\sum_{d=1}^{J}d
 =J(J+1)=\Theta_{a,b}(m).}
\tag{5A.10}
\]

#### Proof

Lemma 5A.1 proves the entrance matching assertion. Here \(G=2n=4m\),
while every \(N_d\) is exponential in \(m\). Hence the forced floor is
zero at every displayed depth. With only two packets, a repeated target
is exactly a common interval of the two packets. Lemma 5A.2 and summation
prove (5A.10). \(\square\)

Since \(G=4m\), equation (5A.10) is \(\Omega_{a,b}(G)\). It is a literal
counterexample to every claim that entrance disjointness alone makes
synchronized repeat excess sublinear in the selected occurrence mass.
It is not a critical-leave counterexample, because its entrance leave is
\(N_0-O(m)\).

## 6. Separation of the two global pair gates

Call a pair of packets a block-reversal gadget if it is a coordinate
conjugate of the pair in Section 5A. Suppose a rank-\(r\) matching contains
\(g\) pairwise entrance-disjoint gadgets. Their internal common intervals
give the raw lower bound

\[
 \sum_{d=1}^{J}P_d\ge gJ(J+1).
\tag{6.1}
\]

For \(g=\Theta(W/m)\), the right side is \(\Theta(W)\). This identifies
the exact scale at which coherent packet pairs affect the desired error
term. It is not by itself a lower bound for
\(\sum_d\widetilde E_d\), because the full near-factor has a
\(\Theta(W\sqrt m)\) raw pair floor which must first be subtracted.

A genuine \(\Omega(W)\) repeat-excess construction must therefore do one
of the following:

1. pack block-reversal or other coherent gadgets at near-factor density
   and align their common intervals beyond the forced floor; or
2. create high-multiplicity target clusters, already permitted by the
   exact extension cap (4.3).

For the all-parity block gadget, the first task is a matching problem in
the \(2n\)-uniform hypergraph whose edges are the unions of the two
entrance decks, and even a near-factor would still require a separate
floor-alignment argument. The domino twin is sharper: by Theorem 5.2 its
near-factor alone already gives the counterexample, with no cross-pair
alignment assumption. In both cases the same growing-uniformity integral
matching issue as the original packet catalogue reappears. It is not
settled by the exact fractional point.

Conversely, a positive theorem through the pair-energy inequality (0.10)
must prove that both mechanisms contribute only \(o(W)\) to the
floor-correct discrepancy (0.18). A different direct hole argument could
in principle bypass that stronger certificate.

## 7. Audited boundary

Proved:

1. the exact common-interval pair identity (1.5);
2. the exact floor-correct sufficient bound (2.5);
3. complete-catalogue row and total incidence profiles (3.2)--(3.3);
4. the exact conditional entrance-overlap profile (3.7) and the global
   compatible-pair census (3.9);
5. the exact all-depth extension cap (4.3) and endpoint-pair normal form;
6. the domino twin's full alternating-depth profile and local aggregate
   excess \(\Theta(m^{3/2})\);
7. the conditional implication from a critical domino-superpacket
   near-factor to \(\widetilde E_1=\Omega(W)\) and aggregate
   \(\Omega(W\sqrt m)\); and
8. an all-parity literal pair with \(C_d\ge2d\) at every annular depth.

Not proved:

1. \(\sum_d\Phi_d/\kappa_d=o(W)\) for every critical-leave packet
   matching;
2. a critical-leave matching with \(\Omega(W)\) repeat excess;
3. a critical-leave near-factor of the domino-superpacket catalogue; or
4. coefficient one.

The exact decision is therefore narrower than either an automatic
positive theorem or a global counterexample. Shared leave closes the
scalar floor. The strongest direct pair-profile route is the
floor-correct common-interval certificate (0.18), and entrance matching
controls only its depth-zero row. The complete pair profiles and global
incidence counts do not propagate that control: (3.9) leaves essentially
all lower collision incidence available, and the domino twin turns that
freedom into an exact W-scale counterexample as soon as its paired
fractional factor can be rounded to the critical leave.
