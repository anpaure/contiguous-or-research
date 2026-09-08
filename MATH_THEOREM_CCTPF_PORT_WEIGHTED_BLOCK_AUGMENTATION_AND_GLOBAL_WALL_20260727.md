# CCTPF port-weighted block augmentation and the global exterior-wall obstruction

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

The isolated ladder nibble cannot be repaired by merely declaring a
vertical ladder to be one object: a complete history still has effective
conflict degree \((1-o(1))kD\). This note instead develops a genuinely
nonisolated augmentation rule.

Fix a target-simple CCTPF matching \(\mathcal M\). Remove an arbitrary
block \(S\subseteq\mathcal M\), adjoin one or more currently unmatched
roots, and reconfigure all roots of this block against the unchanged
exterior. The relevant quantity is not the number of exterior targets,
but their exact normalized **port exposure** inside each root fibre.

Let

\[
 p_*=\max\left\{
  \frac{L}{\binom{s}{H}},
  \max_{\substack{1\le q<H\\b_q>0}}
  \left{
   \frac{b_q}{\binom{s}{H-q}},
   \frac{b_q}{\binom{s}{H+q}}
  \right}
 \right\},
\tag{0.1}
\]

and

\[
                         k=L+2\sum_{q=1}^{H-1}b_q
                          =(\sqrt\pi+o(1))m^{3/2}.
\tag{0.2}
\]

The main positive result is the following exact block augmentation.

> Let \(A\) consist of the roots of \(S\) together with \(u\ge1\)
> unmatched roots, and put \(a=|A|=|S|+u\). Let \(\mathcal B_{\rm ext}\)
> be the target set used by \(\mathcal M\setminus S\). If the roots of
> \(A\) admit an order \(U_1,\ldots,U_a\) such that
> \[
>  \omega_{U_i}(\mathcal B_{\rm ext})+(i-1)kp_*<1
>  \qquad(1\le i\le a),
> \tag{0.3}
> \]
> then all \(a\) roots have new literal full histories which avoid the
> exterior and one another. Replacing \(S\) augments the matching by
> exactly \(u\).

Every column in this argument is one complete tail order with all middle,
lower, and upper ladders coupled. No ladder is re-expanded into separate
Hall choices.

At the calibrated height,

\[
 \boxed{
 \log\frac1{kp_*}
 \ge\left(\frac{\log2}{4}-o(1)\right)\sqrt{m\log m}.}
\tag{0.4}
\]

Thus (0.3) can reroute an exponentially large block whenever its exterior
exposure has fixed positive slack.

The same lemma yields a sharp obstruction for any maximum matching. If
\(S\) has \(r\) histories, \(U_0\) is unmatched, and
\(a=r+1\), then some root \(U\) among
\(\{U_0\}\cup\operatorname {root}(S)\) satisfies

\[
 \boxed{
 \omega_U(\mathcal B_{\rm ext})
 \ge1-(a-1)kp_*.}
\tag{0.5}
\]

In particular, for

\[
                         a\le\frac1{2kp_*},
\tag{0.6}
\]

one root sees exterior exposure at least \(1/2\), supplied by at least

\[
                         \frac1{2kp_*}
\tag{0.7}
\]

distinct exterior matched histories. Hence every failed polynomial or
subexponential augmenting block is attached to an exponential exterior
port wall.

This is a rigorous regeneration/augmentation lemma with full \(k\)-
dependence, plus its exact natural obstruction. It does not prove the
desired root leave \(o(N/\sqrt m)\): at that leave scale, the available
global port budget is still much larger than the exposure forced by
(0.5), so double counting gives no contradiction. A positive proof must
show that these exponential port walls cannot be globally interlocked,
or must augment through them by cancellations not visible to nonnegative
exposure.

## 1. Full-history port cylinders

Use the calibrated CCTPF parameters

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 M=m+H,\qquad s=m-H,\qquad L=m-3H+1,
\tag{1.1}
\]

and the fixed quotas

\[
 b_0=L,
\qquad
 b_q=\min\left\{L-1,
  \max\left\{0,\left\lfloor\frac{N_q}{N_H}\right\rfloor-1\right\}
 \right\}
 \quad(1\le q<H).
\tag{1.2}
\]

At each root \(U\), fix its audited \(2H\)-core and any one nested phase
family of these sizes. Let \(\Omega_U\) be the \(D=s!\) literal tail
orders over that root. For \(F\in\Omega_U\), let \(P(F)\) denote its
complete typed protected target set. It contains exactly \(k\) targets,
with every vertical ladder already coupled by the one tail order.

For a typed target \(T\), define its port cylinder in root \(U\) by

