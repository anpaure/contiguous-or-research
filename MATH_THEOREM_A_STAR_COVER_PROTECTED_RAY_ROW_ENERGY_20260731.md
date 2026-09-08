# Star-covered upper rays and Catalan-scale C6 row energy

Date: 2026-07-31  
Lane: A, arbitrary-width upper guards on the \(m^{-2}\)-thinned C6 reservoir  
Status: exact protected-energy implication and alteration constants proved;
SCPR alone is shown insufficient; boundary-local ray exposure is the remaining
upper-witness hypothesis

## 0. Verdict

The bad-pair star-cover theorem is compatible with the Catalan-scale
average-load extraction.  Its direct effect is only list pruning:

\[
                         m^2\longmapsto m^2-Kmd.                  \tag{0.1}
\]

It does not itself add cross-list row energy.

To protect arbitrary-width targets simultaneously, however, each surviving
packet must carry a composable witness certificate.  If all such certificates
compress into \(O(d)\) protected rays per packet and each ray has full-atlas
invalidation exposure \(O(m^3)\), then the complete upper-guard row energy is

\[
                              O(dm^3).                            \tag{0.2}
\]

Bernoulli thinning at density \(m^{-2}\), per-list alteration and Haxell then
extract a Catalan-scale compatible packet bank whenever \(d=o(m)\).

The exposure hypothesis is essential.  SCPR controls which choices are bad
at one anchor in isolation; it does not control how packets at different
anchors can jointly destroy complementary old witnesses.  A two-witness
schema has empty bad graph at every anchor but arbitrarily large cross-list
witness energy.  Thus the positive route is exact but conditional:

> prove a boundary-local protected-ray certificate, together with the same
> row bound for common-cap and topology tickets.

## 1. Guarded lists and row energy

Let \({\cal E}\) be an eligible directed-incidence anchor bank.  At anchor
\(e\), the raw list \({\cal P}_e^0\) consists of the \(m^2\) standard
incidence C6s.  Let \(G_e^{\rm bad}\) be the union bad graph of the complete
protected upper bank.

Assume

\[
                         \tau(G_e^{\rm bad})\le Kd                \tag{1.1}
\]

for every \(e\), and delete every bad parameter pair.  The safe list
\({\cal P}_e\) has size

\[
 L_e\ge m^2-Kmd=\alpha_m m^2,\qquad
 \alpha_m:=1-\frac{Kd}{m}.                                       \tag{1.2}
\]

For raw physical tokens, let \(K_{\rm raw}(e,f)\) denote the average number
of token-conflict witnesses from one candidate at \(e\) into the list at
\(f\).  The exact complete-atlas identity is

\[
 \sum_{f\ne e}K_{\rm raw}(e,f)
   =R_m:=18m^3+51m^2-4m-5<44m^3.                                \tag{1.3}
\]

Restriction to safe lists can only lower its numerator.  Renormalizing by
\(L_e\) gives

\[
 \frac1{L_e}\sum_{p\in{\cal P}_e}
       \deg_{\rm raw}(p;{\cal E}\setminus\{e\})
       \le\frac{R_m}{\alpha_m}.                                  \tag{1.4}
\]

Thus SCPR contributes no external-energy term.  It changes the raw row only
by the factor \(1/\alpha_m\).

## 2. Protected-ray tickets

For each safe packet \(p\in{\cal P}_e\), let \({\cal T}(p)\) be a set of
occurrence-labelled protected-ray tickets.  A ticket may stand for an entire
nested arbitrary-width tower, but it must have literal semantics:

1. if every ticket in \({\cal T}(p)\) survives, then \(p\) preserves every
   protected upper target assigned to it;
2. for a ticket \(\rho\), the relation \(q\triangleright\rho\) means that
   packet \(q\) cuts, contaminates or otherwise invalidates that certificate;
3. any selected pair with \(q\triangleright\rho\in{\cal T}(p)\) is declared
   a conflict.

Define the full eligible-atlas exposure

\[
 \Lambda(\rho)=
   \#\{(f,q):f\in{\cal E},\ q\in{\cal P}_f,\ q\triangleright\rho\}. \tag{2.1}
\]

For \(p\in{\cal P}_e\), also let

\[
 \Gamma(p)=
 \#\{(f,q,\rho):f\ne e,\ q\in{\cal P}_f,\ \rho\in{\cal T}(q),
                         \ p\triangleright\rho\}.                  \tag{2.1a}
\]

The quantity \(\Lambda(\rho)\) counts packets attacking one ticket;
\(\Gamma(p)\) counts tickets attacked by one packet.  A pointwise bound on
the first does not give a pointwise bound on the second.

### Definition 2.1 (boundary-local protected rays)

The guarded atlas has \((s_0,s_1,\lambda,d)\)-BLPR if

\[
                         |{\cal T}(p)|\le s_0d+s_1                \tag{2.2}
\]

for every safe packet and

\[
                         \Lambda(\rho)\le\lambda m^3              \tag{2.3}
\]

for every ticket used by a safe packet.