\[
                         \mathcal C_U(T)
 =\{F\in\Omega_U:T\in P(F)\},
\tag{1.3}
\]

and put

\[
                         p_U(T)=\frac{|\mathcal C_U(T)|}{D}.
\tag{1.4}
\]

The exact single-port count is

\[
 p_U(T)=
 \begin{cases}
  L/\binom{s}{H},&T\text{ is a compatible middle target},\\[1mm]
  b_q/\binom{s}{H-q},&T\text{ is compatible at upper depth }q,\\[1mm]
  b_q/\binom{s}{H+q},&T\text{ is compatible at lower depth }q,\\[1mm]
  0,&T\text{ is incompatible with }U.
 \end{cases}
\tag{1.5}
\]

In particular,

\[
                              0\le p_U(T)\le p_*.
\tag{1.6}
\]

For a target family \(\mathcal B\), define its additive port exposure
and exact cylinder coverage by

\[
 \omega_U(\mathcal B)=\sum_{T\in\mathcal B}p_U(T),
\tag{1.7}
\]

\[
 \beta_U(\mathcal B)
 =\frac1D\left|\bigcup_{T\in\mathcal B}\mathcal C_U(T)\right|.
\tag{1.8}
\]

Then

\[
                         \beta_U(\mathcal B)\le
                         \min\{1,\omega_U(\mathcal B)\}.
\tag{1.9}
\]

The root has a literal history avoiding every target in \(\mathcal B\)
if and only if

\[
                         \beta_U(\mathcal B)<1.
\tag{1.10}
\]

Thus \(\omega_U<1\) is a quantitative sufficient condition, while
\(\beta_U=1\) is the exact obstruction for one frozen exterior.

### Lemma 1.1 (one history has port weight at most \(kp_*\))

For arbitrary roots \(U,V\) and a history \(F\in\Omega_V\),

\[
 \boxed{
                         \omega_U(P(F))\le kp_*.}
\tag{1.11}
\]

#### Proof

The history contains exactly \(k\) typed targets, and every one has
port exposure at most \(p_*\) in root \(U\). Sum (1.6). \(\square\)

This is the sole place where the large all-rank history size enters the
augmentation. Because the ladders are contracted, it is charged once as
the exact total port weight of one complete history, not through a
separate matching at every rank.

## 2. Port-weighted block augmentation

Let \(\mathcal M\) be any target-simple rooted matching. Thus its
histories have distinct roots and pairwise disjoint protected target
sets. Let \(S\subseteq\mathcal M\), and let \(R\) be a nonempty set of
roots not saturated by \(\mathcal M\). Put

\[
 A=R\mathbin{\dot\cup}\operatorname {root}(S),
 \qquad a=|A|=|R|+|S|,
\tag{2.1}
\]

and define the frozen exterior target set

\[
 \mathcal B_{\rm ext}
 =\bigcup_{F\in\mathcal M\setminus S}P(F).
\tag{2.2}
\]

### Theorem 2.1 (ordered block augmentation)

Suppose the roots of \(A\) can be ordered as
\(U_1,\ldots,U_a\) so that

\[
 \boxed{
 \omega_{U_i}(\mathcal B_{\rm ext})+(i-1)kp_*<1
 \qquad(1\le i\le a).}
\tag{2.3}
\]

Then there are literal histories \(F_i\in\Omega_{U_i}\) such that

1. every \(P(F_i)\) avoids \(\mathcal B_{\rm ext}\); and
2. the sets \(P(F_1),\ldots,P(F_a)\) are pairwise disjoint.

Consequently

\[
 \mathcal M'
 =(\mathcal M\setminus S)\cup\{F_1,\ldots,F_a\}
\tag{2.4}
\]

is a matching and

\[
                         |\mathcal M'|-|\mathcal M|=|R|.
\tag{2.5}
\]

#### Proof

Choose the histories in the displayed order. Suppose
\(F_1,\ldots,F_{i-1}\) have already been chosen. The forbidden family
for root \(U_i\) is

\[
 \mathcal B_i
 =\mathcal B_{\rm ext}
  \cup P(F_1)\cup\cdots\cup P(F_{i-1}).
\tag{2.6}
\]

Subadditivity of \(\omega\), Lemma 1.1, and (2.3) give

\[
 \begin{aligned}
 \omega_{U_i}(\mathcal B_i)
 &\le\omega_{U_i}(\mathcal B_{\rm ext})
      +\sum_{j<i}\omega_{U_i}(P(F_j))\\
 &\le\omega_{U_i}(\mathcal B_{\rm ext})+(i-1)kp_*<1.
 \end{aligned}
\tag{2.7}
\]

Equations (1.9)--(1.10) now give a literal history \(F_i\) avoiding
\(\mathcal B_i\). Induction constructs all histories. They avoid the
exterior and one another, proving (2.4). The root count in (2.1) gives
(2.5). \(\square\)

This is a nonisolated contention rule: the old histories in \(S\) may
have arbitrarily many conflicts with the new ones and are removed as one
block. The new histories are not required to have been isolated tentative
choices.

### Corollary 2.2 (uniform-slack augmentation)

If

\[
 \max_{U\in A}\omega_U(\mathcal B_{\rm ext})\le1-\eta
\tag{2.8}
\]

and

\[
                         (a-1)kp_*<\eta,
\tag{2.9}
\]

then the block augments by \(|R|\).

In particular, any block with exterior exposure at most \(1/2\) may
contain

\[
                         a\le\frac1{2kp_*}
\tag{2.10}
\]

roots, up to harmless strict-inequality rounding.

## 3. The obstruction left by a maximum matching

The augmentation theorem has an exact contrapositive.

### Theorem 3.1 (robust exterior port wall)

Let \(\mathcal M\) be a maximum matching, let
\(R\ne\varnothing\) be any set of its unmatched roots, and let
\(S\subseteq\mathcal M\). Put \(A\) and \(a\) as in (2.1). Then

\[
 \boxed{
 \max_{U\in A}\omega_U(\mathcal B_{\rm ext})
 \ge1-(a-1)kp_*.}
\tag{3.1}
\]

#### Proof

If every root had exposure strictly below the right side, any ordering of
\(A\) would satisfy (2.3). Theorem 2.1 would produce a matching larger by
\(|R|\), contradicting maximality. \(\square\)

For one unmatched root and \(r\) removed histories, (3.1) says that the
failure of an \((r+1)\)-root augmenting block forces one of its roots to
retain exterior exposure at least

\[
                         1-rkp_*.
\tag{3.2}
\]

### Corollary 3.2 (exponential blocker support)

Assume

\[
                         a\le\frac1{2kp_*}.
\tag{3.3}
\]

Then some root \(U\in A\) satisfies

\[
                         \omega_U(\mathcal B_{\rm ext})\ge\frac12.
\tag{3.4}
\]

Moreover at least \(1/(2kp_*)\) distinct histories of
\(\mathcal M\setminus S\) have positive port exposure in \(U\).

#### Proof

Equation (3.4) is immediate from (3.1). Decompose the exterior into its
pairwise target-disjoint histories:

\[
 \omega_U(\mathcal B_{\rm ext})
 =\sum_{F\in\mathcal M\setminus S}\omega_U(P(F)).
\tag{3.5}
\]

Every summand is at most \(kp_*\) by Lemma 1.1. A sum at least \(1/2\)
therefore has at least \(1/(2kp_*)\) positive summands. \(\square\)

This is the exact obstruction encountered by an augmenting-path search.
Before a port-weighted block can close, at least one of its roots branches
to exponentially many exterior matched histories. A bounded blossom, a
polynomial augmenting tree, or a subexponential union of odd-port prisms
cannot be a closed terminal obstruction under this rule.

## 4. Full calibrated size of the augmentation radius

Let

\[
 t_*=\left\lceil
       \frac{(m-H+1)\log2}{2H-1}
      \right\rceil.
\tag{4.1}
\]

Every active deletion length is at least \(t_*\). Consequently

\[
                         p_*\le\frac L{\binom{s}{t_*}}.
\tag{4.2}
\]

Indeed, if \(b_q>0\), then the definition of \(b_q\) implies

\[
 \frac{N_q}{N_H}\ge2.
\tag{4.2a}
\]

For \(0\le q<H\),

\[
 \log\frac{N_q}{N_H}
 =\sum_{j=q+1}^{H}\log\frac{m+j}{m-j+1}
 \le (H-q)\frac{2H-1}{m-H+1}.
\tag{4.2b}
\]

Thus every active upper deletion length \(H-q\) is at least \(t_*\).
The middle deletion length is \(H\), and every lower deletion length
\(H+q\) is larger still. Since all these lengths are at most \(2H-1<s/2\)
for large \(m\), monotonicity of \(\binom{s}{t}\), together with
\(b_q\le L\), proves (4.2).

At the calibrated height,

\[
 t_*=\left(\frac{\log2}{2}+o(1)\right)
       \sqrt{\frac m{\log m}},
\tag{4.3}
\]

and

\[
 \log\binom{s}{t_*}
 \ge\left(\frac{\log2}{4}-o(1)\right)\sqrt{m\log m}.
\tag{4.4}
\]

Here (4.3) follows directly from (4.1). Also \(t_*=o(s)\), so