An internal packet-private witness has \(\Lambda(\rho)=0\).  A sufficient
physical realization of (2.3) is that invalidating \(\rho\) requires
touching one of at most \(h\) named local rank-\(m\), rank-\((m+1)\), or
incidence tokens, where \(h\) is constant.  Their complete-atlas loads are
at most \(3(m+1)m^2\) and \(6m^2\), so one may take

\[
                         \lambda\le 6h                            \tag{2.4}
\]

for \(m\ge1\), after a harmless common constant enlargement.

The word “boundary-local” is substantive.  A certificate whose invalidation
set contains all packet supports along a ray of physical length \(\ell\) has
only the weaker bound \(O(\ell m^3)\).

## 3. Exact protected-energy theorem

### Theorem 3.1 (SCPR + BLPR positive-density row bound)

Assume \(\alpha_m>0\), (1.1), and BLPR.  If the full packet conflict graph
contains the raw token conflicts and every ticket-invalidation conflict,
then there is a subbank

\[
                         {\cal E}^\sharp\subseteq{\cal E},\qquad
                         |{\cal E}^\sharp|\ge|{\cal E}|/2          \tag{3.1}
\]

such that every \(e\in{\cal E}^\sharp\) has

\[
 \overline\Delta_e^{\rm full}
 :=\frac1{L_e}\sum_{p\in{\cal P}_e}
      \deg_{\rm full}(p;{\cal E}\setminus\{e\})
 \le
 \frac{R_m}{\alpha_m}
 +\lambda(s_0d+s_1)m^3
 +\frac{2\lambda(s_0d+s_1)}{\alpha_m}m^3.                        \tag{3.2}
\]

In particular, if \(d\ge1\) and \(Kd\le m/2\), then

\[
 \overline\Delta_e^{\rm full}
 \le C_{\rm up}\,d\,m^3,\qquad
 C_{\rm up}:=88+5\lambda(s_0+s_1).                               \tag{3.3}
\]

#### Proof

Equation (1.4) bounds the raw part.  The attacks directed into tickets
named by one packet obey

\[
\begin{aligned}
 \frac1{L_e}\sum_{p\in{\cal P}_e}
  \sum_{\rho\in{\cal T}(p)}\Lambda(\rho)
 &\le
 \frac1{L_e}\sum_{p\in{\cal P}_e}
       (s_0d+s_1)\lambda m^3  \\
 &=\lambda(s_0d+s_1)m^3.
\end{aligned}                                                     \tag{3.4}
\]

It remains to control the reverse direction.  Put
\(s=s_0d+s_1\).  The total number of directed packet-to-ticket attacks is
at most

\[
 \sum_{f,q}\sum_{\rho\in{\cal T}(q)}\Lambda(\rho)
       \le |{\cal E}|\,m^2s\,\lambda m^3.                         \tag{3.5}
\]

Because every \(L_e\ge\alpha_m m^2\),

\[
 \sum_{e\in{\cal E}}\frac1{L_e}\sum_{p\in{\cal P}_e}\Gamma(p)
       \le\frac{|{\cal E}|s\lambda m^3}{\alpha_m}.                \tag{3.6}
\]

Delete anchors whose last displayed average exceeds
\(2s\lambda m^3/\alpha_m\).  At least half remain, proving (3.1).  On this
subbank, restriction cannot increase any degree.  Add the raw bound, (3.4),
and the surviving reverse bound to obtain (3.2).  Under \(Kd\le m/2\),
\(\alpha_m\ge1/2\), \(R_m/\alpha_m<88m^3\), and
\(s\le(s_0+s_1)d\), giving (3.3). \(\square\)

Exactly the same two-direction proof covers cap, sink, residence and
topology tickets.
Their ticket counts and exposure constants must be added to \(s_0,s_1\)
and \(\lambda\); local upper BLPR does not imply those rows.

## 4. Catalan-scale alteration with explicit constants

The row-energy extraction works on any eligible bank \({\cal E}_0\subseteq
{\cal E}\) for which (3.3) holds with the sum restricted to
\({\cal E}_0\).

### Theorem 4.1 (protected Catalan extraction)

Suppose every anchor in \({\cal E}_0\) has a guarded list of size at least
\(\alpha m^2\), and

\[
                         \overline\Delta_e^{\rm full}
                              \le Cdm^3                            \tag{4.1}
\]

in the full eligible bank.  Retain every anchor independently with
probability \(p=m^{-2}\).  There is a deterministic survivor bank
\({\cal S}\) with

\[
                         |{\cal S}|\ge
                         \frac{3|{\cal E}_0|}{4m^2}               \tag{4.2}
\]

such that every survivor list has average external degree at most

\[
                              4Cdm.                               \tag{4.3}
\]

Deleting from each survivor list the candidates of degree greater than
\(8Cdm\) retains at least \(\alpha m^2/2\) choices per list and leaves
maximum degree at most \(8Cdm\).  Hence Haxell selects one packet from every
survivor list whenever

\[
                         \alpha m^2\ge32Cdm.                      \tag{4.4}
\]

#### Proof

Conditional on retaining \(e\), linearity and (4.1) give expected average
external degree at most \(pCdm^3=Cdm\).  Mark \(e\) bad if this average
exceeds \(4Cdm\).  Conditional Markov makes its bad probability at most
\(1/4\), so the expected number of retained nonbad anchors is at least
\(3p|{\cal E}_0|/4\).  Some outcome attains (4.2), and deleting bad anchors
cannot increase degrees.

Within each surviving list, Markov at twice (4.3) retains at least half the
choices.  The induced maximum degree is at most \(8Cdm\).  Haxell requires
part size at least twice maximum degree, which is precisely (4.4).
\(\square\)

When \(|{\cal E}_0|=\Theta(I)\), (4.2) is
\(\Theta(I/m^2)=\Theta(W/m)\), the required Catalan scale.  If
\(\alpha,C\) are fixed and \(d=o(m)\), (4.4) holds eventually.

The theorem extracts an existential compatible reservoir.  A prescribed
leave still needs a spread task-to-anchor eligibility distribution; ordinary
Hall does not imply that quantifier.

## 5. Why SCPR alone does not bound row energy

The gap is already visible with two occurrence-labelled old witnesses.
Let a target \(Y\) have exactly two protected witnesses \(H_0,H_1\).  At
each of \(J\) abstract anchor lists, split the \(L=m^2\) candidates equally
into:

* type 0, which cuts \(H_0\) and leaves \(H_1\);
* type 1, which cuts \(H_1\) and leaves \(H_0\).

Every candidate individually preserves \(Y\).  Hence every individual
bad-pair graph is empty:

\[
                         G_e^{\rm bad}=\varnothing,\qquad
                         \tau(G_e^{\rm bad})=0.                   \tag{5.1}
\]

But one type-0 and one type-1 packet jointly cut both witnesses.  If this
joint loss is represented as the required cross-list conflict, each packet
conflicts with \(L/2\) candidates in every other list, and every list has
average external degree

\[
                              \frac{(J-1)L}{2}.                    \tag{5.2}
\]

This can exceed \(dm^3\) by an arbitrary factor as \(J\) grows.  The schema
uses exactly the old-witness alternative in the last-witness theorem and no
bad choice at one anchor; it proves that SCPR is not a simultaneous
certificate.

This is a logical obstruction at the exact occurrence-ticket interface.  It
is not asserted to be a materialized complete Johnson C6 atlas.  Its role is
to identify the missing implication: individual last-witness safety does not
give bounded joint witness exposure.

A second obstruction is geometric.  If one nested ray ticket is invalidated
by touching any of \(\ell\) independent boundary tokens, its exposure can be
\(\Theta(\ell m^3)\).  Arbitrary target width does not bound \(\ell\).
Therefore “\(O(d)\) rays” yields (0.2) only after proving that each ray is
represented by \(O(1)\) boundary-local invalidation tokens.

## 6. Exact remaining upper theorem

The positive route reduces to the following statement.

### Protected-ray energy (PRE)

For every eligible source anchor of the actual extensive leave:

1. the complete protected upper bank satisfies \(\operatorname{SCPR}(K,d)\);
2. every safe packet has an occurrence-labelled certificate for all old and
   regenerated upper targets which compresses into \(O(d)\) rays;
3. invalidating any one ray is witnessed by \(O(1)\) local Boolean
   vertex/incidence tokens, or more generally has full eligible-atlas
   exposure \(O(m^3)\); and
4. the cap, sink, topology, residence and physical replay tickets obey the
   same aggregate \(O(dm^3)\) row.

PRE and Theorem 3.1 give the full row-energy hypothesis needed by Theorem
4.1.  This is weaker than maximum weighted-code control: individual tokens
may have large maximum load, and high-degree packet choices are discarded
after thinning.  It is stronger than SCPR, because it controls simultaneous
certificate destruction across anchors.

No current Pascal/RSB theorem proves PRE.  The exact canonical per-seam
endpoint collar has the opposite polarity (bad graph \(K_{m,m-1}\)), while
the favorable key-preloaded collar proves list survival but not the global
ray-exposure row.  Thus the \(m^{-2}\) reservoir removes the maximum-load
obstruction, but the smallest live arbitrary-width gate is now the
boundary-local PRE statement.

## 7. Scope audit

1. The \(Kmd\) star-cover term is a within-list deletion count.  It is not
   added again as cross-list energy.
2. Row energy is an average over candidates in each list.  An average only
   over anchors is insufficient for the per-list Markov step.
3. The ticket relation must be composition-complete.  Pairwise
   nonadjacency is useful only when all simultaneous witness, cap and
   topology failures are represented.
4. A positive-density eligible anchor bank is needed before \(m^{-2}\)
   thinning can leave Catalan order.
5. The theorem proves a compatible packet reservoir under PRE, not
   prescribed-task absorption, regenerative closure, or
   \(\nu(k)\le B(k)+O(1)\).