\[
 \log\binom{s}{t_*}
 \ge t_*\log\frac{s}{t_*}
 =\left(\frac{\log2}{4}-o(1)\right)\sqrt{m\log m},
\tag{4.4a}
\]

which proves (4.4).

Since \(kL\) is polynomial in \(m\),

\[
 \boxed{
 \frac1{kp_*}
 \ge
 \exp\left\{
  \left(\frac{\log2}{4}-o(1)\right)\sqrt{m\log m}
 \right\}.}
\tag{4.5}
\]

Thus Theorem 2.1 is not merely a bounded-switch lemma. With fixed
exterior slack it simultaneously reconfigures an exponential number of
roots, while preserving every vertical ladder and every common-history
constraint.

## 5. Why the lemma does not yet force the desired leave

Let \(\ell=N-|\mathcal M|\) be the root leave. The synchronized CCTPF
hole identity requires

\[
                              \ell=o(N/\sqrt m).
\tag{5.1}
\]

Theorem 3.1 shows that a maximum matching with \(\ell>0\) must carry a
robust exterior port wall around every small augmenting block. But the
available scalar port budget does not contradict such a wall.

Indeed, for a typed target \(T\), let

\[
                         \rho(T)=\sum_U p_U(T).
\tag{5.2}
\]

The audited common-core degree caps give

\[
                              \rho(T)\le1.
\tag{5.3}
\]

To spell out this step, at signed rank \(r\) put
\(d_r=\binom{s}{H-r}\). A target is compatible with at most
\(d_r/b_{|r|}\) roots, and each compatible root contributes exactly
\(b_{|r|}/d_r\) to (5.2). At the middle rank the corresponding two
quantities are \(d_0/L\) and \(L/d_0\). Their products are one, proving
(5.3) at every protected rank.

Therefore every matched history \(F\) obeys

\[
 \sum_U\omega_U(P(F))
 =\sum_{T\in P(F)}\rho(T)\le k.
\tag{5.4}
\]

Summing over the matching yields only

\[
 \sum_U\omega_U(\mathcal B_{\mathcal M})
 \le k|\mathcal M|\le kN.
\tag{5.5}
\]

Even if every unmatched root requires exposure at least one, (5.5)
gives merely

\[
                              \ell\le kN,
\]

which is vacuous. At the critical target leave
\(\ell=N/\sqrt m\), the ratio between the available budget \(kN\) and
the forced exposure \(\ell\) is

\[
                              k\sqrt m=\Theta(m^2).
\tag{5.6}
\]

Thus no unweighted or first-moment double count can turn the exponential
local repair radius into (5.1). One needs a new statement limiting how
many unmatched-root port walls one matched history can support
simultaneously, or a signed/cancellative augmentation which crosses a
wall of additive exposure at least one.

## 6. Contiguous phase blocks and vertical contraction

The block augmentation acts on complete histories, but it is compatible
with a contiguous-phase implementation. An adjacent transposition of two
tail labels changes a target only when its deletion interval contains
exactly one of the two positions. At a fixed deletion length there are at
most two such phase intervals. Hence one adjacent tail transposition
changes at most

\[
                              4H-2
\tag{6.1}
\]

protected trace cells, across all signed ranks.

More generally, permuting a contiguous tail block of \(B\) positions can
change only trace intervals meeting that block boundary or interior. The
number of affected phase--rank cells is at most

\[
 O(H(B+H)).
\tag{6.2}
\]

These bounds show why contiguous-block switches are physically local.
They do not by themselves prove augmentation: near a terminal matching,
the exterior port exposure of a root can be order one or larger even when
each individual switch changes only \(O(H(B+H))\) cells. Theorem 2.1
identifies the exact additional condition under which such local switches
can be completed to an unrestricted literal tail order.

## 7. Audited boundary

Proved:

1. the exact additive and union port exposures for a frozen exterior;
2. the ordered multi-root block augmentation theorem (2.3);
3. its uniform-slack exponential-radius corollary;
4. the robust exterior-wall obstruction for every maximum matching;
5. the exponential blocker-support lower bound;
6. the exact global first-moment barrier at the target leave
   \(N/\sqrt m\); and
7. locality of adjacent and contiguous tail-block switches.

Not proved:

1. exclusion of a globally interlocked exponential port wall;
2. a cancellative augmentation across exposure at least one;
3. a matching with root leave \(o(N/\sqrt m)\); or
4. coefficient one.

The strongest exact conclusion is that nonisolated augmentation works on
blocks of exponential size whenever the frozen exterior leaves fixed port
slack. The only surviving obstruction is a genuinely global exterior wall
which blocks every small alternating block through exponentially many full
histories. This is the precise successor to the dead isolated ladder
nibble.
